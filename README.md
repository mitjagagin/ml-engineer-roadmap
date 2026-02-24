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

### 🚀 Training script CLI usage

Script `scripts/train.py` supports command-line arguments for flexible runs:

```powershell
# Run with defaults (model saved to models/iris_logreg.pkl)
python scripts/train.py

# Custom parameters: output path, test split, reproducibility seed
python scripts/train.py --model-path models/my_model.pkl --test-size 0.3 --random-state 123

# Show all available options
python scripts/train.py --help

**Arguments:**
- `--model-path` (default: `models/iris_logreg.pkl`) — Path to save the trained model (.pkl)
- `--test-size` (default: `0.2`) — Fraction of data for testing (0.0–1.0)
- `--random-state` (default: `42`) — Seed for reproducible train/test split

## Setup (Windows + Miniconda)

### 1) Create environment
> Creates conda env `ml` using `environment.yml`.

```powershell
conda env create -f environment.yml
conda activate ml