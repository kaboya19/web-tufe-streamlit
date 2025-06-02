import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Örnek veri
data = {
    "Grup": [
        "Lokanta ve oteller", "Konut", "Ulaştırma", "TÜFE", "Ev eşyası",
        "Eğlence ve kültür", "Çeşitli mal ve hizmetler", "Gıda ve alkolsüz içecekler",
        "Eğitim", "Alkollü içecekler ve tütün", "Sağlık", "Haberleşme", "Giyim ve ayakkabı"
    ],
    "Değişim": [4.67, 2.63, 2.34, 1.78, 1.59, 1.59, 1.39, 1.17, 0.01, 0, 0, -0.15, -0.12]
}
df = pd.DataFrame(data)

# Mobilde ve masaüstünde responsive yükseklik
bar_height = 40
chart_height = max(len(df) * bar_height, 350)

# Renkleri ayarla
colors = ['red' if g == 'TÜFE' else ('green' if v >= 0 else 'blue') for g, v in zip(df['Grup'], df['Değişim'])]

fig = go.Figure(go.Bar(
    y=df['Grup'],
    x=df['Değişim'],
    orientation='h',
    marker=dict(color=colors),
    text=[f"%{v:.2f}" for v in df['Değişim']],
    textposition='auto',
))

fig.update_layout(
    title="TÜFE ve Alt Kalemler",
    xaxis_title="Değişim (%)",
    yaxis_title="Grup",
    height=chart_height,
    margin=dict(l=100, r=20, t=50, b=40),
    plot_bgcolor='whitesmoke',
    paper_bgcolor='white',
    font=dict(family="Arial Black", size=14, color="black"),
    yaxis=dict(
        automargin=True,
        tickfont=dict(size=14)
    ),
)

# Mobilde yatay scroll için container
st.markdown(
    """
    <style>
    .scroll-container {
        overflow-x: auto;
        width: 100vw;
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)