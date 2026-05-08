import pandas as pd
from .data_loader import load_config


def preprocess_data(df):
    """판매 데이터를 전처리합니다."""
    config = load_config()
    columns = config['columns']

    if columns['date'] in df.columns:
        df[columns['date']] = pd.to_datetime(df[columns['date']], errors='coerce')

    numeric_cols = [columns['quantity'], columns['price'], columns['total']]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna()

    if columns['date'] in df.columns:
        df['year_month'] = df[columns['date']].dt.to_period('M').astype(str)
        df['month_label'] = df[columns['date']].dt.strftime('%Y-%m')

    return df


def save_processed_data(df, file_path):
    """전처리된 데이터를 저장합니다."""
    df.to_excel(file_path, index=False)
