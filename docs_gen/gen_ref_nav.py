# Auto-generate one API reference page per module using mkdocstrings
from __future__ import annotations
from pathlib import Path
import mkdocs_gen_files

PACKAGE = "fallrisk_kit"
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / PACKAGE
API_DIR = Path("api")

# API index page
with mkdocs_gen_files.open(API_DIR / "index.md", "w") as f:
    f.write(
        (
            """
            # API Reference

            This section is auto-generated from the source code using `mkdocstrings`.

            - One page per module in `fallrisk_kit`
            - Functions, classes, and module docstrings are rendered
            """
        ).lstrip()
    )

for path in sorted(SRC.rglob("*.py")):
    module_path = path.relative_to(ROOT).with_suffix("")
    dotted = ".".join(module_path.parts)
    if not dotted.startswith(PACKAGE):
        continue

    rel_parts = module_path.parts[1:]  # strip the package name from path
    out_name = "package.md" if not rel_parts else "/".join(rel_parts) + ".md"
    out_path = API_DIR / out_name

    mkdocs_gen_files.set_edit_path(out_path, str(path.relative_to(ROOT)))

    with mkdocs_gen_files.open(out_path, "w") as f:
        f.write(f"# `{dotted}`\n\n")
        f.write(
            f"""
            ::: {dotted}
                options:
                  members_order: source
                  show_source: true
                  separate_signature: true
                  docstring_style: google
            """
        )
