# 🐍 Python Learning – Quickstart Cheat Sheet

**Targets:** macOS (VS Codium) + iPad (Working Copy + Pythonista)  
**Repo:** `python-learning`

---

## 1) Start of Session (Laptop/Desktop)

```bash
cd ~/Projects/python-learning
git pull origin main
source .venv/bin/activate  # if missing: python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # only if requirements.txt changed
```
In VS Codium:
- Command Palette → **Python: Select Interpreter** → `.venv/bin/python`
- Format-on-save (Black) + Ruff linting enabled via `.vscode/settings.json`

---

## 2) While You Work

Run a script:
```bash
python path/to/file.py
```

Run tests:
```bash
pytest -q
```

Add a package and pin versions:
```bash
pip install <package>
pip freeze > requirements.txt
```

---

## 3) End of Session (Sync with GitHub)

```bash
git add -A
git commit -m "Describe what you changed"
git push origin main
```

Next machine:
```bash
cd ~/Projects/python-learning
git pull origin main
source .venv/bin/activate
pip install -r requirements.txt  # only if changed
```

---

## 4) iPad Workflow (Working Copy + Pythonista)

1. **Working Copy** → open `python-learning` → **Pull**
2. **Pythonista** → External Files → open repo → edit/run (▶️)
3. **Working Copy** → **Commit** → **Push**
4. Back on Mac: `git pull`

*Tip:* Use Pythonista’s console handle to split editor/console.

---

## 5) GitHub Actions (CI)

- Location: `.github/workflows/ci.yml`
- Runs on every **push/PR**: `black --check`, `ruff`, `mypy`, `pytest` on Python 3.11–3.13
- Add a basic test to pass CI:
```bash
mkdir -p tests
printf "def test_smoke() -> None:\n    assert True\n" > tests/test_smoke.py
```

---

## 6) Common Fixes

Unfinished merge:
```bash
git status
# resolve conflicts, then:
git add <files>
git merge --continue  # or: git commit
```

Abort merge and rebase:
```bash
git merge --abort
git pull --rebase origin main
```

Discard all local changes (destructive):
```bash
git fetch origin
git reset --hard origin/main
```

Exit venv:
```bash
deactivate
```

---

## 7) Nice-to-have

Aliases (add to `~/.zshrc`):
```bash
alias python="python3"
alias pip="pip3"
```

Auto-activate venv (via `direnv`):
```bash
brew install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc && source ~/.zshrc
echo 'source .venv/bin/activate' > .envrc && direnv allow
```

---

**You’re ready to code.** Start each day with `git pull` → activate venv → code → tests → commit & push.
