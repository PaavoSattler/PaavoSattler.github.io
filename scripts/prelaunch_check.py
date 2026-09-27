from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".qmd", ".md", ".yml", ".yaml", ".html", ".scss", ".css", ".bib", ".txt"}
EXCLUDE_PARTS = {"_site", ".git", ".quarto", "setup"}
EXCLUDE_FILES = {"TODO-before-launch.md", "README.md", "images/README.md"}

checks = {
    "old GitHub username": "PSattlerStat",
    "old private email domain": "@yahoo.de",
    "GoatCounter placeholder": "YOURCODE",
    "Search Console placeholder": "YOUR_VERIFICATION_CODE",
    "profile image placeholder": "profile-placeholder.svg",
}

hits = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
        continue
    if any(part in EXCLUDE_PARTS for part in path.parts) or str(path.relative_to(ROOT)).replace("\\", "/") in EXCLUDE_FILES:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for label, needle in checks.items():
        if needle in text:
            hits.append((label, path.relative_to(ROOT), needle))

if hits:
    print("Pre-launch checks found items to review:\n")
    for label, path, needle in hits:
        print(f"- {label}: {path} ({needle})")
    raise SystemExit(1)
else:
    print("Pre-launch text checks passed.")
