import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import os
from io import BytesIO
from datetime import datetime
from st_social_media_links import SocialMediaIcons
import base64
from streamlit_option_menu import option_menu
import streamlit as st

# HTML etiketini başlık kısmında çalıştırmaya zorlamak


st.set_page_config(page_title="Web-Tüketici Fiyat Endeksi",layout="wide")
social_media_links = {
    "GitHub": {"url": "https://github.com/kaboya19", "color": "#000000"},
    "LinkedIn": {"url": "https://www.linkedin.com/in/bora-kaya/", "color": "#000000"}
}
tabs=["Tüketici Fiyat Endeksi","Ana Gruplar","Harcama Grupları","Madde Endeksleri","Özel Kapsamlı Göstergeler","Bültenler","Metodoloji Notu"]
tabs = option_menu(
    menu_title=None,
    options=["Tüketici Fiyat Endeksi","Ana Gruplar","Harcama Grupları","Madde Endeksleri","Özel Kapsamlı Göstergeler","Bültenler" ,"Metodoloji Notu"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#d6094d"},
        "icon": {"color": "orange", "font-size": "18px"},
        "nav-link": {
            "font-size": "20px", 
            "text-align": "center", 
            "margin": "0px", 
            "--hover-color": "#444", 
            "padding-left": "20px",  # Add padding for consistent spacing
            "padding-right": "20px",  # Add padding for consistent spacing
            "height": "85px",  # Set a fixed height for all buttons
            "min-width": "150px",  # Ensure buttons do not shrink too small
            "white-space": "normal",  # Allow text to wrap if necessary
            "display": "inline-flex",  # Use inline-flex to adjust width to text content
            "justify-content": "center",
            "align-items": "center",
        },
        "nav-link-selected": {"background-color": "orange"},
    }
)


import time
page=st.sidebar.radio("Sekmeler",tabs)

social_media_icons = SocialMediaIcons(
        [link["url"] for link in social_media_links.values()],
        colors=[link["color"] for link in social_media_links.values()]
    )
social_media_icons.render(sidebar=True)
import streamlit as st
import pandas as pd

# Örnek veri
import streamlit as st
import pandas as pd
from streamlit_marquee import streamlit_marquee

import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

import time
import streamlit as st
import pandas as pd
from datetime import timedelta











from datetime import datetime,timedelta
import pytz
tüfe=pd.read_csv("tüfe.csv",index_col=0)
tüfe.index=pd.to_datetime(tüfe.index)

gruplar=pd.read_csv("gruplar_int.csv",index_col=0)
gruplar.index=pd.to_datetime(gruplar.index)
gfe1=tüfe.copy()
gfe1["Date"]=pd.to_datetime(gfe1.index)
gfe1["Ay"]=gfe1["Date"].dt.month
gfe1["Yıl"]=gfe1["Date"].dt.year    
month = gfe1["Ay"].iloc[-1]
year=gfe1["Yıl"].iloc[-1] 
oncekiyear=gfe1["Yıl"].iloc[-1] 
tarihim=pd.to_datetime(gfe1.index[-1]).day
if tarihim>24:
    tarihim=24
if tarihim<10:
    tarihim="0"+str(tarihim)

from datetime import datetime,timedelta
tarih=datetime.now().strftime("%Y-%m")
onceki=(datetime.now()-timedelta(days=30)).strftime("%Y-%m")




