import os
import streamlit as st
from src.data_loader import load_sales_data, get_raw_data_path
from src.preprocessing import preprocess_data
from src.analysis import get_kpi_summary, analyze_by_product, analyze_by_seller
from src.visualization import create_product_chart, create_seller_chart


def app():
    st.header("📊 대시보드")

    file_path = os.path.join(get_raw_data_path(), "판매데이터_4월.xlsx")
    if not os.path.exists(file_path):
        st.error("판매 데이터 파일이 존재하지 않습니다.")
        return

    df = load_sales_data(file_path)
    if df is None:
        st.error("데이터를 로드할 수 없습니다.")
        return

    df = preprocess_data(df)
    kpis = get_kpi_summary(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("총 매출", f"₩{kpis['총 매출']:,.0f}")
    col2.metric("총 수량", f"{kpis['총 수량']:,}")
    col3.metric("평균 가격", f"₩{kpis['평균 가격']:,.0f}")

    st.markdown("---")
    st.subheader("매출 시각화")

    product_analysis = analyze_by_product(df)
    seller_analysis = analyze_by_seller(df)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_product_chart(product_analysis), use_container_width=True)
    with col2:
        st.plotly_chart(create_seller_chart(seller_analysis), use_container_width=True)

    st.markdown("---")
    st.subheader("판매 데이터 미리보기")
    st.dataframe(df.head(20), use_container_width=True)
