import plotly.express as px
import plotly.graph_objects as go


def create_product_chart(df):
    fig = px.bar(df, x='제품', y='총 매출', title='제품별 총 매출', template='plotly_white')
    fig.update_layout(xaxis_title='제품', yaxis_title='총 매출')
    return fig


def create_seller_chart(df):
    fig = px.bar(df, x='판매처', y='총 매출', title='판매처별 총 매출', template='plotly_white')
    fig.update_layout(xaxis_title='판매처', yaxis_title='총 매출')
    return fig


def create_kpi_gauge(value, title, max_value):
    fig = go.Figure(go.Indicator(
        mode='gauge+number',
        value=value,
        title={'text': title},
        gauge={'axis': {'range': [None, max_value]}}
    ))
    return fig
