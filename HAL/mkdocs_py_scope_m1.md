### Short answer
MkDocs itself doesn’t “scan .py files.” To build API docs from all your Python modules, you:
- Use `mkdocstrings` to render docstrings.
- (Optionally) use `mkdocs-gen-files` to auto-generate one Markdown page per module so you don’t have to list them manually.
- Point your `nav` at the generated `api/` directory so all modules appear automatically.

Below is a copy‑pasteable setup that works with your current `mkdocs.yml` (you already have `mkdocstrings`, `gen-files`, and `section-index` configured).

### 1) Create a generator script to enumerate all .py modules
Create `docs_gen/gen_ref_nav.py` (path matches your `mkdocs.yml`) with content like this. Adjust the `PACKAGES` list to include the top‑level packages you want documented (e.g., `fallrisk_kit`, and optionally `infra` if it’s importable and has docstrings you want exposed).

```python
# docs_gen/gen_ref_nav.py
from __future__ import annotations
import pathlib
import mkdocs_gen_files

# Top-level Python packages in your repo to document
PACKAGES = [
    "fallrisk_kit",
    # "infra",  # Uncomment if you want to include this and it’s a proper package
]

nav = mkdocs_gen_files.Nav()

for package in PACKAGES:
    pkg_path = pathlib.Path(package.replace(".", "/"))
    if not pkg_path.exists():
        continue

    for path in sorted(pkg_path.rglob("*.py")):
        # Skip private modules and test files if desired
        if any(part.startswith("_") for part in path.parts):
            continue
        if path.name.startswith("_"):
            continue
        # Optionally skip tests
        if "tests" in path.parts:
            continue

        # Convert file path to dotted module path
        module_path = path.with_suffix("")
        if module_path.name == "__init__":
            module_path = module_path.parent
        dotted = ".".join(module_path.parts)

        # Where to write the doc page under docs/ (mkdocs-gen-files writes into a virtual FS)
        doc_path = pathlib.Path("api", *module_path.parts).with_suffix(".md")
        doc_path.parent.mkdir(parents=True, exist_ok=True)

        # Build the page content rendered by mkdocstrings
        with mkdocs_gen_files.open(doc_path, "w") as fd:
            title = dotted
            fd.write(f"# `{title}`\n\n")
            fd.write(f"::: {dotted}\n")
            fd.write("    options:\n")
            fd.write("      show_root_heading: true\n")
            fd.write("      show_source: true\n")

        # Add to navigation
        nav[dotted] = doc_path.as_posix()

# Optional: create an index page for the API section
index_path = pathlib.Path("api", "index.md")
with mkdocs_gen_files.open(index_path, "w") as fd:
    fd.write("""
# API Reference

This section is generated automatically from the project’s Python docstrings.
    """.strip()
    )

# Option 1 (simple): rely on MkDocs directory mapping in `nav:` (see Step 2)
# Option 2 (literate nav): write a summary file and include via a plugin that supports !include
# with mkdocs_gen_files.open("api/SUMMARY.md", "w") as nav_file:
#     nav_file.write(nav.build_literate_nav())
```

Notes:
- This script creates `docs/api/...` pages at build time (virtually). No files are committed.
- If you want a single page per top-level package rather than per-module pages, change the loop to only write for packages and use the `::: package` directive with `filters`/`selection` options.

### 2) Point your nav to the generated directory
You already have:

```yaml
nav:
  - Home: index.md
  - Architecture: architecture.md
  - Stacks: stacks.md
  - Usage: usage.md
  - API Reference:
      - Overview: api/index.md
```

Add the directory mapping so MkDocs will include every generated page under `api/`:

```yaml
nav:
  - Home: index.md
  - Architecture: architecture.md
  - Stacks: stacks.md
  - Usage: usage.md
  - API Reference:
      - Overview: api/index.md
      - Packages: api/
```

MkDocs will now pick up all pages under `api/` (which the generator creates to mirror your package/module structure).

### 3) Ensure mkdocstrings can import your code
`mkdocstrings` must be able to import your packages. Common pitfalls:
- Build from the project root so the packages are on `PYTHONPATH`.
- If your package requires extras for import, install them in the same environment used by `mkdocs`.
- If needed, you can customize the Python handler to adjust `sys.path` via `setup_commands`:

```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          setup_commands:
            - import sys, pathlib
            - sys.path.append(str(pathlib.Path('.').resolve()))
```

### 4) Run the site
- Live preview: `mkdocs serve`
- Build: `mkdocs build`

As you add or change `.py` files, the generator will produce matching pages, and `mkdocstrings` will render docstrings automatically.

### Alternative: manual pages without a generator
If you prefer not to generate files, create Markdown pages under `docs/api/` that reference your modules explicitly using the `mkdocstrings` directive:

```markdown
# API: fallrisk_kit.alerts

::: fallrisk_kit.alerts
    options:
      show_root_heading: true
      show_source: true
```

Then list each page in `nav`. The generator simply automates creating one such page for every module.

### Troubleshooting tips
- Empty pages: ensure your modules have docstrings (Google style is already configured).
- Import errors: verify the package is importable from the build environment and that any optional dependencies are installed.
- Too many internals appearing: adjust `filters` (e.g., `filters: ["!^_"]`) or `selection` options in the directive to exclude private members.

This setup gives you “make mkdocs pick up all .py files with documentation” behavior, with minimal ongoing maintenance.