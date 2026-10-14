import pandas as pd


def extract_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f'Файл не найден по пути: {path}')
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError('Файл пустой')