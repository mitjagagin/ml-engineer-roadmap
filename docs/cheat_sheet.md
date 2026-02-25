# Мастер-шпаргалка ML Engineer (Python)

> Для: Дмитрия | Путь: Junior / Intern ML Engineer  
> Формат: микро-сессии 10-20 минут -> видимый результат -> коммит  
> Последнее обновление: [дата]

---
## 🎯 Главная цель

Выйти на уровень Junior / Intern ML Engineer (Python):
- Уметь обучать модели (регрессия, классификация)
- Уметь сервить модели через REST API (FastAPI)
- Знать базовые инженерные практики (Git, тесты, Docker)
- Иметь портфолио из 4+ проектов на GitHub

---
## 🔁 Паттерн 1: Обучение и сохранение модели

### 1. Подготовка данных

~~~python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
~~~

### 2. Обучение

~~~python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
~~~

### 3. Оценка

~~~python
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
~~~

### 4. Сохранение

~~~python
import joblib, os
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/iris_logreg.pkl")
~~~

---
## 🧹 Паттерн 2: Очистка данных (Titanic-style)

### Заполнить пропуски в числе (медиана)

~~~python
df['age'] = df['age'].fillna(df['age'].median())
~~~

### Заполнить пропуски в категории (мода)

~~~python
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
~~~

### Удалить колонку с >70% пропусков

~~~python
df = df.drop(columns=['deck'])
~~~

### Закодировать категории (One-Hot Encoding)

~~~python
df = pd.get_dummies(df, columns=['sex', 'embarked'])
~~~

---
## 🧪 Паттерн 3: Тест для FastAPI

Файл: `tests/test_api.py`

~~~python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
~~~

### Запуск тестов

~~~bash
pytest tests/test_api.py -v
~~~

---
## 🛠 Паттерн 4: CLI аргументы (argparse)

### В начале скрипта `scripts/train.py`

~~~python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--model-path", type=str, default="models/iris_logreg.pkl")
parser.add_argument("--test-size", type=float, default=0.2)
parser.add_argument("--random-state", type=int, default=42)
args = parser.parse_args()
~~~

### Использование

~~~python
model_path = args.model_path
test_size = args.test_size
~~~

### Запуск

~~~bash
python scripts/train.py
~~~

~~~bash
python scripts/train.py --model-path models/titanic_logreg.pkl --test-size 0.3
~~~

---
## 🔀 Git: базовые команды

| Команда | Описание |
|---------|----------|
| `git status` | Посмотреть статус |
| `git diff имя_файла` | Посмотреть изменения в файле |
| `git add путь/к/файлу` | Добавить файл |
| `git commit -m "сообщение"` | Закоммитить |
| `git push` | Отправить на GitHub |

### Типы коммитов

| Тип | Описание |
|-----|----------|
| `feat` | Новая фича |
| `fix` | Исправление бага |
| `docs` | Обновление документации |
| `test` | Добавление тестов |
| `chore` | Рутинные изменения |

---
## ✅ Чек-лист: Я это могу

- [ ] Могу загрузить датасет из sklearn/seaborn
- [ ] Могу найти и обработать пропуски (медиана/мода/drop)
- [ ] Могу закодировать текстовые колонки через `get_dummies`
- [ ] Могу разделить данные на train/test со `stratify`
- [ ] Могу обучить `LogisticRegression` и `RandomForest`
- [ ] Могу посчитать accuracy и вывести confusion matrix
- [ ] Могу сохранить модель через `joblib.dump`
- [ ] Могу написать простой тест для FastAPI эндпоинта
- [ ] Могу добавить CLI аргументы через `argparse`
- [ ] Могу закоммитить изменения и отправить на GitHub

---
## ⚡ Полезные команды (PowerShell)

~~~bash
conda activate ml
python --version
pip list | findstr sklearn
jupyter notebook notebooks/02_titanic_eda.ipynb
uvicorn app.main:app --reload
pytest tests/test_api.py -v
~~~

---

> Принцип работы: микро-сессии 10-20 минут -> видимый результат -> коммит -> документирование  
> Репозиторий: https://github.com/mitjagagin/ml-engineer-roadmap