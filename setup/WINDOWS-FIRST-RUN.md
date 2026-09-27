# First run on the Windows PC

Do this only when you are back at the Windows computer.

## 1. Check prerequisites

Open PowerShell and run:

```powershell
git --version
quarto --version
```

If one is missing, install it before continuing.

## 2. Clone the private repository

```powershell
git clone https://github.com/PaavoSattler/PaavoSattler.github.io.git
cd PaavoSattler.github.io
```

## 3. Copy this prepared starter into the cloned repository

Copy all project files into the cloned `PaavoSattler.github.io` directory.
Do **not** copy a nested folder containing the project; `_quarto.yml` must be at the repository root.

## 4. Preview locally

```powershell
quarto preview
```

A browser window should open with the site. Keep the terminal open while previewing.

## 5. Full render

```powershell
quarto render
```

The generated site should appear in `_site/`.

## 6. Run the local pre-launch checker

```powershell
python scripts/prelaunch_check.py
```

Python is optional for rendering the site; this helper only checks for common placeholders/old links.

## 7. Commit only after the local preview looks right

```powershell
git add .
git status
git commit -m "Add initial academic website"
git push
```

The repository can remain private throughout development.
