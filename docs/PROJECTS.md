# Projects (portfolio)

## 1) Python basics notebook
**Goal:** закрепить базовые конструкции Python для ML/engineering задач.  
**What:** list/dict/loops, простые упражнения, проверка окружения `ml`.  
**Stack:** Python, Jupyter, conda, Git/GitHub  
**Links:**
- GitHub notebook: https://github.com/mitjagagin/ml-engineer-roadmap/tree/main/notebooks/00_python_basics.ipynb
- Kaggle notebook: https://www.kaggle.com/code/mitjagagin/python-basics-portfolio

## 2) Iris model serving API (FastAPI)
**Goal:** “train → save artifact → serve predictions via REST API”.  
**What:**
- `scripts/train.py` обучает модель (sklearn) и сохраняет `models/iris_logreg.pkl`
- `app/main.py` поднимает API: `GET /health`, `POST /predict` (class_id, class_name, proba)
- `scripts/test_api.ps1` — автопроверка API (health + predict)
**Stack:** Python, scikit-learn, joblib, FastAPI, uvicorn, PowerShell, Git/GitHub  
**Link:** https://github.com/mitjagagin/ml-engineer-roadmap

## 3) California Housing — tabular ML baseline + error analysis
**Goal:** построить baseline на табличных данных и понять характер ошибок модели.  
**What:**
- Baseline: Ridge + StandardScaler (Pipeline)
- Improved: HistGradientBoostingRegressor
- Metrics on test split (random_state=42):  
  - Ridge: RMSE≈0.746, MAE≈0.533, R2≈0.576  
  - HGB: RMSE≈0.464, MAE≈0.310, R2≈0.836
- Error analysis: actual vs predicted, error distribution, bias by target bins (over/underestimation)
**Stack:** Python, pandas, scikit-learn, matplotlib  
**Link:** https://github.com/mitjagagin/ml-engineer-roadmap/blob/main/notebooks/01_california_housing_baseline.ipynb