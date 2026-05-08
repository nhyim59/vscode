import os
import streamlit as st
from src.data_loader import load_sales_data, get_raw_data_path
from src.preprocessing import preprocess_data
from src.utils import to_excel


def app():
    st.header("📥 월별 다운로드")

    file_path = os.path.join(get_raw_data_path(), "판매데이터_4월.xlsx")
    if not os.path.exists(file_path):
        st.error("판매 데이터 파일이 존재하지 않습니다.")
        return

    df = load_sales_data(file_path)
    if df is None:
        st.error("데이터를 로드할 수 없습니다.")
        return

    df = preprocess_data(df)
    if 'month_label' not in df.columns and '날짜' in df.columns:
        df['month_label'] = df['날짜'].dt.strftime('%Y-%m')

    selected_month = st.selectbox(
        "다운로드할 월 선택",
        sorted(df['month_label'].unique())
    )

    selected_df = df[df['month_label'] == selected_month]
    st.write(f"{selected_month} 판매 데이터 ({len(selected_df)}건)")
    st.dataframe(selected_df, use_container_width=True, height=340)

    excel_data = to_excel(selected_df)
    st.markdown("<div class='download-button-container'>", unsafe_allow_html=True)
    st.download_button(
        label=f"{selected_month}_판매데이터.xlsx 다운로드",
        data=excel_data,
        file_name=f"{selected_month}_판매데이터.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    st.markdown("</div>", unsafe_allow_html=True)
