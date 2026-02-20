# Learning log — ML Engineer path

## Goal

Become Junior ML Engineer (Python): train models + build API + Docker basics.

## Current setup (Windows)

- Miniconda installed
- conda env: `ml` (Python 3.11)
- VS Code works with kernel: **Python (ml)**
- `sys.executable` in notebook:
  `C:\Users\gagindv\AppData\Local\miniconda3\envs\ml\python.exe`

## Repo
<https://github.com/mitjagagin/ml-engineer-roadmap>

## Done

- GitHub repo initialized, README created
- Project structure added: `notebooks/`, `scripts/`, `docs/`, `data/`, `.gitignore`
- Notebook: `notebooks/00_python_basics.ipynb`
- `environment.yml` added + README setup instructions
- Jupyter kernels:
  - `python3`
  - `ml` (registered via ipykernel)

## Next steps (Mini-project #1)

**Train → Save → Serve**

1) Install packages (in env `ml`):
   - `python -m pip install fastapi uvicorn joblib ipykernel`
2) Add files:
   - `scripts/train.py` (train Iris model, save `models/iris_logreg.pkl`)
   - `app/main.py` (FastAPI `/health` + `/predict`)
3) Run:
   - `python scripts/train.py`
   - `uvicorn app.main:app --reload`
4) Check:
   - <http://127.0.0.1:8000/health>
   - <http://127.0.0.1:8000/docs>

## Notes / issues

- If VS Code does not show kernel, ensure Jupyter extension is installed and run:
  - `python -m pip install ipykernel`
  - `python -m ipykernel install --user --name ml --display-name "Python (ml)"`

“Mini-project #1: FastAPI /health и /predict работает, возвращает class_name.”
“Тестировал через Invoke-RestMethod на порту 8001.”
