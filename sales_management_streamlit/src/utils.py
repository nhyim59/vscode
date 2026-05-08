import pandas as pd
from io import BytesIO


def to_excel(df: pd.DataFrame) -> BytesIO:
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='판매데이터')
    output.seek(0)
    return output


def filter_data(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    filtered_df = df.copy()
    for column, value in filters.items():
        if value and column in filtered_df.columns:
            filtered_df = filtered_df[filtered_df[column].astype(str).str.contains(value, case=False, na=False)]
    return filtered_df


def load_config():
    from .data_loader import load_config as _load_config
    return _load_config()
