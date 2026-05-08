from pathlib import Path
import importlib.util

BASE_DIR = Path(__file__).resolve().parent
SALES_APP_PATH = BASE_DIR / "sales_management_streamlit" / "app.py"


def load_sales_management_app():
    spec = importlib.util.spec_from_file_location("sales_management_streamlit_app", SALES_APP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    sales_app = load_sales_management_app()
    if hasattr(sales_app, "main"):
        sales_app.main()
    else:
        raise RuntimeError("sales_management_streamlit/app.py에 main() 함수가 없습니다.")


if __name__ == "__main__":
    main()
