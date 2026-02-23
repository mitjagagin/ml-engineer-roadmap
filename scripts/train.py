import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import argparse  # Инструмент для работы с командной строкой
import os        # Нужен для создания папок


def main():
    # 1. Создаем парсер
    parser = argparse.ArgumentParser(description="Train Iris Logistic Regression")
    
    # 2. Добавляем настройки, которые можно менять при запуске
    parser.add_argument("--model-path", type=str, default="models/iris_logreg.pkl", help="Куда сохранить модель")
    parser.add_argument("--test-size", type=float, default=0.2, help="Доля данных для теста")
    parser.add_argument("--random-state", type=int, default=42, help="Фиксация случайности для воспроизводимости")
    
    # 3. Считываем команды и сохраняем в переменную args
    args = parser.parse_args()
    X, y = load_iris(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=args.random_state, stratify=y
    )

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"accuracy={acc:.3f}")

    os.makedirs(os.path.dirname(args.model_path), exist_ok=True)
    joblib.dump(model, args.model_path)
    print(f"Model saved to {args.model_path}")


if __name__ == "__main__":
    main()
