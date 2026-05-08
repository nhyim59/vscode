import importlib.util
import sys
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
PAGES_DIR = BASE_DIR / "pages"

from src.utils import load_config

PAGE_FILES = {
    "01_대시보드": "01_대시보드.py",
    "02_판매데이터_조회": "02_판매데이터_조회.py",
    "03_월별_다운로드": "03_월별_다운로드.py",
    "04_제품별_분석": "04_제품별_분석.py",
    "05_판매처별_분석": "05_판매처별_분석.py",
}

st.set_page_config(page_title="판매 관리 시스템", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

config = load_config()


def login(username: str, password: str) -> bool:
    return username == "admin" and password == "password"


def show_login():
    st.title("판매 관리 시스템 로그인")
    st.write("앱을 사용하려면 로그인이 필요합니다.")
    st.markdown("---")

    login_success = False
    col1, col2, col3 = st.columns([1, 0.5, 1])
    with col2:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        with st.form("login_form"):
            username = st.text_input("사용자 이름")
            password = st.text_input("비밀번호", type="password")
            submitted = st.form_submit_button("로그인")

            if submitted:
                if login(username, password):
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("아이디 또는 비밀번호가 올바르지 않습니다.")
        st.markdown("</div>", unsafe_allow_html=True)

    return login_success


def load_page_module(file_path: Path):
    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def inject_style():
    style_file = BASE_DIR / "assets" / "style.css"
    if style_file.exists():
        with open(style_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def sidebar_menu():
    logo_file = BASE_DIR / "assets" / "logo.png"
    if logo_file.exists():
        st.sidebar.image(str(logo_file), width=120)
    st.sidebar.title("판매관리시스템")
    st.sidebar.markdown("---")
    page = st.sidebar.radio("페이지 선택", list(PAGE_FILES.keys()))
    st.sidebar.markdown("---")
    st.sidebar.caption("데이터: data/raw/판매데이터_4월.xlsx")
    return page


def render_page(page_name: str):
    page_file = PAGES_DIR / PAGE_FILES[page_name]
    if not page_file.exists():
        st.error(f"페이지 파일을 찾을 수 없습니다: {page_file}")
        return
    page_module = load_page_module(page_file)
    if hasattr(page_module, "app"):
        page_module.app()
    else:
        st.error("페이지에 app() 함수를 정의해주세요.")


def main():
    if not st.session_state.logged_in:
        show_login()
        return

    inject_style()
    selected_page = sidebar_menu()
    if st.sidebar.button("🚪 로그아웃"):
        st.session_state.logged_in = False
        return

    st.title(selected_page)
    render_page(selected_page)


if __name__ == "__main__":
    main()
