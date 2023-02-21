import yfinance as yf
import datetime
import plotly.graph_objects as go
import streamlit as st

st.write("# 주식 데이터 시각화")

ticker = st.text_input("티커 입력 >> ")
data = yf.Ticker(ticker)
today = datetime.datetime.today().strftime("%Y-%m-%d")
df = data.history(period="1d", start="2015-01-01", end=today)
st.write(df)

candle = go.Candlestick(x=df.index, open=df["Open"], close=df["Close"], high=df["High"], low=df["Low"])
layout = go.Layout(yaxis={"fixedrange":False})
fig = go.Figure(data=[candle], layout=layout)
st.plotly_chart(fig)

st.write("### 거래량")
st.bar_chart(df["Volume"])
