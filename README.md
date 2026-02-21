# ML Engineer Roadmap (from zero)

## Goal
Become a Junior / Intern ML Engineer (Python): train models + build API + Docker basics.

## Links
- GitHub profile: https://github.com/mitjagagin
- Kaggle: https://www.kaggle.com/mitjagagin
- Kaggle notebook (Python basics portfolio): https://www.kaggle.com/code/mitjagagin/python-basics-portfolio

## What is inside (portfolio)
### 1) Python basics notebook
- File: `notebooks/00_python_basics.ipynb`

### 2) Model training + Model serving API (FastAPI)
- Train script: `scripts/train.py` (saves model artifact to `models/iris_logreg.pkl`)
- API service: `app/main.py`
  - `GET /health`
  - `POST /predict` (returns `class_id`, `class_name`, `proba`)
- API test script (PowerShell): `scripts/test_api.ps1`

---

## Setup (Windows + Miniconda)

### 1) Create environment
> Creates conda env `ml` using `environment.yml`.

```powershell
conda env create -f environment.yml
conda activate ml