# superstore-etl
ETL-пайплайн: CSV > pandas > SQLite > проверки > отчёты

## Стек
Python, pandas, SQLite

## Запуск
1. Скачать датасет и положить в `Data/`
2. Установить зависимости и запустить:
```
pip install -r requirements.txt
python main.py
```

## Датасет
Superstore (Kaggle), https://www.kaggle.com/datasets/roopacalistus/superstore

## Схема данных

![Схема БД](Docs/schema.png)