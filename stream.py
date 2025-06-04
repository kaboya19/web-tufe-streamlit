import streamlit as st

st.set_page_config(page_title="Yeni Adres", layout="centered")

# Google Fonts üzerinden Roboto veya benzeri bir font kullanalım
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        text-align: center;
        padding-top: 100px;
        background-color: #f9f9f9;
        color: #333333;
    }

    .redirect-box {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
        display: inline-block;
    }

    .redirect-box h1 {
        font-size: 32px;
        margin-bottom: 10px;
    }

    .redirect-box a {
        font-size: 20px;
        color: #0072ff;
        text-decoration: none;
        font-weight: 600;
    }

    .redirect-box a:hover {
        text-decoration: underline;
    }
    </style>

    <div class="redirect-box">
        <h1>Web TÜFE taşındı!</h1>
        <p>Yeni sitemizi ziyaret edin:</p>
        <a href="https://www.webtufe.com" target="_blank">www.webtufe.com</a>
    </div>
""", unsafe_allow_html=True)
