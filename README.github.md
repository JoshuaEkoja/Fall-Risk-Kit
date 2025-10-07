# Ensure you’re on the right branch
git branch --show-current
# Switch if needed
git switch main

# Sync from remote (safe fast-forward only)
git fetch origin
git pull --ff-only origin main

# Review changes
git status
git diff

# Stage and commit
git add -A
git commit -m "feat: describe your change"

# Tag this release (Git Bash example)
VERSION=0.1.3
git tag -a v$VERSION -m "Release v$VERSION"

# Push branch and tag
git push -u origin main
git push origin v$VERSION

# Create a branch for a new feature from an existing branch
git checkout -b feature/my-feature
git branch -m <old-branch-name> <new-branch-name>

# Push branch
git push -u origin feature/my-feature
