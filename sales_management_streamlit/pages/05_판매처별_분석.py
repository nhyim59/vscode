import os
import streamlit as st
from src.data_loader import load_sales_data, get_raw_data_path
from src.preprocessing import preprocess_data
from src.analysis import analyze_by_seller
from src.visualization import create_seller_chart


def app():
    st.header("🏪 판매처별 분석")

    file_path = os.path.join(get_raw_data_path(), "판매데이터_4월.xlsx")
    if not os.path.exists(file_path):
        st.error("판매 데이터 파일이 존재하지 않습니다.")
        return

    df = load_sales_data(file_path)
    if df is None:
        st.error("데이터를 로드할 수 없습니다.")
        return

    df = preprocess_data(df)
    seller_analysis = analyze_by_seller(df)

    st.subheader("판매처별 매출 및 수량")
    st.dataframe(seller_analysis, use_container_width=True)
    st.plotly_chart(create_seller_chart(seller_analysis), use_container_width=True)

    selected_seller = st.selectbox("판매처 선택", seller_analysis['판매처'].unique())
    if selected_seller:
        selected_df = df[df['판매처'] == selected_seller]
        st.markdown("---")
        st.subheader(f"{selected_seller} 판매 내역")
        st.dataframe(selected_df, use_container_width=True)
