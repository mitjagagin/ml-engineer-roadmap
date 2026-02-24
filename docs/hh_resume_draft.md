# Черновик резюме — Junior / Intern ML Engineer (Python)

## Контакты
Город: Нефтекамск  
Готовность к переезду: да  
Формат работы: офис / удалённо / гибрид  

## Ссылки
GitHub: https://github.com/mitjagagin  
Репозиторий портфолио: https://github.com/mitjagagin/ml-engineer-roadmap  
Kaggle: https://www.kaggle.com/mitjagagin  

## Желаемая должность
Junior / Intern ML Engineer (Python)

## Обо мне
Начинающий ML-инженер (Python). Формирую портфолио с упором на инженерные практики: воспроизводимое окружение (conda), разведочный анализ и пайплайны в Jupyter/VS Code, модели на scikit-learn (регрессия, классификация), REST API на FastAPI, автотесты через pytest. Следующий шаг — контейнеризация (Docker) и работа в WSL2/Linux.

Сильная инженерная база: эксплуатация и диагностика оборудования и ПО, работа по инцидентам (ITIL-подход), документирование процессов, взаимодействие с разработчиками и техподдержкой. Умею работать в условиях ограниченного времени (вахтовый формат), ценю микро-шаги и видимый результат.

## Ключевые навыки
- Python (базовый уровень), Pandas, NumPy, Jupyter, VS Code
- Git, GitHub, управление окружениями через conda
- scikit-learn: предобработка данных, train/test split, логистическая регрессия, случайный лес, Ridge, HistGradientBoosting
- FastAPI, uvicorn (базовый уровень), pytest (написание тестов для API)
- Метрики качества: accuracy, RMSE, MAE, R², матрица ошибок (confusion matrix)
- В планах: Docker, WSL2/Linux, SQL, MLflow

## Проекты

### 1) Python: основы и метрики
- Файл: `notebooks/00_python_basics.ipynb`
- Ссылка на Kaggle: https://www.kaggle.com/code/mitjagagin/python-basics-portfolio
- Что сделано: функции, структуры данных, ручная реализация метрик precision/recall/f1
- Навыки: чистый Python, работа с данными, документирование в Markdown

### 2) Iris: сервис предсказаний на FastAPI
- Обучение: `scripts/train.py` (поддержка CLI-аргументов: --model-path, --test-size, --random-state)
- API: `app/main.py` (эндпоинты `GET /health`, `POST /predict` → возвращает class_id, class_name, вероятности)
- Тесты: `tests/test_api.py` (pytest + TestClient), `scripts/test_api.ps1` (PowerShell для быстрой проверки)
- Ссылка: https://github.com/mitjagagin/ml-engineer-roadmap
- Навыки: FastAPI, сервинг моделей, CLI, автотестирование

### 3) California Housing: регрессия стоимости жилья
- Файл: `notebooks/01_california_housing_baseline.ipynb`
- Задача: предсказание медианной стоимости дома (регрессия)
- Модели: Ridge (базовая) vs HistGradientBoostingRegressor (улучшенная)
- Метрики на тесте: RMSE ≈ 0.46, MAE ≈ 0.31, R² ≈ 0.84 (для HGB)
- Анализ: распределение целевой переменной, Actual vs Predicted, анализ ошибок по ценовым диапазонам (bias)
- Навыки: работа с табличными данными, сравнение моделей, визуализация ошибок

### 4) 🆕 Titanic: предсказание выживания пассажиров
- Файл: `notebooks/02_titanic_eda.ipynb`
- Задача: бинарная классификация (выжил / не выжил)
- EDA: загрузка данных (seaborn), анализ пропусков, визуализация распределений (seaborn/matplotlib)
- Предобработка:
  - Заполнение пропусков: Age → медиана, Embarked → мода
  - Удаление колонок с >70% пропусков (Deck)
  - Кодирование категорий: One-Hot Encoding через get_dummies
- Модели: LogisticRegression (~78% accuracy) vs RandomForest (~82% accuracy)
- Метрики: accuracy, матрица ошибок (confusion matrix), важность признаков (feature importances)
- Артефакты: сохранение модели и списка признаков через joblib
- Навыки: полный цикл ML-проекта, работа с пропусками, кодирование, сравнение моделей

## Обучение и развитие
- Самостоятельное изучение: ML Engineering (Python, scikit-learn, FastAPI, pytest, Git)
- Текущий фокус: Docker, WSL2, углубление в feature engineering и деплой моделей
- Формат: микро-сессии 10–20 минут → видимый результат → коммит

## Дополнительная информация
- Готов к обучению и менторству со стороны команды
- Ответственный, системный подход к задачам (опыт работы в вахтовом режиме)
- Умею документировать решения и объяснять технические детали простым языком