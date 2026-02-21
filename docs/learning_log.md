# Learning log — ML Engineer path

## Goal
Become Junior / Intern ML Engineer (Python): training models + serving + Docker basics.

## Repo
https://github.com/mitjagagin/ml-engineer-roadmap

## Current setup (Windows)
- Miniconda installed
- conda env: `ml` (Python 3.11)
- VS Code kernel: "Python (ml)"

## Done (confirmed)
- Project structure: notebooks/, scripts/, docs/, data/, .gitignore
- Notebook: `notebooks/00_python_basics.ipynb`
- Environment reproducibility: `environment.yml` + README setup
- Mini-project #1 (Train -> Serve):
  - `scripts/train.py` trains Iris LogisticRegression and saves `models/iris_logreg.pkl`
  - `app/main.py` FastAPI service:
    - GET /health -> {"status":"ok"}
    - POST /predict -> returns class_id, class_name, proba
  - API tested via PowerShell:
    - `Invoke-RestMethod` calls
    - script `scripts/test_api.ps1` (prints "All checks passed")

## How to run (quick)
Train:
```powershell
conda activate ml
python scripts/train.py