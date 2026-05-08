from pathlib import Path
import pandas as pd
import yaml


def get_root_path() -> Path:
    return Path(__file__).resolve().parents[1]


def load_config():
    config_path = get_root_path() / 'config' / 'config.yaml'
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_sales_data(file_path):
    """엑셀 파일에서 판매 데이터를 로드합니다."""
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"데이터 로드 오류: {e}")
        return None


def get_raw_data_path() -> str:
    config = load_config()
    return str(get_root_path() / config['data_paths']['raw'])


def get_processed_data_path() -> str:
    config = load_config()
    return str(get_root_path() / config['data_paths']['processed'])


def get_monthly_data_path() -> str:
    config = load_config()
    return str(get_root_path() / config['data_paths']['monthly'])