if page=="Bültenler":
    import streamlit as st
    from PIL import Image

    import streamlit as st
    import base64

    # PDF dosyasını yükle
    



    # Tab for selecting the bulletin
    tab = st.selectbox("Bülten Seçin", ["Nisan 2025","Mart 2025","Şubat 2025"])
    import requests

    if tab == "Nisan 2025":
        pdf_url = "https://raw.githubusercontent.com/kaboya19/web-tufe-streamlit/main/webtüfenisan25.pdf"
        response = requests.get(pdf_url)
        if response.status_code == 200:
            st.download_button(
                label="📥 PDF'yi İndir",
                data=response.content,
                file_name="WebTÜFE_Nisan25.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("PDF indirilemedi. Lütfen bağlantıyı kontrol edin.")
        viewer_url = f"https://mozilla.github.io/pdf.js/web/viewer.html?file={pdf_url}"

        st.markdown(
            f'<iframe src="{viewer_url}" width="90%" height="800px" style="border:none;"></iframe>',
            unsafe_allow_html=True
        )
                

        st.markdown("<p><strong>Hazırlayan: Bora Kaya</strong></p>", unsafe_allow_html=True)
        st.markdown("<p>Web-TÜFE Twitter: <a href='https://x.com/webtufe'>https://x.com/webtufe</a></p>", unsafe_allow_html=True)
        st.markdown("<p>Linkedin: <a href='https://www.linkedin.com/in/bora-kaya/'>https://www.linkedin.com/in/bora-kaya/</a></p>", unsafe_allow_html=True)
    # Check if the user selects February 2025
    if tab == "Mart 2025":
        pdf_url = "https://raw.githubusercontent.com/kaboya19/web-tufe-streamlit/main/webt%C3%BCfemart25.pdf"
        response = requests.get(pdf_url)
        if response.status_code == 200:
            st.download_button(
                label="📥 PDF'yi İndir",
                data=response.content,
                file_name="WebTÜFE_Mart25.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("PDF indirilemedi. Lütfen bağlantıyı kontrol edin.")
        viewer_url = f"https://mozilla.github.io/pdf.js/web/viewer.html?file={pdf_url}"

        st.markdown(
            f'<iframe src="{viewer_url}" width="90%" height="800px" style="border:none;"></iframe>',
            unsafe_allow_html=True
        )
                

        st.markdown("<p><strong>Hazırlayan: Bora Kaya</strong></p>", unsafe_allow_html=True)
        st.markdown("<p>Web-TÜFE Twitter: <a href='https://x.com/webtufe'>https://x.com/webtufe</a></p>", unsafe_allow_html=True)
        st.markdown("<p>Linkedin: <a href='https://www.linkedin.com/in/bora-kaya/'>https://www.linkedin.com/in/bora-kaya/</a></p>", unsafe_allow_html=True)
    if tab == "Şubat 2025":

# PDF dosyasını oku
        
        # Title
        st.markdown("<h2 style='color:black; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Şubat 2025 Bülteni</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:red; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Şubatta %3,83 arttı</h3>", unsafe_allow_html=True)

        # First image
        image1 = Image.open("anagruplar_şubat.png")
        st.image(image1, caption="En çok artış ve düşüş yaşanan maddeler")

        # Paragraphs and next images
        st.write("Web-Tüketici Fiyat Endeksi Şubatta %3,83 artış kaydederken mevsimsellikten arındırılmış artış %3,38 oldu.")
        st.write("En çok artış ve düşüş yaşanan maddeler:")
        image2 = Image.open("maddeler_şubat.png")
        st.image(image2, caption="En çok artış ve düşüş yaşanan temel başlıklar")

        st.write("En çok artış ve düşüş yaşanan temel başlıklar:")
        image3 = Image.open("temelbaşlıklar_şubat.png")


        st.write("Özel Kapsamlı Göstergeler aylık artış oranları:")
        image5 = Image.open("özelgöstergelerşubat.png")
        st.image(image5, caption="Ana gruplara ait artış oranları")

        # Display remaining images
        images = [
            ("eveşyasışubat.png", "Ev Eşyası"),
            ("eğitimşubat.png", "Eğitim"),
            ("eğlenceşubat.png", "Eğlence"),
            ("Giyim ve ayakkabışubat.png", "Giyim ve Ayakkabı"),
            ("Gıda ve alkolsüz içeceklerşubat.png", "Gıda ve Alkolsüz İçecekler"),
            ("Haberleşmeşubat.png", "Haberleşme"),
            ("Konutşubat.png", "Konut"),
            ("Lokanta ve otellerşubat.png", "Lokanta ve Oteller"),
            ("Ulaştırmaşubat.png", "Ulaştırma"),
            ("Çeşitli mal ve hizmetlerşubat.png", "Çeşitli Mal ve Hizmetler"),
        ]

        for image_path, caption in images:
            image = Image.open(image_path)
            st.image(image, caption=caption)

        st.write("Ham ve mevsimsellikten arındırılmış göstergelerin aylık artışları:")
        image18 = Image.open("maözelgöstergelerşubat.png")
        st.image(image18, caption="Ham ve mevsimsellikten arındırılmış göstergelerin aylık artışları")

        # Final section with trend and link
        st.write("Mevsimsellikten arındırılmış ana eğilimlere bakıldığında medyan artış %3,64 olmuştur.")
        st.write("SATRIM(Mevsimsel Düzeltilmiş Budanmış Enflasyon) göstergesi ise %3,86 artmıştır.")
        image18 = Image.open("eğilimşubat.png")
        st.image(image18, caption="Mevsimsellikten Arındırılmış Eğilim")


        # Footer
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
            <small>
                *Bu bültenin bir sonraki yayınlanma tarihi 24 Mart 2025'tir. Burada yer alan bilgi ve analizler tamamen kişisel çalışma olup kesin bir doğruluk içermemekte ve yatırım tavsiyesi içermemektedir.*<br>
                *TÜİK’in hesaplamasıyla uyumlu olması açısından ayın ilk 24 günündeki veriler dikkate alınmıştır.*
            </small>
        """, unsafe_allow_html=True)

        st.markdown("<p><strong>Hazırlayan: Bora Kaya</strong></p>", unsafe_allow_html=True)
        st.markdown("<p>Web-TÜFE Twitter: <a href='https://x.com/webtufe'>https://x.com/webtufe</a></p>", unsafe_allow_html=True)
        st.markdown("<p>Linkedin: <a href='https://www.linkedin.com/in/bora-kaya/'>https://www.linkedin.com/in/bora-kaya/</a></p>", unsafe_allow_html=True)


def hareketli_aylik_ortalama(df):
        değer = df.name  # Kolon ismi
        df = pd.DataFrame(df)
        df["Tarih"] = pd.to_datetime(df.index)  # Tarih sütununu datetime formatına çevir
        df["Gün Sırası"] = df.groupby(df["Tarih"].dt.to_period("M")).cumcount() + 1  # Her ay için gün sırasını oluştur
        
        # Her ay için ilk 24 günü sınırla ve hareketli ortalama hesapla
        df["Aylık Ortalama"] = (
            df[df["Gün Sırası"] <= 24]
            .groupby(df["Tarih"].dt.to_period("M"))[değer]
            .expanding()
            .mean()
            .reset_index(level=0, drop=True)
        )
        
        # Orijinal indeksi geri yükle
        df.index = pd.to_datetime(df.index)
        return df

if page=="Metodoloji Notu":
    import streamlit as st
    import requests
    
    
     

    # Başlık
    st.title("Web Tüketici Fiyat Endeksi (Web-TÜFE) Metodoloji Açıklaması")

    pdf_url = "https://raw.githubusercontent.com/kaboya19/web-tufe-streamlit/main/WEB%20TÜKETİCİ%20FİYAT%20ENDEKSİ.pdf"
    response = requests.get(pdf_url)
    if response.status_code == 200:
        st.download_button(
            label="📥 PDF'yi İndir",
            data=response.content,
            file_name="WEB TÜKETİCİ FİYAT ENDEKSİ.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("PDF indirilemedi. Lütfen bağlantıyı kontrol edin.")
    viewer_url = f"https://mozilla.github.io/pdf.js/web/viewer.html?file={pdf_url}"

    st.markdown(
        f'<iframe src="{viewer_url}" width="90%" height="800px" style="border:none;"></iframe>',
        unsafe_allow_html=True
    )
                

    st.markdown("<p><strong>Hazırlayan: Bora Kaya</strong></p>", unsafe_allow_html=True)
    st.markdown("<p>Web-TÜFE Twitter: <a href='https://x.com/webtufe'>https://x.com/webtufe</a></p>", unsafe_allow_html=True)
    st.markdown("<p>Linkedin: <a href='https://www.linkedin.com/in/bora-kaya/'>https://www.linkedin.com/in/bora-kaya/</a></p>", unsafe_allow_html=True)

   

    from PIL import Image

    # Logoları yükle
    logo1 = Image.open("Teknosa_logo.svg (1).png")
    logo3 = Image.open("855_arcelik.jpg")
    logo4 = Image.open("trendyol_logo-freelogovectors.net_.png")
    logo5 = Image.open("images (1).png")
    logo6 = Image.open("9_2_guncel-logo-kullanimimiz.jpg")
    logo7 = Image.open("resim-yok.jpg")
    logo8 = Image.open("unnamed (2).png")
    logo9 = Image.open("channels4_profile.jpg")
    logo10 = Image.open("madame-coco6296.logowik.com.webp")
    logo11 = Image.open("214279.png")
    logo12 = Image.open("3423.png")
    logo13 = Image.open("vivense-logo-png_seeklogo-445916.png")
    logo14 = Image.open("Logo_of_Mavi.png")
    logo15 = Image.open("Gratis-logo-big.svg.png")
    logo16 = Image.open("images.png")
    logo17 = Image.open("csa-logo.jpg")
    logo18 = Image.open("beymen-logo-png_seeklogo-18935.png")
    logo19 = Image.open("349_karaca_logo_ikon_ust.jpg")
    logo20 = Image.open("20200401091456!D&R_logo.jpg")
    logo21 = Image.open("Koctas_logo.png")
    logo22 = Image.open("Hepsiburada_logo_official.svg.png")
    logo23 = Image.open("Bauhaus_logo.svg.png")
    logo24 = Image.open("1280px-Boyner_Logo.jpg")
    logo25 = Image.open("793_defacto.jpg")
    logo26 = Image.open("pttavm.webp")
    logo27 = Image.open("N11_logo.svg.png")
    logo28 = Image.open("dc8e9a5099cd06581951bd48511afb3f-642e71cbd9cf4.webp")
    logo29 = Image.open("resim-yok.jpg")
    logo30 = Image.open("madame-coco6296.logowik.com.webp")
    logo31 = Image.open("sehzade_logo.png")
    logo32 = Image.open("mopas_web_logo.webp")
    logo33 = Image.open("Tarimkredilogo.jpg")
    logo34 = Image.open("A101_logo.svg.png")
    logo35 = Image.open("bim-logo-png_seeklogo-516849.png")
    logo36 = Image.open("hakmar_logo_transperent.png")
    logo37 = Image.open("ŞOK_Market_logo.svg.png")
    logo38 = Image.open("migros_logo.png")
    # Kolonlara yerleştir (yan yana)    
    cols = st.columns(4)

    with cols[0]:
        st.image(logo1, use_container_width=True)
        st.image(logo5, use_container_width=True)
        st.image(logo9, use_container_width=True)
        st.image(logo13, use_container_width=True)
        st.image(logo17, use_container_width=True)
        st.image(logo21, use_container_width=True)
        st.image(logo25, use_container_width=True)
        st.image(logo29, use_container_width=True)
        st.image(logo33, use_container_width=True)
        st.image(logo37, use_container_width=True)

    with cols[1]:
        st.image(logo6, use_container_width=True)
        st.image(logo10, use_container_width=True)
        st.image(logo14, use_container_width=True)
        st.image(logo18, use_container_width=True)
        st.image(logo22, use_container_width=True)
        st.image(logo26, use_container_width=True)
        st.image(logo30, use_container_width=True)
        st.image(logo34, use_container_width=True)
        st.image(logo38, use_container_width=True)

    with cols[2]:
        st.image(logo3, use_container_width=True)
        st.image(logo7, use_container_width=True)
        st.image(logo11, use_container_width=True)
        st.image(logo15, use_container_width=True)
        st.image(logo19, use_container_width=True)
        st.image(logo23, use_container_width=True)
        st.image(logo27, use_container_width=True)
        st.image(logo31, use_container_width=True)
        st.image(logo35, use_container_width=True)
    with cols[3]:
        st.image(logo4, use_container_width=True)
        st.image(logo8, use_container_width=True)
        st.image(logo12, use_container_width=True)
        st.image(logo16, use_container_width=True)
        st.image(logo20, use_container_width=True)
        st.image(logo24, use_container_width=True)
        st.image(logo28, use_container_width=True)
        st.image(logo32, use_container_width=True)
        st.image(logo36, use_container_width=True)
    
    


    




     

if page=="Tüketici Fiyat Endeksi":

    import streamlit as st

        # ---------------- Ayar ----------------
    secim = st.selectbox("Veri türünü seçin:", ["Madde", "Harcama Grubu"])
    hiz_slider = st.slider("Yazı kayma hızı (hızlı: 1, yavaş: 3)", min_value=1, max_value=3, value=2)
    kayma_suresi = hiz_slider * 2000  # Hızı kayma süresiyle ilişkilendiriyoruz

    # ---------------- Veri Yükleme ----------------
    if secim == "Madde":
        df = pd.read_csv("endeksler.csv", index_col=0)
        df.index = pd.to_datetime(df.index)
    else:
        df = pd.read_csv("harcama_grupları.csv", index_col=0).sort_index()
        df.index = pd.to_datetime(df.index)

    # ---------------- Günlük Değişim ----------------
    gunluk_degisimler = df.pct_change().dropna().iloc[-1].sort_values(ascending=False) * 100
    gunluk_degisimler = gunluk_degisimler.round(2)
    gunluk_degisimler = gunluk_degisimler[gunluk_degisimler != 0]

    tarihim = pd.to_datetime(df.index[-1]).day
    if tarihim > 24:
        tarihim = 24
    if tarihim < 10:
        tarihim = "0" + str(tarihim)
    tarih = df.index[-1]
    onceki_tarih = tarih - timedelta(days=30)

    ortalama_son = df.loc[tarih.strftime("%Y-%m"):tarih.strftime(f"%Y-%m-{tarihim}")].mean()
    ortalama_onceki = df.loc[onceki_tarih.strftime("%Y-%m-%d"):onceki_tarih.strftime(f"%Y-%m-{tarihim}")].mean()

    degisimler2 = (((ortalama_son / ortalama_onceki).sort_values(ascending=False)) - 1) * 100
    degisimler2 = degisimler2.round(2)
    degisimler2 = degisimler2[degisimler2 != 0]

    def olustur_kayan_yazi_html(degisimler, sure, class_suffix, bosluk_ekle=False):
        parcalar = []
        for madde, degisim in degisimler.items():
            renk = "red" if degisim > 0 else "green"
            madde_html = f"<b style='color:black'>{madde}:</b> <span style='color:{renk}'>%{degisim:+.2f}</span>"
            parcalar.append(madde_html)

        bosluk = "&nbsp;" * 10
        icerik = bosluk.join(10 * parcalar)

        if bosluk_ekle:
            # Yazının başına 1 seferlik boşluk ekliyoruz
            icerik = f"{bosluk*5}{icerik}"

        html = f"""
        <style>
        .scrolling-wrapper-{class_suffix} {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            overflow: hidden;
            box-sizing: border-box;
            background-color: #f0f0f0;
            padding: 10px;
            margin-top: 0; /* Başlık ile kayan yazı arasındaki boşluğu kaldır */
        }}
        .scrolling-content-{class_suffix} {{
            display: inline-block;
            white-space: nowrap;
            animation: scroll-left-{class_suffix} {sure}s linear infinite;
            padding-left: 20px;
        }}
        @keyframes scroll-left-{class_suffix} {{
            0%   {{ transform: translateX(0%); }}
            100% {{ transform: translateX(-100%); }}  /* Yazı tamamen sola kayacak şekilde */
        }}
        </style>
        <div class="scrolling-wrapper-{class_suffix}">
            <div class="scrolling-content-{class_suffix}">
                {icerik} {bosluk*5} {icerik}
            </div>
        </div>
        """
        return html

    # ---------------- Göster ----------------

    # 3 saniye bekleme ekliyoruz
    time.sleep(3)

    st.markdown("<b>Günlük Değişimler</b>", unsafe_allow_html=True)
    st.markdown(olustur_kayan_yazi_html(gunluk_degisimler, kayma_suresi, "daily", bosluk_ekle=True), unsafe_allow_html=True)

    st.markdown("<b>Aylık Değişimler</b>", unsafe_allow_html=True)
    st.markdown(olustur_kayan_yazi_html(degisimler2, kayma_suresi, "monthly", bosluk_ekle=True), unsafe_allow_html=True)

   


    st.markdown(
    """
    <style>
    .title {
        font-size: 36px;  
        font-family: 'Freestyle Script', Courier !important;  
        color: red !important;  
        text-align: center;  
    }
    </style>
    <h1 class="title">Hazırlayan: Bora Kaya</h1>
    """, 
    unsafe_allow_html=True)

    with st.expander("📌 Yapılan Revizyonlar (Son Revizyon:18.05.2025)"):
        st.markdown("""
        - **Şubat ayında elektrikte yapılan sübvansiyon düzenlemesi sebebiyle 
            TÜİK tarafından ortalama fiyatların yayınlanmasının ardından endeksin Şubat verisi revize olmuştur. (%3,5>>%3,83)
        - **: Gündelikçi ücretinde veri kaynağından kaynaklı geriye dönük fiyat güncellemesi yapılmış ve endeksin Mart verisi revize olmuştur. (%4,1>>%3,23) 🛠️ 
        - **Uçak bileti,Vapur bileti ve Şehirlerarası otobüs bileti ürünleri sepete eklenmiştir.
            Mart %3,23>>%3,16
            Nisan %2,57>>%2,66
                    olarak revize olmuştur.
        """)


    import streamlit as st
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from datetime import datetime

    
        
    


    
    tüfe = pd.read_csv("gruplar_int.csv",index_col=0)
    tüfe=pd.DataFrame(tüfe["TÜFE"])
    tüfe.index=pd.to_datetime(tüfe.index)

    endeksler=pd.read_csv("endeksler_int.csv",index_col=0)
    endeksler.index=pd.to_datetime(endeksler.index)
    sira=np.sort(endeksler.columns.values)
    endeksler=endeksler[sira]
   
    

    

    
    ağırlıklar=pd.read_csv("ağırlıklartüfe.csv",index_col=0)
    
    
    endeksler["TÜFE"]=tüfe["TÜFE"]

    sira = ['TÜFE'] + [col for col in endeksler.columns if col != 'TÜFE']


    endeksler = endeksler[sira]

    for col in endeksler.columns:
        endeksler[col]=endeksler[col].astype(float)
    

    

    gruplar = endeksler.columns


    selected_group = st.sidebar.selectbox("Ürün Seçin:", gruplar)
    formatted_dates = endeksler.index.strftime("%d.%m.%Y")  # "06.10.2024" formatında

    import streamlit as st
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from datetime import datetime

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = dict(st.secrets["gspread"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet_url = "https://docs.google.com/spreadsheets/d/1Y3SpFSsASfCzrM7iM-j_x5XR5pYv__8etC4ptaA9dio"
    worksheet = client.open_by_url(sheet_url).sheet1

    # --- Streamlit Sidebar: Abonelik Kutusu ---
    st.sidebar.title("📬 Bülten Aboneliği")

    email = st.sidebar.text_input("E-posta adresiniz")
    action = st.sidebar.radio("Ne yapmak istersiniz?", ["Abone ol", "Çık"])

    if st.sidebar.button("Gönder"):
        if "@" not in email or "." not in email:
            st.sidebar.error("Lütfen geçerli bir e-posta adresi girin.")
        else:
            # Tüm e-postaları oku
            emails = worksheet.col_values(1)

            if action == "Abone ol":
                if email in emails:
                    st.sidebar.info("Bu e-posta zaten abone.")
                else:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    worksheet.append_row([email, now])
                    st.sidebar.success("Aboneliğiniz başarıyla eklendi 🎉")

            elif action == "Çık":
                if email in emails:
                    cell = worksheet.find(email)
                    worksheet.delete_rows(cell.row)
                    st.sidebar.success("Aboneliğiniz iptal edildi.")
                else:
                    st.sidebar.info("Bu e-posta zaten abone değil.")

    
   

    
    
        
    selected_group_data = endeksler[selected_group]

   

    selected_group_data=pd.DataFrame(selected_group_data)

        # Datetime index'i atıyoruz
    selected_group_data.index = endeksler.index
    selected_group_monthly=selected_group_data.resample('M').mean()
    selected_group_monthlyfull=selected_group_data.resample('M').last()
    from datetime import datetime,timedelta
    import pytz
    gfe1=tüfe.copy()
    gfe1["Date"]=pd.to_datetime(gfe1.index)
    gfe1["Ay"]=gfe1["Date"].dt.month
    gfe1["Yıl"]=gfe1["Date"].dt.year    
    month = gfe1["Ay"].iloc[-1]
    year=gfe1["Yıl"].iloc[-1] 
    oncekiyear=gfe1["Yıl"].iloc[-1] 
   

        # İlk ve son tarihleri belirleme
    first_date = selected_group_data.index[0].strftime("%d.%m.%Y")  # İlk tarihi formatlama
    last_date = selected_group_data.index[-1].strftime("%d.%m.%Y")  # Son tarihi formatlama
    selected_group_data1=selected_group_data.copy()
    selected_group_data1["Tarih"]=pd.to_datetime(selected_group_data1.index)
    ay_data = selected_group_data1[selected_group_data1['Tarih'].dt.month == month]
    
    ilk=ay_data.index[0].strftime("%d.%m.%Y")
    son=ay_data.index[-1].strftime("%d.%m.%Y")

        # Değişim yüzdesini hesaplama
    first_value = 100
    last_value = selected_group_data.iloc[-1,0] # Son değer
    change_percent = ((last_value - first_value) / first_value) * 100  # Yüzde değişim
    change_percent = round(change_percent, 2)

    #monthly=np.round(((selected_group_monthly.iloc[-1,0])/(selected_group_monthly.iloc[-2,0])-1)*100,2)

    def hareketli_aylik_ortalama(df):
        değer = df.name  # Kolon ismi
        df = pd.DataFrame(df)
        df["Tarih"] = pd.to_datetime(df.index)  # Tarih sütununu datetime formatına çevir
        df["Gün Sırası"] = df.groupby(df["Tarih"].dt.to_period("M")).cumcount() + 1  # Her ay için gün sırasını oluştur
        
        # Her ay için ilk 24 günü sınırla ve hareketli ortalama hesapla
        df["Aylık Ortalama"] = (
            df[df["Gün Sırası"] <= 24]
            .groupby(df["Tarih"].dt.to_period("M"))[değer]
            .expanding()
            .mean()
            .reset_index(level=0, drop=True)
        )
        
        # Orijinal indeksi geri yükle
        df.index = pd.to_datetime(df.index)
        return df
    

   
    
    tarihim=pd.to_datetime(gfe1.index[-1]).day
    if tarihim>24:
        tarihim=24
    if tarihim<10:
        tarihim="0"+str(tarihim)
    

    def hareketli_aylik_ortalama1(df):
            değer=df.name
            df=pd.DataFrame(df)
            df["Tarih"]=pd.to_datetime(df.index)
            df['Aylık Ortalama'] = df.groupby(df['Tarih'].dt.to_period('M'))[değer].expanding().mean().reset_index(level=0, drop=True)
            df.index=pd.to_datetime(df.index)
            return df
    

    def aylik_degisim_serisi(ts: pd.Series) -> pd.Series:
        ts = ts.sort_index()
        aylik_degisim = []

        for tarih in ts.index:
            gun = tarih.day
            ay = tarih.month
            yil = tarih.year

            # Bu ay ve geçen ay için veri
            bu_ay = ts[(ts.index.year == yil) & (ts.index.month == ay)]
            if ay == 1:
                onceki_ay = ts[(ts.index.year == yil - 1) & (ts.index.month == 12)]
            else:
                onceki_ay = ts[(ts.index.year == yil) & (ts.index.month == ay - 1)]

            if gun <= 24:
                ort_bu = bu_ay.iloc[:gun].mean()
                ort_onceki = onceki_ay.iloc[:gun].mean()

                if pd.notna(ort_bu) and pd.notna(ort_onceki) and ort_onceki != 0:
                    oran = (ort_bu / ort_onceki) - 1
                    aylik_degisim.append(oran*100)
                else:
                    aylik_degisim.append(None)
            else:
                try:
                    tarih_24 = bu_ay.index[23]
                    oran_24 = aylik_degisim[ts.index.get_loc(tarih_24)]
                    aylik_degisim.append(oran_24)
                except:
                    aylik_degisim.append(None)

        return pd.Series(aylik_degisim[-gun:], index=ts.index[-gun:])



    
    hareketlima = hareketli_aylik_ortalama(selected_group_data.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill")
    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=30)).strftime("%Y-%m")
    cari=hareketli_aylik_ortalama(selected_group_data.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
    hareketliartıs=aylik_degisim_serisi(selected_group_data.iloc[:,0])




    if selected_group == "TÜFE":

    
        st.markdown(f"<h2 style='text-align:left; color:black;'>Web Tüketici Fiyat Endeksi</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Fiyat Endeksi</h2>", unsafe_allow_html=True)
    
    figgartıs = go.Figure()
    figgartıs.add_trace(go.Scatter(
                x=hareketliartıs.index,
                y=hareketliartıs.values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
    
    figgartıs.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index,  # Original datetime index
                ticktext=selected_group_data.index.strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    

    

    

        # Grafiği çizme
    figgalt = go.Figure()
    tickvals = selected_group_data.index[::5]  # Her 3 birimde bir tarih
    ticktext = tickvals.strftime("%d.%m.%Y")  # Tarih formatını özelleştir
    if selected_group!="TÜFE":
        figgalt.add_trace(go.Scatter(
                x=selected_group_data.index[0:],
                y=selected_group_data.iloc[0:,0].values,
                mode='lines',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
        



    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgalt.update_layout(
            xaxis=dict(
                tickvals=tickvals,  # Original datetime index
                ticktext=ticktext,  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
   
    

  
   
   

      

  
   

   

   
    if selected_group!="TÜFE":
        tickvals = selected_group_data.index[::5]  # Her 3 birimde bir tarih
        ticktext = tickvals.strftime("%d.%m.%Y")  # Tarih formatını özelleştir

        aylikdegisim=((hareketlima.iloc[-1]/hareketlima.loc[f"{onceki}-{tarihim}"])-1)*100
        
        aylikdegisim=aylikdegisim.round(2)
        st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                01.01.2025 - {last_date} Değişimi: <span style='color:red;'>%{change_percent}</span><br>
                Mayıs Değişimi: <span style='color:red;'>%{aylikdegisim}</span><br>
            </h3>
            """, unsafe_allow_html=True)
        

  

        
        st.plotly_chart(figgalt)

        st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Aylık Artış Oranı</h2>", unsafe_allow_html=True)
        st.plotly_chart(figgartıs)

        fig30 = go.Figure()
        fig30.add_trace(go.Scatter(
                    x=selected_group_data.iloc[:,0].pct_change(30).dropna().index,
                    y=(selected_group_data.iloc[:,0].pct_change(30).dropna()*100).values,
                    mode='lines+markers',
                    name=selected_group,
                    line=dict(color='blue', width=4),
                    marker=dict(size=8, color="black"),
                    hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
                ))
        
        fig30.update_layout(
                xaxis=dict(
                    tickvals=selected_group_data.index[::5],  # Original datetime index
                    ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                    tickfont=dict(size=14, family="Arial Black", color="black"),
                ),
                yaxis=dict(
                    tickfont=dict(size=14, family="Arial Black", color="black")
                ),
                font=dict(family="Arial", size=14, color="black")
            )
        
        st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} 30 Günlük Artış Hızı (%)</h2>", unsafe_allow_html=True)
    
        st.plotly_chart(fig30)




        
    elif selected_group=="TÜFE":

        

        tüfem=tüfe.copy()
        tüfem.loc[pd.to_datetime("2024-12-31")]=100
        tüfem=tüfem.sort_index()

        figgalt.add_trace(go.Scatter(
                x=tüfem.index,
                y=tüfem["TÜFE"].values,
                mode='lines',
                name="Web-TÜFE",
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
        tüik=pd.read_csv("tüik.csv",index_col=0)
        figgalt.add_trace(
    go.Scatter(
        x=tüik.index,
        y=tüik["TÜİK"].values,
        mode="lines",
        line=dict(shape="hv",color="red", width=4),  # 'hv' yatay-dikey step grafiği
        name="TÜİK TÜFE",
        marker=dict(size=8, color="black"),
        hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
    )
)

        
        aylikdegisim=((hareketlima.iloc[-1]/hareketlima.loc[f"{onceki}-{tarihim}"])-1)*100
        aylikdegisim=aylikdegisim.round(2)
        günüm=datetime.now().day
        if günüm<24:
            st.markdown(f"""
                <h3 style='text-align:left; color:black;'>
                    01.01.2025 - {last_date} Değişimi: <span style='color:red;'>%{change_percent}</span><br>
                    Mayıs Değişimi: <span style='color:red;'>%{aylikdegisim}</span><br>
                    <span style='color:red;'>Nisan 2025 bülteni yayınlandı: <a href='https://github.com/kaboya19/web-tufe-streamlit/raw/main/webtüfenisan25.pdf' target='_blank'>Link</a></span
                </h3>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
    <h3 style='text-align:left; color:black;'>
        01.01.2025 - {last_date} Değişimi: <span style='color:red;'>%{change_percent}</span><br>
        <span style='color:red;'>Web Tüketici Fiyat Endeksi Nisanda %{aylikdegisim} arttı.</span><br>
        <span style='color:red;'>Nisan 2025 bülteni yayınlandı: <a href='https://github.com/kaboya19/web-tufe-streamlit/raw/main/webtüfenisan25.pdf' target='_blank'>Link</a></span>
    </h3>
    """, unsafe_allow_html=True)

            
        st.markdown("""
    <div style="font-size: 18px; color: black; background-color: #f0f0f0; padding: 15px; border-radius: 5px;">
        Not: Nihai veriler ayın 24.günü oluşmaktadır.
    </div>
""", unsafe_allow_html=True)
        

        st.plotly_chart(figgalt)

        
   
        
      
        
        st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Aylık Artış Oranı</h2>", unsafe_allow_html=True)
        st.markdown("""
    <div style="font-size: 18px; color: black; background-color: #f0f0f0; padding: 15px; border-radius: 5px;">
        Not: Aylık artış oranı mevcut ayın ortalamasının önceki ayın aynı dönemdeki ortalamasına göre değişimi ile hazırlanmıştır.
    </div>
""", unsafe_allow_html=True)
        st.plotly_chart(figgartıs)


        fig30 = go.Figure()
        fig30.add_trace(go.Scatter(
                    x=selected_group_data.iloc[:,0].pct_change(30).dropna().index,
                    y=(selected_group_data.iloc[:,0].pct_change(30).dropna()*100).values,
                    mode='lines+markers',
                    name=selected_group,
                    line=dict(color='blue', width=4),
                    marker=dict(size=8, color="black"),
                    hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
                ))
        
        fig30.update_layout(
                xaxis=dict(
                    tickvals=selected_group_data.index[::5],  # Original datetime index
                    ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                    tickfont=dict(size=14, family="Arial Black", color="black"),
                ),
                yaxis=dict(
                    tickfont=dict(size=14, family="Arial Black", color="black")
                ),
                font=dict(family="Arial", size=14, color="black")
            )
        
        st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} 30 Günlük Artış Hızı (%)</h2>", unsafe_allow_html=True)
    
        st.plotly_chart(fig30)

        figcomp=go.Figure()
        tüik=pd.read_csv("tüik.csv",index_col=0)
        tüik.index=pd.to_datetime(tüik.index)
        tüik=tüik.resample('M').last()
       
        tüik_aylık=tüik["TÜİK"].pct_change().dropna().iloc[1:]*100
        tüik_aylık=tüik_aylık.round(2)
        tüik_aylık.index=pd.to_datetime(tüik_aylık.index)

        cari=hareketli_aylik_ortalama(tüfe.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill")
        tüfeaylıkdata=cari.resample('M').last().pct_change().loc["2025-02":]*100
        tüfeaylıkdata.iloc[-1]=hareketliartıs.iloc[-1]
        tüfeaylıkdata=pd.DataFrame(tüfeaylıkdata)
        tüfeaylıkdata.columns=["Aylık Artış"]

       
        tüfeaylıkdata["TÜİK"]=tüik_aylık
        tüfeaylıkdata=tüfeaylıkdata.round(2)
        figcomp.add_trace(go.Bar(
            x=tüfeaylıkdata.index.strftime("%Y-%m"),
            y=tüfeaylıkdata["Aylık Artış"],
            name="Web-TÜFE",
            marker=dict(color='blue'),
            text=tüfeaylıkdata["Aylık Artış"],  # Değerleri göster
            textposition='outside',
            hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>',  # Tüm değerler barların üstünde olacak
            textfont=dict(
                color='black',
                size=13,
                family='Arial Black'  # Font Arial Black
            )
        ))

        figcomp.add_trace(go.Bar(
            x=tüfeaylıkdata.index.strftime("%Y-%m"),
            y=tüfeaylıkdata["TÜİK"],
            name="TÜİK",
            marker=dict(color='red'),
            text=tüfeaylıkdata["TÜİK"],  # Değerleri göster
            textposition='outside',
            hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>',  # Tüm değerler barların üstünde olacak
            textfont=dict(
                color='black',
                size=13,
                family='Arial Black'  # Font Arial Black
            )
        ))
        tickvals = tüfeaylıkdata.index
        ticktext = tickvals.strftime("%Y-%m")
        figcomp.update_layout(
            barmode='group',  # Barlar gruplanmış şekilde gösterilir
            title=dict(
                text=f"TÜİK ve Web-TÜFE Aylık Değişim Karşılaştırması",
                font=dict(size=18, color="black", family="Arial Black")
            ),
            xaxis=dict(
                tickmode='array',
                tickvals=tüfeaylıkdata.index.strftime("%Y-%m"),
                ticktext=ticktext,
                tickangle=-0,
                tickfont=dict(size=15, color="black", family="Arial Black")
            ),
            yaxis=dict(
                title='Aylık Değişim (%)',
                tickfont=dict(size=15, color="black", family="Arial Black")            ),
            legend=dict(
                x=1,
                y=1,
                xanchor='right',
                yanchor='top',
                font=dict(size=12, color="black", family="Arial Black"),
                bgcolor='rgba(255,255,255,0.8)',  # Arka plan rengi (şeffaf beyaz)
                bordercolor='black',
                borderwidth=1
            ),
            bargap=0.2,  # Barlar arası boşluk
            bargroupgap=0.1,  # Gruplar arası boşluk
            margin=dict(t=50, b=50, l=50, r=50)  # Kenar boşlukları
        )
       
        st.plotly_chart(figcomp)
        










        gruplar24=pd.read_csv("gruplar24.csv",index_col=0)
        gruplar=pd.read_csv("anagruplar.csv",index_col=0)
        gruplar.index=pd.to_datetime(gruplar.index)
        gruplar["TÜFE"]=tüfe["TÜFE"]
        harcama_artıs=pd.Series(index=gruplar.columns)
        for col in gruplar.columns:
            harcama_artıs.loc[col]=((hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-{tarihim}"])-1)*100
        harcama_artıs=harcama_artıs.sort_values()

        colors = ['red' if label == 'TÜFE' else 'blue' for label in harcama_artıs.index]

        # İlk 42 karakteri almak için index etiketlerini kısaltma
        shortened_index = [label[:42] for label in harcama_artıs.index]

        # Grafik oluşturma
        # Grafik oluşturma
        # Grafik oluşturma
        figartıs = go.Figure()

        # Verileri ekleme
        figartıs.add_trace(go.Bar(
            y=shortened_index,  # Kısaltılmış index etiketleri
            x=harcama_artıs.values,
            orientation='h', 
            marker=dict(color=colors),
            name=f'Artış Oranı',
        ))

        # FiveThirtyEight tarzı ayarlar
        figartıs.update_layout(
            title={
                'text': "Web-TÜFE Ana Gruplar Artış Oranları",  # Başlık metni
                'x': 0.5,  # Ortalamak için 0.5
                'xanchor': 'center',  # Yatay hizalama
                'yanchor': 'top'  # Dikey hizalama
            },
            xaxis_title='Artış Oranı (%)',
            yaxis_title='Grup',
            xaxis=dict(
                tickformat='.2f',
                gridcolor='lightgray',  # X ekseni için grid çizgileri
                zerolinecolor='lightgray',
                zerolinewidth=1
            ),
            yaxis=dict(
                tickfont=dict(family="Arial Black", size=14, color="black"),
                tickmode='array',
                tickvals=list(range(len(harcama_artıs.index))),
                ticktext=shortened_index,
                gridcolor='lightgray',  # Y ekseni için grid çizgileri
            ),
            bargap=0.5,  # Çubuklar arasındaki boşluk
            height=600,
            font=dict(family="Arial Black", size=14, color="black"),
            plot_bgcolor='whitesmoke',  # Grafik arka planı
            paper_bgcolor='white',  # Kağıt (arka plan) rengi
        )

        # Etiket ekleme (arka planlı)
        for i, value in enumerate(harcama_artıs.values):
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),
                align='left' if value >= 0 else 'right',
                xanchor='left' if value >= 0 else 'right',
                yanchor='middle',
                bgcolor='rgba(200, 200, 200, 0.8)',  # Etiket arka plan rengi (şeffaf gri)
                bordercolor='black',  # Sınır rengi
                borderwidth=1,  # Sınır genişliği
                borderpad=4  # Sınır ile metin arasındaki boşluk
            )

        # Streamlit ile grafiği görüntüleme
        st.markdown(f"<h2 style='text-align:left; color:black;'>Web-TÜFE Ana Gruplar Artış Oranları</h2>", unsafe_allow_html=True)
        st.plotly_chart(figartıs)

        sheet_url = "https://docs.google.com/spreadsheets/d/14iiu_MQwtMxHTFt6ceyFhkk6v0OL-wuoQS1IGPzSpNE"

        # Başlık veya açıklama

        # Tıklanabilir buton
        if st.button("Web TÜFE Veriseti"):
            st.markdown(f"[Google Sheet'e Git]({sheet_url})", unsafe_allow_html=True)

        
        
        

        

        

      




        
             



    
    
    
    
  
    
    
    


    


    
    


    
    
   
        
        

    
    if selected_group == "WEB-GFE":
        turkish_months = [
    "Eylül 23", "Ekim 23", "Kasım 23", "Aralık 23", 
    "Ocak 24", "Şubat 24", "Mart 24", "Nisan 24", 
    "Mayıs 24", "Haziran 24", "Temmuz 24","Ağustos 24","Eylül 24","Ekim 24","Kasım 24","Aralık 24"
]




        from io import BytesIO
        import pandas as pd

        from io import BytesIO
        import pandas as pd

       


        
        

        


        
        
       
       

        
      

        
          


        
    
        
if page=="Ana Gruplar":
    def aylik_degisim_serisi(ts: pd.Series) -> pd.Series:
        ts = ts.sort_index()
        aylik_degisim = []

        for tarih in ts.index:
            gun = tarih.day
            ay = tarih.month
            yil = tarih.year

            # Bu ay ve geçen ay için veri
            bu_ay = ts[(ts.index.year == yil) & (ts.index.month == ay)]
            if ay == 1:
                onceki_ay = ts[(ts.index.year == yil - 1) & (ts.index.month == 12)]
            else:
                onceki_ay = ts[(ts.index.year == yil) & (ts.index.month == ay - 1)]

            if gun <= 24:
                ort_bu = bu_ay.iloc[:gun].mean()
                ort_onceki = onceki_ay.iloc[:gun].mean()

                if pd.notna(ort_bu) and pd.notna(ort_onceki) and ort_onceki != 0:
                    oran = (ort_bu / ort_onceki) - 1
                    aylik_degisim.append(oran*100)
                else:
                    aylik_degisim.append(None)
            else:
                try:
                    tarih_24 = bu_ay.index[23]
                    oran_24 = aylik_degisim[ts.index.get_loc(tarih_24)]
                    aylik_degisim.append(oran_24)
                except:
                    aylik_degisim.append(None)

        return pd.Series(aylik_degisim[-gun:], index=ts.index[-gun:])
    from datetime import datetime,timedelta
    import pytz
    tüfe=pd.read_csv("tüfe.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    gfe1=tüfe.copy()
    gfe1["Date"]=pd.to_datetime(gfe1.index)
    gfe1["Ay"]=gfe1["Date"].dt.month
    gfe1["Yıl"]=gfe1["Date"].dt.year    
    month = gfe1["Ay"].iloc[-1]
    year=gfe1["Yıl"].iloc[-1] 
    oncekiyear=gfe1["Yıl"].iloc[-1] 
    tarihim=pd.to_datetime(gfe1.index[-1]).day
    if tarihim>24:
        tarihim=24
    if tarihim<10:
        tarihim="0"+str(tarihim)

    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=30)).strftime("%Y-%m")

    



    gruplar=pd.read_csv("gruplar_int.csv",index_col=0)
    gruplar.index=pd.to_datetime(gruplar.index)
    gruplar.loc[pd.to_datetime("2024-12-31")]=100
    gruplar=gruplar.sort_index()

    
    
    ana = gruplar.columns[:-1]
    

    selected_group = st.sidebar.selectbox("Ana Grup Seçin:", ana)

    selected_group_data=gruplar[selected_group]

    aylık=(((hareketli_aylik_ortalama(gruplar[selected_group])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(gruplar[selected_group])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-{tarihim}"])-1)*100)
    aylık=aylık.round(2)


   

    
    hareketliartıs=aylik_degisim_serisi(selected_group_data)


    figgartıs = go.Figure()
    figgartıs.add_trace(go.Scatter(
                x=hareketliartıs.index,
                y=hareketliartıs.values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
    
    figgartıs.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index,  # Original datetime index
                ticktext=selected_group_data.index.strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )

    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Endeksi</h2>", unsafe_allow_html=True)

    first_date = selected_group_data.index[0].strftime("%d.%m.%Y")  # İlk tarihi formatlama
    last_date = selected_group_data.index[-1].strftime("%d.%m.%Y")  # Son tarihi formatlama
  

        # Değişim yüzdesini hesaplama
    first_value = 100
    last_value = selected_group_data.iloc[-1] # Son değer
    change_percent = ((last_value - first_value) / first_value) * 100  # Yüzde değişim
    change_percent = round(change_percent, 2)

    

    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                31.12.2024 - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                Mayıs Değişimi: <span style='color:red;'>% {aylık}</span><br>
                

            </h3>
            """, unsafe_allow_html=True)
    


    figgana= go.Figure()
    
    figgana.add_trace(go.Scatter(
                x=selected_group_data.index,
                y=selected_group_data.values,
                mode='lines',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
    




    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgana.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index[::5],  # Original datetime index
                ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.plotly_chart(figgana)
    

    data=pd.read_excel("harcama gruplarina gore endeks sonuclari.xlsx")
    data=data.iloc[1:,:]
    data.columns=data.iloc[1,:]

    data=data.drop(1,axis=0)
    data=data.drop(2,axis=0)
    data=data.iloc[1:,3:]
    data=data.set_index(pd.date_range(start="2005-01-31",freq="M",periods=len(data)))

    data=data.iloc[:,1:13]
    data=data.rename(columns={"Konut, su, elektrik, gaz ve diğer yakıtlar":"Konut","Mobilya, ev aletleri ve ev bakım hizmetleri":"Ev eşyası"})
    data=data.drop(["Sağlık","Alkollü içecekler ve tütün"],axis=1)
    data=data[[selected_group]]
    data=data.pct_change().dropna().loc["2025-02":]*100
    

    gruplar=pd.read_csv("gruplar_int.csv",index_col=0)
    gruplar.index=pd.to_datetime(gruplar.index)
    gruplar=gruplar.sort_index()
    gruplar_aylık=pd.DataFrame(columns=gruplar.columns)
    for col in gruplar.columns:
        cari=hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill")
        gruplar_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
        carim=hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
        hareketliartıs=aylik_degisim_serisi(selected_group_data)

        gruplar_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
        gruplar_aylık=pd.DataFrame(gruplar_aylık)
    gruplar_aylık=np.round(gruplar_aylık,2)

    gruplar_aylık["Tarih"]=(gruplar_aylık.index)
    cols=["Tarih"]
    cols.extend(gruplar.columns)
    gruplar_aylık=gruplar_aylık[cols]
    gruplar_aylık=gruplar_aylık.reset_index(drop=True)
    gruplar_aylık=gruplar_aylık.set_index("Tarih")
    tüikdata=pd.DataFrame(index=gruplar_aylık.index)




    tüikdata["Web-TÜFE"]=gruplar_aylık[selected_group]
    tüikdata["TÜİK"]=data
    tüikdata=tüikdata.round(2)

    figcompana=go.Figure()
    figcompana.add_trace(go.Bar(
            x=tüikdata.index.strftime("%Y-%m"),
            y=tüikdata["Web-TÜFE"],
            name="Web-TÜFE",
            marker=dict(color='blue'),
            text=tüikdata["Web-TÜFE"],  # Değerleri göster
            textposition='outside',
            hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>',  # Tüm değerler barların üstünde olacak
            textfont=dict(
                color='black',
                size=13,
                family='Arial Black'  # Font Arial Black
            )
        ))

    figcompana.add_trace(go.Bar(
        x=tüikdata.index.strftime("%Y-%m"),
        y=tüikdata["TÜİK"],
        name="TÜİK",
        marker=dict(color='red'),
        text=tüikdata["TÜİK"],  # Değerleri göster
        textposition='outside',
        hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>',  # Tüm değerler barların üstünde olacak
        textfont=dict(
            color='black',
            size=13,
            family='Arial Black'  # Font Arial Black
        )
    ))
    tickvals = tüikdata.index
    ticktext = tickvals.strftime("%Y-%m")
    figcompana.update_layout(
        barmode='group',  # Barlar gruplanmış şekilde gösterilir
        title=dict(
            text=f"{selected_group} TÜİK ve Web-TÜFE Aylık Değişim Karşılaştırması",
            font=dict(size=18, color="black", family="Arial Black")
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=tüikdata.index.strftime("%Y-%m"),
            ticktext=ticktext,
            tickangle=-0,
            tickfont=dict(size=15, color="black", family="Arial Black")
        ),
        yaxis=dict(
            title='Aylık Değişim (%)',
            tickfont=dict(size=15, color="black", family="Arial Black")            ),
        legend=dict(
            x=1,
            y=1,
            xanchor='right',
            yanchor='top',
            font=dict(size=12, color="black", family="Arial Black"),
            bgcolor='rgba(255,255,255,0.8)',  # Arka plan rengi (şeffaf beyaz)
            bordercolor='black',
            borderwidth=1
        ),
        bargap=0.2,  # Barlar arası boşluk
        bargroupgap=0.1,  # Gruplar arası boşluk
        margin=dict(t=50, b=50, l=50, r=50)  # Kenar boşlukları
    )
    
    st.plotly_chart(figcompana)

    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Grubu Aylık Artışı</h2>", unsafe_allow_html=True)

    st.plotly_chart(figgartıs)

    fig30 = go.Figure()
    fig30.add_trace(go.Scatter(
                x=selected_group_data.pct_change(30).dropna().index,
                y=(selected_group_data.pct_change(30).dropna()*100).values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
    
    fig30.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index[::5],  # Original datetime index
                ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} 30 Günlük Artış Hızı (%)</h2>", unsafe_allow_html=True)

    st.plotly_chart(fig30)
    


    

    ürüngrupları=pd.read_csv("harcamaürünleri1.csv",index_col=0)
    ürüngrupları=ürüngrupları[ürüngrupları["Ana Grup"]==selected_group]

    harcama = ürüngrupları["Grup"].unique()


 

    harcama_grupları=pd.read_csv("harcama_grupları.csv",index_col=0)
    harcama_grupları.index=pd.to_datetime(harcama_grupları.index)
    harcama_grupları=harcama_grupları.sort_index()
    selected_harcamagrupları=harcama_grupları[harcama]
    anagruplar=pd.read_csv("gruplar_int.csv",index_col=0)
    anagruplar.index=pd.to_datetime(anagruplar.index)

    selected_harcamagrupları[selected_group]=anagruplar[selected_group]


    selected_harcamagruplarıartıs=pd.DataFrame(columns=selected_harcamagrupları.columns)
    for col in selected_harcamagrupları.columns:
        cari=hareketli_aylik_ortalama(selected_harcamagrupları[col])["Aylık Ortalama"].fillna(method="ffill")
        selected_harcamagruplarıartıs[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
        carim=hareketli_aylik_ortalama(selected_harcamagrupları[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
        hareketliartıs=aylik_degisim_serisi(selected_harcamagrupları[col])

        selected_harcamagruplarıartıs[col].iloc[-1]=hareketliartıs.iloc[-1]
        selected_harcamagruplarıartıs=pd.DataFrame(selected_harcamagruplarıartıs)
    selected_harcamagruplarıartıs["Tarih"]=(selected_harcamagruplarıartıs.index.strftime("%Y-%m"))

   

    # Başlığın font büyüklüğünü artırma
    st.markdown(
        """
        <style>
        label[for="Tarih Seçin:"] {
            font-size: 20px !important;
            font-weight: bold;
        }
        div[data-baseweb="select"] > div {
            font-size: 18px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Selectbox başlığını ayrı bir markdown ile büyütme
    st.markdown('<p style="font-size:20px; font-weight:bold;">Tarih Seçin:</p>', unsafe_allow_html=True)

    # Selectbox
    selected_tarih = st.selectbox("", selected_harcamagruplarıartıs["Tarih"].values[::-1])
    
   


    
    

    selected_harcamagruplarıartıs=selected_harcamagruplarıartıs[selected_harcamagruplarıartıs["Tarih"]==selected_tarih].iloc[0]





    selected_harcamagruplarıartıs=selected_harcamagruplarıartıs.drop("Tarih",axis=0).sort_values()

    colors = ['red' if label == f"{selected_group}" else 'blue' for label in selected_harcamagruplarıartıs.index]

    # İlk 42 karakteri almak için index etiketlerini kısaltma
    shortened_index = [label[:200] for label in selected_harcamagruplarıartıs.index]

    # Grafik oluşturma
    figartıs = go.Figure()

    # Verileri ekleme
    figartıs.add_trace(go.Bar(
        y=shortened_index,  # Kısaltılmış index etiketleri
        x=selected_harcamagruplarıartıs.values,
        orientation='h', 
        marker=dict(color=colors),
        name=f'Artış Oranı',
    ))

    if selected_group!="Gıda ve alkolsüz içecekler":
        figartıs.update_layout(
            title={
            'text': "Web-TÜFE Artış Oranları",  # Başlık metni
            'x': 0.5,  # Ortalamak için 0.5
            'xanchor': 'center',  # Yatay hizalama
            'yanchor': 'top'  # Dikey hizalama
        },
            xaxis_title='Artış Oranı (%)',
            yaxis_title='Grup',
            xaxis=dict(tickformat='.2f'),
            bargap=0.5,  # Çubuklar arasındaki boşluk
            height=600,  # Grafik boyutunu artırma
            font=dict(family="Arial Black", size=14, color="black"),  # Yazı tipi ve kalınlık
            yaxis=dict(
                tickfont=dict(family="Arial Black", size=14, color="black"),  # Y eksenindeki etiketlerin rengi
                tickmode='array',  # Manuel olarak etiketleri belirlemek için
                tickvals=list(range(len(selected_harcamagruplarıartıs.index))),  # Her bir index için bir yer belirle
                ticktext=shortened_index  # Kısaltılmış index etiketleri
            )
        )
    else:
        figartıs.update_layout(
            title={
            'text': "Web-TÜFE Artış Oranları",  # Başlık metni
            'x': 0.5,  # Ortalamak için 0.5
            'xanchor': 'center',  # Yatay hizalama
            'yanchor': 'top'  # Dikey hizalama
        },
            xaxis_title='Artış Oranı (%)',
            yaxis_title='Grup',
            xaxis=dict(tickformat='.2f'),
            bargap=0.5,  # Çubuklar arasındaki boşluk
            height=1200,  # Grafik boyutunu artırma
            font=dict(family="Arial Black", size=14, color="black"),  # Yazı tipi ve kalınlık
            yaxis=dict(
                tickfont=dict(family="Arial Black", size=14, color="black"),  # Y eksenindeki etiketlerin rengi
                tickmode='array',  # Manuel olarak etiketleri belirlemek için
                tickvals=list(range(len(selected_harcamagruplarıartıs.index))),  # Her bir index için bir yer belirle
                ticktext=shortened_index  # Kısaltılmış index etiketleri
            )
        )


    # Etiket ekleme
    for i, value in enumerate(selected_harcamagruplarıartıs.values):
        if value >= 0:
            # Pozitif değerler sol tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='left', 
                xanchor='left', 
                yanchor='middle'
            )
        else:
            # Negatif değerler sağ tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='right', 
                xanchor='right', 
                yanchor='middle'
            )




    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Harcama Grupları Artış Oranları</h2>", unsafe_allow_html=True)
    st.plotly_chart(figartıs)





if page=="Harcama Grupları":
    def aylik_degisim_serisi(ts: pd.Series) -> pd.Series:
        ts = ts.sort_index()
        aylik_degisim = []

        for tarih in ts.index:
            gun = tarih.day
            ay = tarih.month
            yil = tarih.year

            # Bu ay ve geçen ay için veri
            bu_ay = ts[(ts.index.year == yil) & (ts.index.month == ay)]
            if ay == 1:
                onceki_ay = ts[(ts.index.year == yil - 1) & (ts.index.month == 12)]
            else:
                onceki_ay = ts[(ts.index.year == yil) & (ts.index.month == ay - 1)]

            if gun <= 24:
                ort_bu = bu_ay.iloc[:gun].mean()
                ort_onceki = onceki_ay.iloc[:gun].mean()

                if pd.notna(ort_bu) and pd.notna(ort_onceki) and ort_onceki != 0:
                    oran = (ort_bu / ort_onceki) - 1
                    aylik_degisim.append(oran*100)
                else:
                    aylik_degisim.append(None)
            else:
                try:
                    tarih_24 = bu_ay.index[23]
                    oran_24 = aylik_degisim[ts.index.get_loc(tarih_24)]
                    aylik_degisim.append(oran_24)
                except:
                    aylik_degisim.append(None)

        return pd.Series(aylik_degisim[-gun:], index=ts.index[-gun:])
    from datetime import datetime,timedelta
    import pytz
    tüfe=pd.read_csv("tüfe.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    gfe1=tüfe.copy()
    gfe1["Date"]=pd.to_datetime(gfe1.index)
    gfe1["Ay"]=gfe1["Date"].dt.month
    gfe1["Yıl"]=gfe1["Date"].dt.year    
    month = gfe1["Ay"].iloc[-1]
    year=gfe1["Yıl"].iloc[-1] 
    oncekiyear=gfe1["Yıl"].iloc[-1] 
    tarihim=pd.to_datetime(gfe1.index[-1]).day
    if tarihim>24:
        tarihim=24
    if tarihim<10:
        tarihim="0"+str(tarihim)

    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=30)).strftime("%Y-%m")
    harcama_grupları=pd.read_csv("harcama_grupları.csv",index_col=0)

    harcama_grupları.index=pd.to_datetime(harcama_grupları.index)
    harcama_grupları=harcama_grupları.drop("2024-12-31",axis=0)
   
    harcama_grupları=harcama_grupları.sort_index()
    ana = harcama_grupları.columns
    selected_group = st.sidebar.selectbox("Harcama Grubu Seçin:", ana)

    selected_group_data=harcama_grupları[selected_group]

    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Endeksi</h2>", unsafe_allow_html=True)

    first_date = selected_group_data.index[0].strftime("%d.%m.%Y")  # İlk tarihi formatlama
    last_date = selected_group_data.index[-1].strftime("%d.%m.%Y")  # Son tarihi formatlama
  

        # Değişim yüzdesini hesaplama
    first_value = 100
    last_value = selected_group_data.iloc[-1] # Son değer
    change_percent = ((last_value - first_value) / first_value) * 100  # Yüzde değişim
    change_percent = round(change_percent, 2)

    aylık=((hareketli_aylik_ortalama(harcama_grupları[selected_group])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(harcama_grupları[selected_group])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-{tarihim}"])-1)*100
    aylık=aylık.round(2)
    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                31.12.2024 - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                Mayıs Değişimi: <span style='color:red;'>% {aylık}</span><br>

            </h3>
            """, unsafe_allow_html=True)
    


    figgharcama= go.Figure()
    
    figgharcama.add_trace(go.Scatter(
                x=selected_group_data.index,
                y=selected_group_data.values,
                mode='lines',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
        



    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgharcama.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index[::5],  # Original datetime index
                ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.plotly_chart(figgharcama)

    tüfe=pd.read_csv("gruplar_int.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    tüfe=tüfe.sort_index()
    harcama_grupları["TÜFE"]=tüfe["TÜFE"]

    fig30 = go.Figure()
    fig30.add_trace(go.Scatter(
                x=selected_group_data.pct_change(30).dropna().index,
                y=(selected_group_data.pct_change(30).dropna()*100).values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
    
    fig30.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index[::5],  # Original datetime index
                ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} 30 Günlük Artış Hızı (%)</h2>", unsafe_allow_html=True)

    st.plotly_chart(fig30)

    

    

    harcama_grupları.index=pd.to_datetime(harcama_grupları.index)
    harcama_grupları=harcama_grupları.sort_index()
    harcama_grupları_aylık=pd.DataFrame(columns=harcama_grupları.columns)
    for col in harcama_grupları.columns:
        cari=hareketli_aylik_ortalama(harcama_grupları[col])["Aylık Ortalama"].fillna(method="ffill")
        harcama_grupları_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
        carim=hareketli_aylik_ortalama(harcama_grupları[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
        hareketliartıs=aylik_degisim_serisi(harcama_grupları[col])

        harcama_grupları_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
        harcama_grupları_aylık=pd.DataFrame(harcama_grupları_aylık)
    harcama_grupları_aylık["Tarih"]=(harcama_grupları_aylık.index.strftime("%Y-%m"))
  

    
    import streamlit as st

    # Başlığın font büyüklüğünü artırma
    st.markdown(
        """
        <style>
        label[for="Tarih Seçin:"] {
            font-size: 20px !important;
            font-weight: bold;
        }
        div[data-baseweb="select"] > div {
            font-size: 18px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Selectbox başlığını ayrı bir markdown ile büyütme
    st.markdown('<p style="font-size:20px; font-weight:bold;">Tarih Seçin:</p>', unsafe_allow_html=True)

    # Selectbox
    selected_tarih = st.selectbox("", harcama_grupları_aylık["Tarih"].values[::-1])



    harcama_artıs=harcama_grupları_aylık[harcama_grupları_aylık["Tarih"]==selected_tarih].iloc[0]





    harcama_artıs=harcama_artıs.drop("Tarih",axis=0).sort_values()


    colors = ['red' if label == 'TÜFE' else 'blue' for label in harcama_artıs.index]

    # İlk 42 karakteri almak için index etiketlerini kısaltma
    shortened_index = [label[:42] for label in harcama_artıs.index]

    # Grafik oluşturma
    figartıs = go.Figure()

    # Verileri ekleme
    figartıs.add_trace(go.Bar(
        y=shortened_index,  # Kısaltılmış index etiketleri
        x=harcama_artıs.values,
        orientation='h', 
        marker=dict(color=colors),
        name=f'Artış Oranı',
    ))

    # Başlık ve etiketler
    figartıs.update_layout(
        title={
        'text': "Web-TÜFE Artış Oranları",  # Başlık metni
        'x': 0.5,  # Ortalamak için 0.5
        'xanchor': 'center',  # Yatay hizalama
        'yanchor': 'top'  # Dikey hizalama
    },
        xaxis_title='Artış Oranı (%)',
        yaxis_title='Grup',
        xaxis=dict(tickformat='.2f'),
        bargap=0.5,  # Çubuklar arasındaki boşluk
        height=2400,  # Grafik boyutunu artırma
        font=dict(family="Arial Black", size=14, color="black"),  # Yazı tipi ve kalınlık
        yaxis=dict(
            tickfont=dict(family="Arial Black", size=14, color="black"),  # Y eksenindeki etiketlerin rengi
            tickmode='array',  # Manuel olarak etiketleri belirlemek için
            tickvals=list(range(len(harcama_artıs.index))),  # Her bir index için bir yer belirle
            ticktext=shortened_index  # Kısaltılmış index etiketleri
        )
    )

    # Etiket ekleme
    for i, value in enumerate(harcama_artıs.values):
        if value >= 0:
            # Pozitif değerler sol tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='left', 
                xanchor='left', 
                yanchor='middle'
            )
        else:
            # Negatif değerler sağ tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='right', 
                xanchor='right', 
                yanchor='middle'
            )




    st.markdown(f"<h2 style='text-align:left; color:black;'>Web-TÜFE Harcama Grupları Artış Oranları</h2>", unsafe_allow_html=True)
    st.plotly_chart(figartıs)

if page=="Özel Kapsamlı Göstergeler":
    def aylik_degisim_serisi(ts: pd.Series) -> pd.Series:
        ts = ts.sort_index()
        aylik_degisim = []

        for tarih in ts.index:
            gun = tarih.day
            ay = tarih.month
            yil = tarih.year

            # Bu ay ve geçen ay için veri
            bu_ay = ts[(ts.index.year == yil) & (ts.index.month == ay)]
            if ay == 1:
                onceki_ay = ts[(ts.index.year == yil - 1) & (ts.index.month == 12)]
            else:
                onceki_ay = ts[(ts.index.year == yil) & (ts.index.month == ay - 1)]

            if gun <= 24:
                ort_bu = bu_ay.iloc[:gun].mean()
                ort_onceki = onceki_ay.iloc[:gun].mean()

                if pd.notna(ort_bu) and pd.notna(ort_onceki) and ort_onceki != 0:
                    oran = (ort_bu / ort_onceki) - 1
                    aylik_degisim.append(oran*100)
                else:
                    aylik_degisim.append(None)
            else:
                try:
                    tarih_24 = bu_ay.index[23]
                    oran_24 = aylik_degisim[ts.index.get_loc(tarih_24)]
                    aylik_degisim.append(oran_24)
                except:
                    aylik_degisim.append(None)

        return pd.Series(aylik_degisim[-gun:], index=ts.index[-gun:])

    from datetime import datetime,timedelta
    import pytz
    tüfe=pd.read_csv("tüfe.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    gfe1=tüfe.copy()
    gfe1["Date"]=pd.to_datetime(gfe1.index)
    gfe1["Ay"]=gfe1["Date"].dt.month
    gfe1["Yıl"]=gfe1["Date"].dt.year    
    month = gfe1["Ay"].iloc[-1]
    year=gfe1["Yıl"].iloc[-1] 
    oncekiyear=gfe1["Yıl"].iloc[-1] 
    tarihim=pd.to_datetime(gfe1.index[-1]).day
    if tarihim>24:
        tarihim=24
    if tarihim<10:
        tarihim="0"+str(tarihim)

    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=30)).strftime("%Y-%m")

    tüfe=pd.read_csv("gruplar_int.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    özelgöstergeler=pd.read_csv("özelgöstergeler.csv",index_col=0)
    özelgöstergeler.index=pd.to_datetime(özelgöstergeler.index)
    özelgöstergeler=özelgöstergeler.rename(columns={"Alkollü içecekler, tütün ve altın":"Altın"})
    özelgöstergeler=özelgöstergeler.rename(columns={"İşlenmemiş Gıda":"İşlenmemiş gıda"})
    gösterge=özelgöstergeler.columns.values

    selected_group = st.sidebar.selectbox("Özel Kapsamlı Gösterge Seçin:", gösterge)

    selected_group_data=özelgöstergeler[selected_group]

    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Endeksi</h2>", unsafe_allow_html=True)

    first_date = selected_group_data.index[0].strftime("%d.%m.%Y")  # İlk tarihi formatlama
    last_date = selected_group_data.index[-1].strftime("%d.%m.%Y")  # Son tarihi formatlama
  

        # Değişim yüzdesini hesaplama
    first_value = 100
    last_value = selected_group_data.iloc[-1] # Son değer
    change_percent = ((last_value - first_value) / first_value) * 100  # Yüzde değişim
    change_percent = round(change_percent, 2)
    
    aylık=((hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-{tarihim}"])-1)*100
    aylık=aylık.round(2)

    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                01.01.2025 - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                Mayıs Değişimi: <span style='color:red;'>% {aylık}</span><br>

            </h3>
            """, unsafe_allow_html=True)
    

    


    figgösterge=go.Figure()
    
    figgösterge.add_trace(go.Scatter(
                x=selected_group_data.index,
                y=selected_group_data.values,
                mode='lines',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
        



    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgösterge.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index[::5],  # Original datetime index
                ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.plotly_chart(figgösterge)

    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=30)).strftime("%Y-%m")
    cari=hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
    hareketliartıs=aylik_degisim_serisi(selected_group_data)


    figgartıs = go.Figure()
    figgartıs.add_trace(go.Scatter(
                x=hareketliartıs.index,
                y=hareketliartıs.values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
    
    figgartıs.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index,  # Original datetime index
                ticktext=selected_group_data.index.strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Aylık Artış Oranı</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 18px; color: black; background-color: #f0f0f0; padding: 15px; border-radius: 5px;">
        Not: Aylık artış oranı mevcut ayın ortalamasının önceki ayın aynı dönemdeki ortalamasına göre değişimi ile hazırlanmıştır.
    </div>
""", unsafe_allow_html=True)
    st.plotly_chart(figgartıs)




    fig30 = go.Figure()
    fig30.add_trace(go.Scatter(
                x=selected_group_data.pct_change(30).dropna().index,
                y=(selected_group_data.pct_change(30).dropna()*100).values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
    
    fig30.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index[::5],  # Original datetime index
                ticktext=selected_group_data.index[::5].strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black"),
                tickangle=45
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} 30 Günlük Artış Hızı (%)</h2>", unsafe_allow_html=True)
  
    st.plotly_chart(fig30)




    data=pd.read_csv("tüiközelgöstergeler.csv",index_col=0)
    data.index=pd.to_datetime(data.index)

    data2=pd.read_excel("harcama gruplarina gore endeks sonuclari.xlsx")
    data2=data2.iloc[1:,:]
    data2.columns=data2.iloc[1,:]

    data2=data2.drop(1,axis=0)
    data2=data2.drop(2,axis=0)
    data2=data2.iloc[1:,3:]
    data2=data2.set_index(pd.date_range(start="2005-01-31",freq="M",periods=len(data2)))
    data2=data2.pct_change().dropna().loc["2025-02":]*100
    
    
    özelgöstergeler.index=pd.to_datetime(özelgöstergeler.index)
    özelgöstergeler=özelgöstergeler.sort_index()
    gruplar_aylık=pd.DataFrame(columns=özelgöstergeler.columns)
    for col in özelgöstergeler.columns:
        cari=hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill")
        gruplar_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
        carim=hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
        hareketliartıs=aylik_degisim_serisi(selected_group_data)

        gruplar_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
        gruplar_aylık=pd.DataFrame(gruplar_aylık)
    gruplar_aylık=np.round(gruplar_aylık,2)

    gruplar_aylık["Tarih"]=(gruplar_aylık.index)
    cols=["Tarih"]
    cols.extend(özelgöstergeler.columns)
    gruplar_aylık=gruplar_aylık[cols]
    gruplar_aylık=gruplar_aylık.reset_index(drop=True)
    gruplar_aylık=gruplar_aylık.set_index("Tarih")
    tüikdata=pd.DataFrame(index=gruplar_aylık.index)




    tüikdata["Web-TÜFE"]=gruplar_aylık[selected_group]
    tüikdata["TÜİK"]=data[selected_group]
    tüikdata=tüikdata.round(2)
    if selected_group=="Altın":
        st.markdown("""
    <div style="font-size: 18px; color: black; background-color: #f0f0f0; padding: 15px; border-radius: 5px;">
        Not: Altın endeksi Web-TÜFE'de sadece altını kapsarken TÜİK verisi Mücevherler, saat ve kol saatleri endeksi olarak verilmektedir.
    </div>
""", unsafe_allow_html=True)
        tüikdata["TÜİK"]=data2["Mücevherler, saat ve kol saatleri"]
        tüikdata=tüikdata.round(2)

    figcompana=go.Figure()
    figcompana.add_trace(go.Bar(
            x=tüikdata.index.strftime("%Y-%m"),
            y=tüikdata["Web-TÜFE"],
            name="Web-TÜFE",
            marker=dict(color='blue'),
            text=tüikdata["Web-TÜFE"],  # Değerleri göster
            textposition='outside',
            hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>',  # Tüm değerler barların üstünde olacak
            textfont=dict(
                color='black',
                size=13,
                family='Arial Black'  # Font Arial Black
            )
        ))

    figcompana.add_trace(go.Bar(
        x=tüikdata.index.strftime("%Y-%m"),
        y=tüikdata["TÜİK"],
        name="TÜİK",
        marker=dict(color='red'),
        text=tüikdata["TÜİK"],  # Değerleri göster
        textposition='outside',
        hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>',  # Tüm değerler barların üstünde olacak
        textfont=dict(
            color='black',
            size=13,
            family='Arial Black'  # Font Arial Black
        )
    ))
    tickvals = tüikdata.index
    ticktext = tickvals.strftime("%Y-%m")
    figcompana.update_layout(
        barmode='group',  # Barlar gruplanmış şekilde gösterilir
        title=dict(
            text=f"{selected_group} TÜİK ve Web-TÜFE Aylık Değişim Karşılaştırması",
            font=dict(size=18, color="black", family="Arial Black")
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=tüikdata.index.strftime("%Y-%m"),
            ticktext=ticktext,
            tickangle=-0,
            tickfont=dict(size=15, color="black", family="Arial Black")
        ),
        yaxis=dict(
            title='Aylık Değişim (%)',
            tickfont=dict(size=15, color="black", family="Arial Black")            ),
        legend=dict(
            x=1,
            y=1,
            xanchor='right',
            yanchor='top',
            font=dict(size=12, color="black", family="Arial Black"),
            bgcolor='rgba(255,255,255,0.8)',  # Arka plan rengi (şeffaf beyaz)
            bordercolor='black',
            borderwidth=1
        ),
        bargap=0.2,  # Barlar arası boşluk
        bargroupgap=0.1,  # Gruplar arası boşluk
        margin=dict(t=50, b=50, l=50, r=50)  # Kenar boşlukları
    )
    
    st.plotly_chart(figcompana)


    
        

    

    
   
   


   
    gösterge_artıs=pd.read_csv("özelgöstergeler.csv",index_col=0)
    gösterge_artıs.index=pd.to_datetime(gösterge_artıs.index)
    gösterge_artıs=gösterge_artıs.rename(columns={"Alkollü içecekler, tütün ve altın":"Altın"})
    gösterge_artıs=gösterge_artıs.rename(columns={"İşlenmemiş Gıda":"İşlenmemiş gıda"})
    gösterge_artıs1=pd.Series(index=gösterge_artıs.columns.values)
    for col in gösterge_artıs.columns:
        gösterge_artıs1.loc[col]=((hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-{tarihim}"])-1)*100
    gösterge_artıs1.loc["TÜFE"]=((hareketli_aylik_ortalama(tüfe["TÜFE"])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(tüfe["TÜFE"])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-{tarihim}"])-1)*100
    gösterge_artıs1=gösterge_artıs1.sort_values()

    colors = ['red' if label == 'TÜFE' else 'blue' for label in gösterge_artıs1.index]

    # İlk 42 karakteri almak için index etiketlerini kısaltma
    shortened_index = [label[:42] for label in gösterge_artıs1.index]

    # Grafik oluşturma
    figartıs = go.Figure()

    # Verileri ekleme
    figartıs.add_trace(go.Bar(
        y=shortened_index,  # Kısaltılmış index etiketleri
        x=gösterge_artıs1.values,
        orientation='h', 
        marker=dict(color=colors),
        name=f'Artış Oranı',
    ))

    # Başlık ve etiketler
    figartıs.update_layout(
        title={
        'text': "Web-TÜFE Artış Oranları",  # Başlık metni
        'x': 0.5,  # Ortalamak için 0.5
        'xanchor': 'center',  # Yatay hizalama
        'yanchor': 'top'  # Dikey hizalama
    },
        xaxis_title='Artış Oranı (%)',
        yaxis_title='Grup',
        xaxis=dict(tickformat='.2f'),
        bargap=0.5,  # Çubuklar arasındaki boşluk
        height=1200,  # Grafik boyutunu artırma
        font=dict(family="Arial Black", size=14, color="black"),  # Yazı tipi ve kalınlık
        yaxis=dict(
            tickfont=dict(family="Arial Black", size=14, color="black"),  # Y eksenindeki etiketlerin rengi
            tickmode='array',  # Manuel olarak etiketleri belirlemek için
            tickvals=list(range(len(gösterge_artıs1.index))),  # Her bir index için bir yer belirle
            ticktext=shortened_index  # Kısaltılmış index etiketleri
        )
    )

    # Etiket ekleme
    for i, value in enumerate(gösterge_artıs1.values):
        if value >= 0:
            # Pozitif değerler sol tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='left', 
                xanchor='left', 
                yanchor='middle'
            )
        else:
            # Negatif değerler sağ tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='right', 
                xanchor='right', 
                yanchor='middle'
            )


    st.markdown(f"<h2 style='text-align:left; color:black;'>Özel Kapsamlı TÜFE Göstergeleri Artış Oranları</h2>", unsafe_allow_html=True)
    st.plotly_chart(figartıs)
if page=="Mevsimsellikten Arındırılmış Göstergeler":

        from datetime import datetime
        bugün=datetime.now().day

   
   




    
    


    
        st.markdown(
        f"""
        <h2 style='text-align:left; color:black;'>
            Mevsimsellikten Arındırılmış Özel Kapsamlı Göstergeler Mart Ayı Artış Oranları
        </h2>
        <p style='text-align:left; color:black; font-size:16px; font:Arial Black'>
        </p>
        """,
        unsafe_allow_html=True
    )


        ma_gösterge=pd.read_csv("özelgöstergeler_int.csv",index_col=0)
        tüfe=pd.read_csv("gruplar_int.csv",index_col=0)
        tüik=pd.read_csv("mevsimselliktenarındırılmışgöstergeler.csv",index_col=0)


        gösterge_artıs_ma=((tüik.iloc[-1]/tüik.iloc[-2])-1)*100
        gösterge_artıs_ma=gösterge_artıs_ma.sort_index()

        

        gösterge_artıs_ham=((ma_gösterge[gösterge_artıs_ma.drop("TÜFE").index.values].iloc[-1]/ma_gösterge[gösterge_artıs_ma.drop("TÜFE").index.values].iloc[0])-1)*100
        gösterge_artıs_ham["TÜFE"]=((tüfe.iloc[-1,0]/tüfe.iloc[0,0])-1)*100
        gösterge_artıs_ham=gösterge_artıs_ham.sort_index()


                
        index_labels = [f"{i}" for i in gösterge_artıs_ham.index]  # Örnek index etiketleri

        colors = ['red' if label == 'TÜFE' else 'blue' for label in gösterge_artıs_ham.index]

        text_colors_mevsim = ["red" if label == "TÜFE" else "black" for label in index_labels]
        text_colors_ham = ["red" if label == "TÜFE" else "black" for label in index_labels]

        y_tick_text = [
    f"<span style='color:red;'>{label}</span>" if label == "TÜFE" else label
    for label in index_labels
]


        max_ham=max(gösterge_artıs_ma)
        min_ham=min(gösterge_artıs_ham)

        max_ma=max(gösterge_artıs_ma)
        min_ma=min(gösterge_artıs_ma)

        # Grafik oluşturma
        fig = go.Figure()

        # Mevsimsellikten Arındırılmış Veriler
        fig.add_trace(go.Bar(
        y=index_labels,
        x=gösterge_artıs_ma,
        orientation='h',
        name="Mevsimsellikten Arındırılmış",
        marker=dict(color='blue'),
        text=[
            f"{val:.2f}%" for val in gösterge_artıs_ma
        ],
        textposition=[
            "inside" if val>(max_ma-2) or val <( min_ma+2) else "outside"
            for val in gösterge_artıs_ma.values
        ],
        textfont=dict(size=14, family="Arial Black", color="black"),
        insidetextfont=dict(size=14, family="Arial Black", color="black")
    ))

    # Ham Veriler
        fig.add_trace(go.Bar(
            y=index_labels,
            x=gösterge_artıs_ham,
            orientation='h',
            name="Ham",
            marker=dict(color='orange'),
            text=[
                f"{val:.2f}%" for val in gösterge_artıs_ham
            ],
            textposition=[
                "inside" if val > (max_ma - 2) or val < (min_ma + 2) else "outside"
                for val in gösterge_artıs_ham.values
            ],
            textfont=dict(size=14, family="Arial Black", color="black"),
            insidetextfont=dict(size=14, family="Arial Black", color="black")
        ))

        fig.update_traces(cliponaxis=False)

        # Keep all text size consistent
        fig.update_layout(uniformtext=dict(mode="show", minsize=16))

        # Grafik düzenlemeleri
        fig.update_layout(
  
    xaxis=dict(
        title="Artış Oranı (%)",
        titlefont=dict(size=16, family="Arial Black", color="black"),  # X eksen etiketi
        tickfont=dict(size=14, family="Arial Black", color="black")   # X ekseni değerleri
    ),
    yaxis=dict(
        title="Gruplar",
        titlefont=dict(size=16, family="Arial Black", color="black"),  # Y eksen etiketi
        ticktext=y_tick_text,  # Renkli Y ekseni etiketleri
        tickvals=index_labels,  # Etiket pozisyonları
        tickfont=dict(size=14, family="Arial Black", color="black")   # Varsayılan Y ekseni değerleri
    ),
    barmode='group',  # Çubukları yan yana yerleştir
    height=1200,
    width=2000,
    margin=dict(l=150, r=20, t=80, b=40),
    legend=dict(
        title=dict(
            text="Veri Türü",
            font=dict(size=16, family="Arial Black", color="black")  # Efsane başlığı
        ),
        font=dict(size=14, family="Arial Black", color="black"),  # Efsane metinleri
        orientation="v",  # Legend dikey olarak yerleştirilir
        x=1.02,  # Sağ kenara yakın
        y=1,  # Üst kenara yakın
        xanchor="left",  # X ekseninde sol hizalama
        yanchor="top"    # Y ekseninde üst hizalama
    )
)
  
        

        # Streamlit'te grafiği görüntüleme
        st.plotly_chart(fig)
    
        

if page=="Madde Endeksleri":
    def aylik_degisim_serisi(ts: pd.Series) -> pd.Series:
        ts = ts.sort_index()
        aylik_degisim = []

        for tarih in ts.index:
            gun = tarih.day
            ay = tarih.month
            yil = tarih.year

            # Bu ay ve geçen ay için veri
            bu_ay = ts[(ts.index.year == yil) & (ts.index.month == ay)]
            if ay == 1:
                onceki_ay = ts[(ts.index.year == yil - 1) & (ts.index.month == 12)]
            else:
                onceki_ay = ts[(ts.index.year == yil) & (ts.index.month == ay - 1)]

            if gun <= 24:
                ort_bu = bu_ay.iloc[:gun].mean()
                ort_onceki = onceki_ay.iloc[:gun].mean()

                if pd.notna(ort_bu) and pd.notna(ort_onceki) and ort_onceki != 0:
                    oran = (ort_bu / ort_onceki) - 1
                    aylik_degisim.append(oran*100)
                else:
                    aylik_degisim.append(None)
            else:
                try:
                    tarih_24 = bu_ay.index[23]
                    oran_24 = aylik_degisim[ts.index.get_loc(tarih_24)]
                    aylik_degisim.append(oran_24)
                except:
                    aylik_degisim.append(None)

        return pd.Series(aylik_degisim[-gun:], index=ts.index[-gun:])

    from datetime import datetime,timedelta
    import pytz
    tüfe=pd.read_csv("tüfe.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    gfe1=tüfe.copy()
    gfe1["Date"]=pd.to_datetime(gfe1.index)
    gfe1["Ay"]=gfe1["Date"].dt.month
    gfe1["Yıl"]=gfe1["Date"].dt.year    
    month = gfe1["Ay"].iloc[-1]
    year=gfe1["Yıl"].iloc[-1] 
    oncekiyear=gfe1["Yıl"].iloc[-1] 
    tarihim=pd.to_datetime(gfe1.index[-1]).day
    if tarihim>24:
        tarihim=24
    if tarihim<10:
        tarihim="0"+str(tarihim)

    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=30)).strftime("%Y-%m")
    ürüngrupları=pd.read_csv("harcamaürünleri1.csv",index_col=0)

    endeksler=pd.read_csv("endeksler_int.csv",index_col=0)

    harcamagrupları=pd.read_csv("harcama_grupları.csv",index_col=0)

    anagruplar=pd.read_csv("gruplar_int.csv",index_col=0)

    

    selected_anagrup=st.sidebar.selectbox("Ana Grup Seçin:", ürüngrupları["Ana Grup"].unique())



    filtered_anagrup=ürüngrupları[ürüngrupları["Ana Grup"]==selected_anagrup]

    maddeler=filtered_anagrup["Ürün"].values

    

    endeksler=pd.read_csv("endeksler_int.csv",index_col=0)
    endeksler.index=pd.to_datetime(endeksler.index)
    endeksler=endeksler.sort_index()

    
    endeksler=endeksler[ürüngrupları[ürüngrupları["Ana Grup"]==selected_anagrup]["Ürün"].values]
    gruplar=pd.read_csv("gruplar_int.csv",index_col=0)
    gruplar.index=pd.to_datetime(gruplar.index)
    endeksler[selected_anagrup]=gruplar[selected_anagrup]
    
    
    maddeler_aylık=pd.DataFrame(columns=endeksler.columns)
    for col in endeksler.columns:
        selected_group_data=endeksler[col]
        cari=hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill")
        maddeler_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
        carim=hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
        hareketliartıs=aylik_degisim_serisi(selected_group_data)

        maddeler_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
        maddeler_aylık=pd.DataFrame(maddeler_aylık)
    maddeler_aylık["Tarih"]=(maddeler_aylık.index.strftime("%Y-%m"))

    import streamlit as st

    # Başlığın font büyüklüğünü artırma
    st.markdown(
        """
        <style>
        label[for="Tarih Seçin:"] {
            font-size: 20px !important;
            font-weight: bold;
        }
        div[data-baseweb="select"] > div {
            font-size: 18px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Selectbox başlığını ayrı bir markdown ile büyütme
    st.markdown('<p style="font-size:20px; font-weight:bold;">Tarih Seçin:</p>', unsafe_allow_html=True)

    # Selectbox
    selected_tarih = st.selectbox("", maddeler_aylık["Tarih"].values[::-1])



    maddeartıslar=maddeler_aylık[maddeler_aylık["Tarih"]==selected_tarih].iloc[0]

    maddeartıslar=maddeartıslar.drop("Tarih",axis=0).sort_values()

    colors = ['red' if label == selected_anagrup else 'blue' for label in maddeartıslar.index]

    # İlk 42 karakteri almak için index etiketlerini kısaltma
    shortened_index = [label[:42] for label in maddeartıslar.index]

    # Grafik oluşturma
    figartıs = go.Figure()

    # Verileri ekleme
    figartıs.add_trace(go.Bar(
        y=shortened_index,  # Kısaltılmış index etiketleri
        x=maddeartıslar.values,
        orientation='h', 
        marker=dict(color=colors),
        name=f'Artış Oranı',
    ))

    if selected_anagrup=="Gıda ve alkolsüz içecekler":

 
        figartıs.update_layout(
            title={
            'text': "Web-TÜFE Artış Oranları",  # Başlık metni
            'x': 0.5,  # Ortalamak için 0.5
            'xanchor': 'center',  # Yatay hizalama
            'yanchor': 'top'  # Dikey hizalama
        },
            xaxis_title='Artış Oranı (%)',
            yaxis_title='Grup',
            xaxis=dict(tickformat='.2f'),
            bargap=0.5,  # Çubuklar arasındaki boşluk
            height=max(600,len(filtered_anagrup)*20),  # Grafik boyutunu artırma
            font=dict(family="Arial Black", size=14, color="black"),  # Yazı tipi ve kalınlık
            yaxis=dict(
                tickfont=dict(family="Arial Black", size=14, color="black"),  # Y eksenindeki etiketlerin rengi
                tickmode='array',  # Manuel olarak etiketleri belirlemek için
                tickvals=list(range(len(maddeartıslar.index))),  # Her bir index için bir yer belirle
                ticktext=shortened_index  # Kısaltılmış index etiketleri
            )
        )
    else:

        figartıs.update_layout(
            title={
            'text': f"{selected_anagrup} Maddeleri Artış Oranları",  # Başlık metni
            'x': 0.5,  # Ortalamak için 0.5
            'xanchor': 'center',  # Yatay hizalama
            'yanchor': 'top'  # Dikey hizalama
        },
            xaxis_title='Artış Oranı (%)',
            yaxis_title='Grup',
            xaxis=dict(tickformat='.2f'),
            bargap=0.5,  # Çubuklar arasındaki boşluk
            height=max(600,len(filtered_anagrup)*20),  # Grafik boyutunu artırma
            font=dict(family="Arial Black", size=14, color="black"),  # Yazı tipi ve kalınlık
            yaxis=dict(
                tickfont=dict(family="Arial Black", size=14, color="black"),  # Y eksenindeki etiketlerin rengi
                tickmode='array',  # Manuel olarak etiketleri belirlemek için
                tickvals=list(range(len(maddeartıslar.index))),  # Her bir index için bir yer belirle
                ticktext=shortened_index  # Kısaltılmış index etiketleri
            )
        )
        

    # Etiket ekleme
    for i, value in enumerate(maddeartıslar.values):
        if value >= 0:
            # Pozitif değerler sol tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='left', 
                xanchor='left', 
                yanchor='middle'
            )
        else:
            # Negatif değerler sağ tarafta
            figartıs.add_annotation(
                x=value, 
                y=shortened_index[i], 
                text=f"{value:.2f}%", 
                showarrow=False, 
                font=dict(size=14, family="Arial Black"),  # Etiketler için yazı tipi
                align='right', 
                xanchor='right', 
                yanchor='middle'
            )




    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_anagrup} Maddeleri Artış Oranları</h2>", unsafe_allow_html=True)
    st.plotly_chart(figartıs)









