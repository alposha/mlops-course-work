# mlops курсовая

Проект классифицирует русскоязычные отзывы на три класса: Положительный, Нейтральный, Отрицательный.  
Реализован полный ML-пайплайн с обучением моделей, инференс-сервисом на FastAPI и Streamlit UI.

---

## Pipeline

```mermaid
graph TB
    A[Исходные данные] --> B[Очищенные данные]
    B --> C[Обучение fasttext модели]
    C --> D[Векторизация]

    D --> E[Random Forest]
    D --> F[CatBoost]
    D --> G[Logistic Regression]

    E --> H[Логгирование экспериментов в MLflow]
    F --> H
    G --> H

    H --> I[Выбор оптимальной модели]
    I --> J[Контейнеризация]
    J --> K[FastApi сервис]

    M[Конфигурация OmegaConf] --> E
    M --> F
    M --> G
    M --> K

    subgraph "Эксперименты"
        E
        F
        G
    end
```

## Быстрый старт

### 1.Клонирование и настройка окружения

##### Клонировать репозиторий

```bash
git clone <repository-url>
cd mlops-coursework
```

##### Создать виртуальное окружение

```bash
python -m venv venv
```

##### Активировать (Linux/macOS)

```bash
source venv/bin/activate
```

##### Активировать (Windows)

```bash
venv\Scripts\activate
```

##### Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Эксперименты

##### Запуск экспериментов

```bash
python src/experiments.py

```

### MLflow UI

##### Отслеживания экспериментов

```bash
mlflow ui --port 5000
```

Открыть: http://127.0.0.1:5000/

### Локальный запуск FastAPI сервиса

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

Эндпоинты:

- /health — проверка состояния сервиса
- /predict — предсказание сентимента

### Streamlit UI

#### Команда для запуска streamlit

```bash
streamlit run ui/streamlit_ui.py
```

### Контейнеризация

##### Сборка образа

```bash
docker build -t nlp-sentiment-inference .
```

##### Запуск контейнера

```bash
docker run -p 8000:8000 nlp-sentiment-inference
```
