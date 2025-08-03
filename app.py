import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# サンプルデータの作成
df = pd.DataFrame({
    'x': range(1, 101),
    'y': np.random.randn(100).cumsum()
})

# Altairでグラフを作成
chart = alt.Chart(df).mark_line().encode(
    x='x',
    y='y'
).properties(
    title='Random Walk'
)

# Streamlitで表示
st.title("Altairを使ったグラフ表示")
st.altair_chart(chart, use_container_width=True)