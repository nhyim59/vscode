import pandas as pd
from .data_loader import load_config


def analyze_by_product(df):
    config = load_config()
    columns = config['columns']

    product_analysis = df.groupby(columns['product']).agg({
        columns['quantity']: 'sum',
        columns['total']: 'sum'
    }).reset_index()
    product_analysis.columns = ['제품', '총 수량', '총 매출']
    return product_analysis


def analyze_by_seller(df):
    config = load_config()
    columns = config['columns']

    seller_analysis = df.groupby(columns['seller']).agg({
        columns['quantity']: 'sum',
        columns['total']: 'sum'
    }).reset_index()
    seller_analysis.columns = ['판매처', '총 수량', '총 매출']
    return seller_analysis


def get_kpi_summary(df):
    config = load_config()
    columns = config['columns']

    total_sales = df[columns['total']].sum()
    total_quantity = df[columns['quantity']].sum()
    avg_price = df[columns['price']].mean()

    return {
        '총 매출': total_sales,
        '총 수량': total_quantity,
        '평균 가격': avg_price
    }
