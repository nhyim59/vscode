import os
import pandas as pd
import streamlit as st
from src.data_loader import load_sales_data, get_raw_data_path
from src.preprocessing import preprocess_data
from src.utils import filter_data, to_excel


def app():
    st.header("🔍 판매 데이터 조회")

    file_path = os.path.join(get_raw_data_path(), "판매데이터_4월.xlsx")
    if not os.path.exists(file_path):
        st.error("판매 데이터 파일이 존재하지 않습니다.")
        return

    df = load_sales_data(file_path)
    if df is None:
        st.error("데이터를 로드할 수 없습니다.")
        return

    df = preprocess_data(df)

    st.sidebar.subheader("필터 옵션")
    product_search = st.sidebar.text_input("제품 검색")
    seller_search = st.sidebar.text_input("판매처 검색")
    date_col = '날짜'

    if date_col in df.columns:
        start_date, end_date = st.sidebar.date_input(
            "기간 선택",
            [df[date_col].min(), df[date_col].max()]
        )
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        df = df[(df[date_col] >= start_date) & (df[date_col] <= end_date)]

    filters = {
        '제품': product_search,
        '판매처': seller_search
    }
    filtered_df = filter_data(df, filters)

    st.write(f"총 {len(filtered_df)}건의 결과")
    st.dataframe(filtered_df, use_container_width=True)

    if len(filtered_df) > 0:
        excel_data = to_excel(filtered_df)
        st.download_button(
            label="필터링된 데이터 다운로드 (엑셀)",
            data=excel_data,
            file_name="filtered_sales_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
