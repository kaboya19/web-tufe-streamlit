import pandas as pd
import plotly.express as px

# CSV verisini oku
url = "https://raw.githubusercontent.com/kaboya19/web-tufe-streamlit/main/t%C3%BCfe.csv"
df = pd.read_csv(url)
df.columns = [col.strip() for col in df.columns]
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], dayfirst=True)

# Plotly grafik oluştur
fig = px.line(df, x=df.columns[0], y=df.columns[1], title="TÜFE Zaman Serisi")

# HTML olarak kaydet
fig.write_html("tufe_plot.html")
