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