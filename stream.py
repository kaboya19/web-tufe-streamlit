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
    "X": {"url": "https://x.com/webtufe", "color": "#000000"},
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



page=st.sidebar.radio("Sekmeler",tabs)

social_media_icons = SocialMediaIcons(
        [link["url"] for link in social_media_links.values()],
        colors=[link["color"] for link in social_media_links.values()]
    )
social_media_icons.render(sidebar=True)

df = pd.read_csv("endeksler.csv",index_col=0)
degisimler = []
for col in df.columns:
    if col != "Tarih":
        try:
            d1 = df[col].iloc[-1].values[0]
            d2 = df[col].iloc[-2].values[0]
            fark = ((d1 - d2) / d2) * 100
            degisimler.append(f"{col}:%{fark:+.1f}")
        except:
            pass  # eksik veri varsa atla

# Kayan yazı oluştur
kayan_yazi = "  Günlük Değişimler  " + "  ".join(degisimler)

# HTML + CSS ile marquee efekti
st.markdown(f"""
    <div style="background-color:#f0f0f0;padding:10px;">
        <marquee behavior="scroll" direction="left" scrollamount="6" loop="infinite" style="font-size:18px; color:darkblue;">
            {kayan_yazi}
        </marquee>
    </div>
""", unsafe_allow_html=True)

if page=="Bültenler":
    import streamlit as st
    from PIL import Image


    # Tab for selecting the bulletin
    tab = st.selectbox("Bülten Seçin", ["Mart 2025","Şubat 2025"])

    # Check if the user selects February 2025
    if tab == "Mart 2025":
        # Title
        st.markdown("<h2 style='color:black; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Mart 2025 Bülteni</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:red; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Martta %4,12 arttı</h3>", unsafe_allow_html=True)

        # First image
        image1 = Image.open("anagruplar.png")
        st.image(image1, caption="En çok artış ve düşüş yaşanan maddeler")

        # Paragraphs and next images
        st.write("Web-Tüketici Fiyat Endeksi Martta %4,12 artış kaydederken mevsimsellikten arındırılmış artış %4,46 oldu.")
        st.write("En çok artış ve düşüş yaşanan maddeler:")
        image2 = Image.open("maddeler.png")
        st.image(image2, caption="En çok artış ve düşüş yaşanan temel başlıklar")

        st.write("En çok artış ve düşüş yaşanan temel başlıklar:")
        image3 = Image.open("temelbaşlıklar.png")
        st.image(image3, caption="Özel Kapsamlı TÜFE Göstergeleri")

        st.write("Özel Kapsamlı TÜFE Göstergeleri:")
        image4 = Image.open("özelgöstergeler.png")
        st.image(image4, caption="Özel Kapsamlı Göstergeler aylık artış oranları")

        st.write("Özel Kapsamlı Göstergeler aylık artış oranları:")
        image5 = Image.open("özelgöstergelerartış.png")
        st.image(image5, caption="Ana gruplara ait artış oranları")

        # Display remaining images
        images = [
            ("eveşyası.png", "Ev Eşyası"),
            ("eğitim.png", "Eğitim"),
            ("eğlence.png", "Eğlence"),
            ("Giyim ve ayakkabı.png", "Giyim ve Ayakkabı"),
            ("Gıda ve alkolsüz içecekler.png", "Gıda ve Alkolsüz İçecekler"),
            ("Haberleşme.png", "Haberleşme"),
            ("Konut.png", "Konut"),
            ("Lokanta ve oteller.png", "Lokanta ve Oteller"),
            ("Ulaştırma.png", "Ulaştırma"),
            ("Çeşitli mal ve hizmetler.png", "Çeşitli Mal ve Hizmetler"),
            ("Giyim ve ayakkabı.png", "Giyim ve Ayakkabı")
        ]

        for image_path, caption in images:
            image = Image.open(image_path)
            st.image(image, caption=caption)

        # Seçilmiş maddelere ait ortalama fiyatlar
        st.write("Seçilmiş maddelere ait ortalama fiyatlar:")
        image17 = Image.open("fiyatlar.png")
        

        # Final section with trend and link
        st.write("Mevsimsellikten arındırılmış ana eğilimlere bakıldığında medyan artış %3,12 olmuştur.")
        st.write("SATRIM(Mevsimsel Düzeltilmiş Budanmış Enflasyon) göstergesi ise %3,36 artmıştır.")
        image18 = Image.open("eğilim.png")
        st.image(image18, caption="Mevsimsellikten Arındırılmış Eğilim")


        # Footer
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
            <small>
                *Bu bültenin bir sonraki yayınlanma tarihi 24 Nisan 2025'tir. Burada yer alan bilgi ve analizler tamamen kişisel çalışma olup kesin bir doğruluk içermemekte ve yatırım tavsiyesi içermemektedir.*<br>
                *TÜİK’in hesaplamasıyla uyumlu olması açısından ayın ilk 24 günündeki veriler dikkate alınmıştır.*
            </small>
        """, unsafe_allow_html=True)

        st.markdown("<p><strong>Hazırlayan: Bora Kaya</strong></p>", unsafe_allow_html=True)
        st.markdown("<p>Web-TÜFE Twitter: <a href='https://x.com/webtufe'>https://x.com/webtufe</a></p>", unsafe_allow_html=True)
        st.markdown("<p>Linkedin: <a href='https://www.linkedin.com/in/bora-kaya/'>https://www.linkedin.com/in/bora-kaya/</a></p>", unsafe_allow_html=True)
    if tab == "Şubat 2025":
        # Title
        st.markdown("<h2 style='color:black; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Şubat 2025 Bülteni</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:red; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Şubatta %3,56 arttı</h3>", unsafe_allow_html=True)

        # First image
        image1 = Image.open("anagruplar.png")
        st.image(image1, caption="En çok artış ve düşüş yaşanan maddeler")

        # Paragraphs and next images
        st.write("Web-Tüketici Fiyat Endeksi Şubatta %3,56 artış kaydederken mevsimsellikten arındırılmış artış %2,91 oldu.")
        st.write("En çok artış ve düşüş yaşanan maddeler:")
        image2 = Image.open("maddeler.png")
        st.image(image2, caption="En çok artış ve düşüş yaşanan temel başlıklar")

        st.write("En çok artış ve düşüş yaşanan temel başlıklar:")
        image3 = Image.open("temelbaşlıklar.png")
        st.image(image3, caption="Özel Kapsamlı TÜFE Göstergeleri")

        st.write("Özel Kapsamlı TÜFE Göstergeleri:")
        image4 = Image.open("özelgöstergeler.png")
        st.image(image4, caption="Özel Kapsamlı Göstergeler aylık artış oranları")

        st.write("Özel Kapsamlı Göstergeler aylık artış oranları:")
        image5 = Image.open("özelgöstergelerartış.png")
        st.image(image5, caption="Ana gruplara ait artış oranları")

        # Display remaining images
        images = [
            ("eveşyası.png", "Ev Eşyası"),
            ("eğitim.png", "Eğitim"),
            ("eğlence.png", "Eğlence"),
            ("Giyim ve ayakkabı.png", "Giyim ve Ayakkabı"),
            ("Gıda ve alkolsüz içecekler.png", "Gıda ve Alkolsüz İçecekler"),
            ("Haberleşme.png", "Haberleşme"),
            ("Konut.png", "Konut"),
            ("Lokanta ve oteller.png", "Lokanta ve Oteller"),
            ("Ulaştırma.png", "Ulaştırma"),
            ("Çeşitli mal ve hizmetler.png", "Çeşitli Mal ve Hizmetler"),
            ("Giyim ve ayakkabı.png", "Giyim ve Ayakkabı")
        ]

        for image_path, caption in images:
            image = Image.open(image_path)
            st.image(image, caption=caption)

        # Seçilmiş maddelere ait ortalama fiyatlar
        st.write("Seçilmiş maddelere ait ortalama fiyatlar:")
        image17 = Image.open("fiyatlar.png")
        st.image(image17, caption="Seçilmiş maddelere ait ortalama fiyatlar")

        # Final section with trend and link
        st.write("Mevsimsellikten arındırılmış ana eğilimlere bakıldığında medyan artış %3,20 olmuştur.")
        st.write("SATRIM(Mevsimsel Düzeltilmiş Budanmış Enflasyon) göstergesi ise %3,29 artmıştır.")
        image18 = Image.open("eğilim.png")
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

    
    
     

    # Başlık
    st.title("Web Tüketici Fiyat Endeksi (Web-TÜFE) Metodoloji Açıklaması")

    # Analitik Çerçeve ve Kapsam
    st.subheader("Analitik Çerçeve ve Kapsam")
    st.write("""
    Web Tüketici Fiyat Endeksinin amacı, TÜFE'de yer alan Alkollü içecekler ve Sağlık grubu dışında kalan ürünlerin günlük değişimini ölçerek enflasyon oranını hesaplamaktır. 
    Alkollü içecekler ve Sağlık grubunun ölçümü web üzerinden yapılamamaktadır.Bu bağlamda bu gruplar dışında yer alan 385 maddenin 325 adedi derlenmektedir.
    TÜİK sepetinin ağırlık bazında %82,6'sı ölçülebilmiştir.
    Bu çerçevede, 31 Aralık 2024 endeksi baz olarak "100" seçilmiştir.Fiyat ölçümü ise 6 Ocak 2025 tarihinde başlamıştır.

    """)

    st.write(
    "Web-TÜFE 20'den fazla veri kaynağından günlük 1 milyonun üzerinde fiyat toplayarak hesaplanmaktadır."
    "Verilerin oluşturulma aşaması şu şekildedir;"
             "1-Sepetin ve madde ağırlıklarının oluşturulması"
             "2-Sepetteki tüm ürünler için fiyat verilerinin toplanması"
             "3-Her bir ürün için günlük ortalama fiyat değişiminin hesaplanması"
             "4-Ürünlerin endeks verilerinin oluşturulması ve endekslerin normalize edilmesi"
             "5-Endeks verilerinden bir üst kırılım olan harcama gruplarının oluşturulması"
             "6-Ağırlıklandırma yapılarak Web-TÜFE verisinin oluşturulması"
             "7-Özel Kapsamlı Gösterge endekslerinin oluşturulması")

    st.write("Endeksin veri kaynakları seçilirken mal fiyatları için online sipariş özelliğinin bulunması,seçilen sitenin Türkiye'nin tamamına hizmetinin bulunması,pazar payının yüksek olması ve örneklem"
    "gücünün yüksek olması gibi kriterler dikkate alınmıştır.")

    st.markdown(f"<h2 style='text-align:left; color:black;'>Ana Grup Ağırlıkları</h2>", unsafe_allow_html=True)
    st.image("ağırlıklar.png")

    ağırlıklar=pd.read_csv("ağırlıklartüfe.csv",index_col=0)
    ağırlıklar=ağırlıklar["Ağırlık"]*100
    ağırlıklar=ağırlıklar.sort_values(ascending=False)
    st.subheader("Madde Ağırlıkları")
    st.dataframe(ağırlıklar)



    # Hesaplama Kuralları
    st.subheader("Hesaplama Kuralları")
    st.image("1.png")
    st.image("2.png")
    st.image("3.png")


    # Mevsimsel Düzeltme
    st.subheader("Mevsimsel Düzeltme")
    st.write("""
    İlk aşamada verilerde mevsimsel düzeltme yapılmayacaktır. Ancak verilerin birikmesiyle ilerleyen dönemlerde, TÜİK’in açıklamış olduğu metodolojiye uygun olarak mevsimsel düzeltme yapılacaktır. 
    Bu sonuçlar web sitesinde ve e-posta aboneliği olan kullanıcılara ayrıca yeni bir endeks olarak bildirilecektir.
    """)

    # Veri Derleme
    st.subheader("Veri Derleme")
    st.write("""
    Toplanan veriler web scraping yöntemiyle Python üzerinden derlenmektedir. Şu an itibariyle her gün yaklaşık 1 milyon adet fiyat toplanmaktadır. 

    """)

    # Sonuçların Açıklanması
    st.subheader("Sonuçların Açıklanması")
    st.write("""
    Her ayın 24'inde aylık enflasyon oranları duyurulacaktır. 
    """)

    # İmza
    st.write("""
    ---
    Hazırlayan
    Bora Kaya  
    """)




     

if page=="Tüketici Fiyat Endeksi":

    import streamlit as st

    # HTML etiketini başlık kısmında çalıştırmaya zorlamak
    st.markdown("""
        <script async src="https://www.googletagmanager.com/gtag/js?id=AW-16886391202"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'AW-16886391202');
        </script>
    """, unsafe_allow_html=True)


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


    
    hareketlima = hareketli_aylik_ortalama(selected_group_data.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill")
    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=31)).strftime("%Y-%m")
    cari=hareketli_aylik_ortalama(selected_group_data.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
    hareketliartıs=cari.values/hareketli_aylik_ortalama(selected_group_data.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
    hareketliartıs=pd.Series(hareketliartıs,index=cari.index)
    hareketliartıs=(hareketliartıs-1)*100



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
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    

    

    

        # Grafiği çizme
    figgalt = go.Figure()
    if selected_group!="TÜFE":
        figgalt.add_trace(go.Scatter(
                x=selected_group_data.index[0:],
                y=selected_group_data.iloc[0:,0].values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
        



    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgalt.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index,  # Original datetime index
                ticktext=selected_group_data.index.strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
   
    

  
   
   

      

  
   

   

   
    if selected_group!="TÜFE":

        aylikdegisim=((hareketlima.iloc[-1]/hareketlima.loc[f"{onceki}-24"])-1)*100
        
        aylikdegisim=aylikdegisim.round(2)
        st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                01.01.2025 - {last_date} Değişimi: <span style='color:red;'>%{change_percent}</span><br>
                Nisan Değişimi: <span style='color:red;'>%{aylikdegisim}</span><br>
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
                mode='lines+markers',
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

        
        aylikdegisim=((hareketlima.iloc[-1]/hareketlima.loc[f"{onceki}-24"])-1)*100
        aylikdegisim=aylikdegisim.round(2)
        st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                01.01.2025 - {last_date} Değişimi: <span style='color:red;'>%{change_percent}</span><br>
                Nisan Değişimi: <span style='color:red;'>%{aylikdegisim}</span><br>
            </h3>
            """, unsafe_allow_html=True)
        st.plotly_chart(figgalt)
        degisim=endeksler.pct_change().iloc[-1]*100
        gainers = degisim.sort_values(ascending=False).head(5)
        losers = degisim.sort_values(ascending=True).head(5)
        aylıkdegisim=pd.DataFrame(columns=endeksler.columns)
        for col in endeksler.columns:
            aylıkdegisim[col]=hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill").resample('M').last().pct_change()*100
        aylıkdegisim=aylıkdegisim.iloc[-1]

        gainersaylık = aylıkdegisim.sort_values(ascending=False).head(5)
        losersaylık = aylıkdegisim.sort_values(ascending=True).head(5)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('### **Günün En Çok Artan Ürünleri**')
            for stock, change in gainers.items():
                st.markdown(f"<span style='color:green; font-weight:bold'>{stock} : {change:.2f}%</span>", unsafe_allow_html=True)
            st.markdown('### **Ayın En Çok Artan Ürünleri**')
            for stock, change in gainersaylık.items():
                    st.markdown(f"<span style='color:green; font-weight:bold'>{stock} : {change:.2f}%</span>", unsafe_allow_html=True)

        # En çok düşenler
        with col2:
            st.markdown('### **Günün En Çok Düşen Maddeleri(Veya en az artan)**')
            for stock, change in losers.items():
                st.markdown(f"<span style='color:red; font-weight:bold'>{stock} : {change:.2f}%</span>", unsafe_allow_html=True)
            st.markdown('### **Ayın En Çok Düşen Ürünleri**')
            for stock, change in losersaylık.items():
                    st.markdown(f"<span style='color:red; font-weight:bold'>{stock} : {change:.2f}%</span>", unsafe_allow_html=True)
   
        
      
        
        st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Aylık Artış Oranı</h2>", unsafe_allow_html=True)
        st.markdown("""
    <div style="font-size: 18px; color: black; background-color: #f0f0f0; padding: 15px; border-radius: 5px;">
        Not: Aylık artış oranı mevcut ayın ortalamasının önceki ayın 24 günlük ortalamasına göre değişimi ile hazırlanmıştır.
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
            harcama_artıs.loc[col]=((hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"])-1)*100
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

        def to_excel(df):
            df.index=pd.to_datetime(df.index)
            df.index=df.index.strftime("%Y-%m-%d")
            output = BytesIO()
            # Pandas'ın ExcelWriter fonksiyonunu kullanarak Excel dosyasını oluştur
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=True, sheet_name='Sheet1')  # index=False ile index'i dahil etmiyoruz
                
                # Writer'dan Workbook ve Worksheet nesnelerine erişim
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                
                # Sütun genişliklerini ayarla
                for i, col in enumerate(df.columns):
                    max_length = max(df[col].astype(str).map(len).max(), len(col))  # En uzun değer veya sütun adı uzunluğu
                    worksheet.set_column(i, i, max_length + 20)  # +2 biraz boşluk ekler
            processed_data = output.getvalue()  # Bellekteki dosya verisini al
            return processed_data
        tüfe_excel=to_excel(tüfe)
        st.download_button(
            label="📊 Web-Tüketici Fiyat Endeksi",
            data=tüfe_excel,
            file_name='webtüfe.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        gruplar=pd.read_csv("anagruplar.csv",index_col=0)
        gruplar.index=pd.to_datetime(gruplar.index)
        gruplar_excel=to_excel(gruplar)
        maddeler_excel=to_excel(endeksler)

        harcama_grupları=pd.read_csv("harcama_grupları.csv",index_col=0)
        harcama_grupları.index=pd.to_datetime(harcama_grupları.index)
        harcama_grupları_excel=to_excel(harcama_grupları)

        özelgöstergeler=pd.read_csv("özelgöstergeler.csv",index_col=0)
        özelgöstergeler.index=pd.to_datetime(özelgöstergeler.index)
        özelgöstergeler_excel=to_excel(özelgöstergeler)
        özelgöstergeler=özelgöstergeler.rename(columns={"Alkollü içecekler, tütün ve altın":"Altın"})


        cari=hareketli_aylik_ortalama(tüfe.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill")
        tüfeaylıkdata=cari.resample('M').last().pct_change().loc["2025-02":]*100
        tüfeaylıkdata.iloc[-1]=hareketliartıs.iloc[-1]
        tüfeaylıkdata=pd.DataFrame(tüfeaylıkdata)
        tüfeaylıkdata.columns=["Aylık Artış"]
        tüfeaylıkdata["Tarih"]=pd.to_datetime(tüfeaylıkdata.index)
        tüfeaylıkdata["Tarih"]=tüfeaylıkdata["Tarih"].dt.strftime("%Y-%m")
        tüfeaylıkdata=tüfeaylıkdata.reset_index()
        tüfeaylıkdata=tüfeaylıkdata[["Tarih","Aylık Artış"]]

        cari=hareketli_aylik_ortalama(tüfe.iloc[:,0])["Aylık Ortalama"].fillna(method="ffill")
        tüfeaylıkdata=cari.resample('M').last().pct_change().loc["2025-02":]*100
        tüfeaylıkdata.iloc[-1]=hareketliartıs.iloc[-1]
        tüfeaylıkdata=pd.DataFrame(tüfeaylıkdata)
        tüfeaylıkdata.columns=["Aylık Artış"]
        tüfeaylıkdata["Tarih"]=pd.to_datetime(tüfeaylıkdata.index)
        tüfeaylıkdata["Tarih"]=tüfeaylıkdata["Tarih"].dt.strftime("%Y-%m")
        tüfeaylıkdata=tüfeaylıkdata.reset_index()
        tüfeaylıkdata=tüfeaylıkdata[["Tarih","Aylık Artış"]]

 


        endeksler=pd.read_csv("endeksler.csv",index_col=0)
        endeksler.index=pd.to_datetime(endeksler.index)
        endeksler_aylık=pd.DataFrame(columns=endeksler.columns)
        for col in endeksler.columns:
            cari=hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill")
            endeksler_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
            carim=hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
            hareketliartıs=carim.values/hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
            hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
            hareketliartıs=(hareketliartıs-1)*100
            endeksler_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
            endeksler_aylık=pd.DataFrame(endeksler_aylık)
        endeksler_aylık["Tarih"]=(endeksler_aylık.index.strftime("%Y-%m"))
        cols=["Tarih"]
        cols.extend(endeksler.columns)
        endeksler_aylık=endeksler_aylık[cols]
        endeksler_aylık=endeksler_aylık.reset_index(drop=True)

        harcama_grupları=pd.read_csv("harcama_grupları.csv",index_col=0)
        harcama_grupları.index=pd.to_datetime(harcama_grupları.index)
        harcama_grupları=harcama_grupları.sort_index()
        harcama_grupları_aylık=pd.DataFrame(columns=harcama_grupları.columns)
        for col in harcama_grupları.columns:
            cari=hareketli_aylik_ortalama(harcama_grupları[col])["Aylık Ortalama"].fillna(method="ffill")
            harcama_grupları_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
            carim=hareketli_aylik_ortalama(harcama_grupları[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
            hareketliartıs=carim.values/hareketli_aylik_ortalama(harcama_grupları[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
            hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
            hareketliartıs=(hareketliartıs-1)*100
            harcama_grupları_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
            harcama_grupları_aylık=pd.DataFrame(harcama_grupları_aylık)
        harcama_grupları_aylık["Tarih"]=(harcama_grupları_aylık.index.strftime("%Y-%m"))
        cols=["Tarih"]
        cols.extend(harcama_grupları.columns)
        harcama_grupları_aylık=harcama_grupları_aylık[cols]
        harcama_grupları_aylık=harcama_grupları_aylık.reset_index(drop=True)

        gruplar=pd.read_csv("gruplar_int.csv",index_col=0)
        gruplar.index=pd.to_datetime(gruplar.index)
        gruplar=gruplar.sort_index()
        gruplar_aylık=pd.DataFrame(columns=gruplar.columns)
        for col in gruplar.columns:
            cari=hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill")
            gruplar_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
            carim=hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
            hareketliartıs=carim.values/hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
            hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
            hareketliartıs=(hareketliartıs-1)*100
            gruplar_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
            gruplar_aylık=pd.DataFrame(gruplar_aylık)
        gruplar_aylık=np.round(gruplar_aylık,2)

        gruplar_aylık["Tarih"]=(gruplar_aylık.index.strftime("%Y-%m"))
        cols=["Tarih"]
        cols.extend(gruplar.columns)
        gruplar_aylık=gruplar_aylık[cols]
        gruplar_aylık=gruplar_aylık.reset_index(drop=True)




        özelgöstergeler=pd.read_csv("özelgöstergeler.csv",index_col=0)
        özelgöstergeler.index=pd.to_datetime(özelgöstergeler.index)
        özelgöstergeler=özelgöstergeler.sort_index()
        özelgöstergeler_aylık=pd.DataFrame(columns=özelgöstergeler.columns)
        for col in özelgöstergeler.columns:
            cari=hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill")
            özelgöstergeler_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
            carim=hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
            hareketliartıs=carim.values/hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
            hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
            hareketliartıs=(hareketliartıs-1)*100
            özelgöstergeler_aylık[col].iloc[-1]=hareketliartıs.iloc[-1]
            özelgöstergeler_aylık=pd.DataFrame(özelgöstergeler_aylık)
        özelgöstergeler_aylık=np.round(özelgöstergeler_aylık,2)

        özelgöstergeler_aylık["Tarih"]=(özelgöstergeler_aylık.index.strftime("%Y-%m"))
        cols=["Tarih"]
        cols.extend(özelgöstergeler.columns)
        özelgöstergeler_aylık=özelgöstergeler_aylık[cols]
        özelgöstergeler_aylık=özelgöstergeler_aylık.reset_index(drop=True)




        def to_excel(df):
            output = BytesIO()
            # Pandas'ın ExcelWriter fonksiyonunu kullanarak Excel dosyasını oluştur
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')  # index=False ile index'i dahil etmiyoruz
                
                # Writer'dan Workbook ve Worksheet nesnelerine erişim
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                
                # Sütun genişliklerini ayarla
                for i, col in enumerate(df.columns):
                    max_length = max(df[col].astype(str).map(len).max(), len(col))  # En uzun değer veya sütun adı uzunluğu
                    worksheet.set_column(i, i, max_length + 2)  # +2 biraz boşluk ekler
            processed_data = output.getvalue()  # Bellekteki dosya verisini al
            return processed_data
        
        def to_excel1(df):
            output = BytesIO()
            # Pandas'ın ExcelWriter fonksiyonunu kullanarak Excel dosyasını oluştur
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')  # index=False ile index'i dahil etmiyoruz
                
                # Writer'dan Workbook ve Worksheet nesnelerine erişim
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                
                
            processed_data = output.getvalue()  # Bellekteki dosya verisini al
            return processed_data
        
        ağırlıklar=pd.read_csv("ağırlıklartüfe.csv")
        ağırlıklar["Ağırlık"]=ağırlıklar["Ağırlık"]*100
        ağırlıklar=ağırlıklar[["Ürün","Ağırlık"]]
        ağırlıklar=ağırlıklar.sort_values(by="Ağırlık",ascending=False)
        ağırlıklar=pd.DataFrame(ağırlıklar)

        ağırlıklar=np.round(ağırlıklar,4)
        ağırlıklar1=to_excel(ağırlıklar)


        ağırlıklar=pd.read_csv("ağırlıklartüfe.csv")
        ağırlıklar["Ağırlık"]=ağırlıklar["Ağırlık"]*100
        ağırlıklar=ağırlıklar[["Ürün","Ağırlık","Ana Grup"]]
        ağırlıklar["Ağırlık"]=ağırlıklar.groupby("Ana Grup")["Ağırlık"].transform("sum")
        ağırlıklar=ağırlıklar.sort_values(by="Ağırlık",ascending=False)
        ağırlıklar=pd.DataFrame(ağırlıklar)
        del ağırlıklar["Ürün"]
        ağırlıklar=ağırlıklar.drop_duplicates()
        ağırlıklar=ağırlıklar[["Ana Grup","Ağırlık"]]
        ağırlıklar2=to_excel(ağırlıklar)

        

        st.download_button(
            label="📊 Madde Ağırlıkları",
            data=ağırlıklar1,
            file_name='Madde Ağırlıkları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        st.download_button(
            label="📊 Ana Grup Ağırlıkları",
            data=ağırlıklar2,
            file_name='Ana Grup Ağırlıkları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        
        tüfeaylıkdata=np.round(tüfeaylıkdata,2)
        tüfeaylıkdata1=to_excel(tüfeaylıkdata)
        st.download_button(
            label="📊 Web-TÜFE Aylık Artış Oranları",
            data=tüfeaylıkdata1,
            file_name='Web-TÜFE Aylık Değişim Oranları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        endeksler_aylık=np.round(endeksler_aylık,2)
        endeksler_aylık=endeksler_aylık.T
        endeksler_aylık.columns=endeksler_aylık.iloc[0,:]
        endeksler_aylık=endeksler_aylık.iloc[1:]
        endeksler_aylık=endeksler_aylık.reset_index()
        endeksler_aylık=endeksler_aylık.rename(columns={"index":"Madde"})
        endeksler_aylık1=to_excel(endeksler_aylık)
        st.download_button(
            label="📊 Maddeler Aylık Artış Oranları",
            data=endeksler_aylık1,
            file_name='Maddeler Aylık Değişim Oranları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        harcama_grupları_aylık=np.round(harcama_grupları_aylık,2)
        harcama_grupları_aylık=harcama_grupları_aylık.T
        harcama_grupları_aylık.columns=harcama_grupları_aylık.iloc[0,:]
        harcama_grupları_aylık=harcama_grupları_aylık.iloc[1:]
        harcama_grupları_aylık=harcama_grupları_aylık.reset_index()
        harcama_grupları_aylık=harcama_grupları_aylık.rename(columns={"index":"Grup"})
        harcama_grupları_aylık1=to_excel(harcama_grupları_aylık)
        st.download_button(
            label="📊 Temel Başlıklar Aylık Artış Oranları",
            data=harcama_grupları_aylık1,
            file_name='Temel Başlıklar Aylık Değişim Oranları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        özelgöstergeler_aylık=özelgöstergeler_aylık.rename(columns={"Alkollü içecekler, tütün ve altın":"Altın"})
        özelgöstergeler_aylık=özelgöstergeler_aylık.T
        özelgöstergeler_aylık.columns=özelgöstergeler_aylık.iloc[0,:]
        özelgöstergeler_aylık=özelgöstergeler_aylık.iloc[1:]
        özelgöstergeler_aylık=özelgöstergeler_aylık.reset_index()
        özelgöstergeler_aylık=özelgöstergeler_aylık.rename(columns={"index":"Grup"})

        özelgöstergeler_aylık1=to_excel(özelgöstergeler_aylık)
        st.download_button(
            label="📊 Özel Kapsamlı Göstergeler Aylık Artış Oranları",
            data=özelgöstergeler_aylık1,
            file_name='Özel Kapsamlı Göstergeler Aylık Değişim Oranları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        gruplar_aylık=gruplar_aylık.T
        gruplar_aylık.columns=gruplar_aylık.iloc[0,:]
        gruplar_aylık=gruplar_aylık.iloc[1:]
        gruplar_aylık=gruplar_aylık.reset_index()
        gruplar_aylık=gruplar_aylık.rename(columns={"index":"Grup"})
        gruplar_aylık1=to_excel(gruplar_aylık)
        st.download_button(
            label="📊 Ana Gruplar Aylık Artış Oranları",
            data=gruplar_aylık1,
            file_name='Ana Gruplar Aylık Değişim Oranları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )


        st.download_button(
            label="📊 Ana Grup Endeksleri",
            data=gruplar_excel,
            file_name='anagruplar.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        endekslerr=pd.read_csv("endeksler.csv",index_col=0)
        maddelerim=endekslerr.T
        maddelerim=maddelerim.reset_index()
        maddelerim=maddelerim.rename(columns={"index":"Madde"})
        maddelerimm=to_excel(maddelerim)

        st.download_button(
            label="📊 Madde Endeksleri",
            data=maddelerimm,
            file_name='maddeler.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        st.download_button(
            label="📊 Harcama Grupları",
            data=harcama_grupları_excel,
            file_name='harcamagrupları.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        ma=pd.read_excel("ma.xlsx",index_col=0)

        st.download_button(
            label="📊 Özel Kapsamlı TÜFE Göstergeleri",
            data=özelgöstergeler_excel,
            file_name='özelkapsamlıgöstergeler.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        ma_excel=to_excel(ma)
        st.download_button(
            label="📊 Mevsimsellikten Arındırılmış Göstergeler (Aylık Artış)",
            data=ma_excel,
            file_name='ma_göstergeler.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )




        
             



    
    
    
    
  
    
    
    



    # Tarihleri belirli bir formatta alıyoruz
    def to_excel(df):
        output = BytesIO()
        # Pandas'ın ExcelWriter fonksiyonunu kullanarak Excel dosyasını oluştur
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')  # index=False ile index'i dahil etmiyoruz
            
            # Writer'dan Workbook ve Worksheet nesnelerine erişim
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            
            # Sütun genişliklerini ayarla
            for i, col in enumerate(df.columns):
                max_length = max(df[col].astype(str).map(len).max(), len(col))  # En uzun değer veya sütun adı uzunluğu
                worksheet.set_column(i, i, max_length + 2)  # +2 biraz boşluk ekler
        processed_data = output.getvalue()  # Bellekteki dosya verisini al
        return processed_data

    


    
    


    
    
   
        
        


    def to_excel(df):
        output = BytesIO()
        # Pandas'ın ExcelWriter fonksiyonunu kullanarak Excel dosyasını oluştur
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')  # index=False ile index'i dahil etmiyoruz
            
            # Writer'dan Workbook ve Worksheet nesnelerine erişim
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            
            # Sütun genişliklerini ayarla
            for i, col in enumerate(df.columns):
                max_length = max(df[col].astype(str).map(len).max(), len(col))  # En uzun değer veya sütun adı uzunluğu
                worksheet.set_column(i, i, max_length + 2)  # +2 biraz boşluk ekler
        processed_data = output.getvalue()  # Bellekteki dosya verisini al
        return processed_data

    

    
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

        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
                
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                
                # Tüm sütunların genişliğini otomatik ayarla
                for i, col in enumerate(df.columns):
                    # En uzun veri ve başlık uzunluğunu hesapla
                    max_len = max(
                        df[col].astype(str).map(len).max(),  # Veri uzunluğu
                        len(str(col))  # Başlık uzunluğu
                    )
                    
                    # Tarih sütunları için özel genişlik
                    if pd.api.types.is_datetime64_any_dtype(df[col]):
                        worksheet.set_column(i, i, 20)  # Tarih sütunları için sabit genişlik
                    else:
                        worksheet.set_column(i, i, max_len + 2)  # Diğer sütunlar için dinamik genişlik
                
                # Hücrelerin hizalanmasını düzenle
                header_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
                for i, col in enumerate(df.columns):
                    worksheet.write(0, i, col, header_format)
            
            processed_data = output.getvalue()
            return processed_data


        
        

        


        
        
       
       

        
      

        
          


        
    
        
if page=="Ana Gruplar":
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
    onceki=(datetime.now()-timedelta(days=31)).strftime("%Y-%m")

    



    gruplar=pd.read_csv("gruplar_int.csv",index_col=0)
    gruplar.index=pd.to_datetime(gruplar.index)
    gruplar.loc[pd.to_datetime("2024-12-31")]=100
    gruplar=gruplar.sort_index()

    
    
    ana = gruplar.columns[:-1]
    

    selected_group = st.sidebar.selectbox("Ana Grup Seçin:", ana)

    selected_group_data=gruplar[selected_group]

    aylık=(((hareketli_aylik_ortalama(gruplar[selected_group])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(gruplar[selected_group])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"])-1)*100)
    aylık=aylık.round(2)


   

    
    hareketliartıs=hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].loc[tarih:]/hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
    hareketliartıs=(hareketliartıs-1)*100

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
                tickfont=dict(size=14, family="Arial Black", color="black")
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
                Nisan Değişimi: <span style='color:red;'>% {aylık}</span><br>
                

            </h3>
            """, unsafe_allow_html=True)
    


    figgana= go.Figure()
    
    figgana.add_trace(go.Scatter(
                x=selected_group_data.index,
                y=selected_group_data.values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
    




    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgana.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index,  # Original datetime index
                ticktext=selected_group_data.index.strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black")
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
        hareketliartıs=carim.values/hareketli_aylik_ortalama(gruplar[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
        hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
        hareketliartıs=(hareketliartıs-1)*100
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
        hareketliartıs=carim.values/hareketli_aylik_ortalama(selected_harcamagrupları[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
        hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
        hareketliartıs=(hareketliartıs-1)*100
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
    onceki=(datetime.now()-timedelta(days=31)).strftime("%Y-%m")
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

    aylık=((hareketli_aylik_ortalama(harcama_grupları[selected_group])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(harcama_grupları[selected_group])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"])-1)*100
    aylık=aylık.round(2)
    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                31.12.2024 - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                Nisan Değişimi: <span style='color:red;'>% {aylık}</span><br>

            </h3>
            """, unsafe_allow_html=True)
    


    figgharcama= go.Figure()
    
    figgharcama.add_trace(go.Scatter(
                x=selected_group_data.index,
                y=selected_group_data.values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
        



    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgharcama.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index,  # Original datetime index
                ticktext=selected_group_data.index.strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black")
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
        hareketliartıs=carim.values/hareketli_aylik_ortalama(harcama_grupları[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
        hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
        hareketliartıs=(hareketliartıs-1)*100
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
    onceki=(datetime.now()-timedelta(days=31)).strftime("%Y-%m")

    tüfe=pd.read_csv("gruplar_int.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    özelgöstergeler=pd.read_csv("özelgöstergeler.csv",index_col=0)
    özelgöstergeler.index=pd.to_datetime(özelgöstergeler.index)
    özelgöstergeler=özelgöstergeler.rename(columns={"Alkollü içecekler, tütün ve altın":"Altın"})
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
    
    aylık=((hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"])-1)*100
    aylık=aylık.round(2)

    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                01.01.2025 - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                Nisan Değişimi: <span style='color:red;'>% {aylık}</span><br>

            </h3>
            """, unsafe_allow_html=True)
    

    


    figgösterge=go.Figure()
    
    figgösterge.add_trace(go.Scatter(
                x=selected_group_data.index,
                y=selected_group_data.values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))
        
        



    
   
   

        # X ekseninde özelleştirilmiş tarih etiketlerini ayarlıyoruz
    figgösterge.update_layout(
            xaxis=dict(
                tickvals=selected_group_data.index,  # Original datetime index
                ticktext=selected_group_data.index.strftime("%d.%m.%Y"),  # Custom formatted labels
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.plotly_chart(figgösterge)

    from datetime import datetime,timedelta
    tarih=datetime.now().strftime("%Y-%m")
    onceki=(datetime.now()-timedelta(days=31)).strftime("%Y-%m")
    cari=hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
    hareketliartıs=cari.values/hareketli_aylik_ortalama(selected_group_data)["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
    hareketliartıs=pd.Series(hareketliartıs,index=cari.index)
    hareketliartıs=(hareketliartıs-1)*100

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
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            yaxis=dict(
                tickfont=dict(size=14, family="Arial Black", color="black")
            ),
            font=dict(family="Arial", size=14, color="black")
        )
    
    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Aylık Artış Oranı</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 18px; color: black; background-color: #f0f0f0; padding: 15px; border-radius: 5px;">
        Not: Aylık artış oranı mevcut ayın ortalamasının önceki ayın 24 günlük ortalamasına göre değişimi ile hazırlanmıştır.
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
        hareketliartıs=carim.values/hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
        hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
        hareketliartıs=(hareketliartıs-1)*100
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
    gösterge_artıs1=pd.Series(index=gösterge_artıs.columns.values)
    for col in gösterge_artıs.columns:
        gösterge_artıs1.loc[col]=((hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(özelgöstergeler[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"])-1)*100
    gösterge_artıs1.loc["TÜFE"]=((hareketli_aylik_ortalama(tüfe["TÜFE"])["Aylık Ortalama"].fillna(method="ffill").iloc[-1]/hareketli_aylik_ortalama(tüfe["TÜFE"])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"])-1)*100
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
    onceki=(datetime.now()-timedelta(days=31)).strftime("%Y-%m")
    ürüngrupları=pd.read_csv("harcamaürünleri1.csv",index_col=0)

    endeksler=pd.read_csv("endeksler_int.csv",index_col=0)

    harcamagrupları=pd.read_csv("harcamagrupları_int.csv",index_col=0)

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
        cari=hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill")
        maddeler_aylık[col]=cari.resample('M').last().pct_change().loc["2025-02":]*100
        carim=hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill").loc[tarih:]
        hareketliartıs=carim.values/hareketli_aylik_ortalama(endeksler[col])["Aylık Ortalama"].fillna(method="ffill").loc[f"{onceki}-24"]
        hareketliartıs=pd.Series(hareketliartıs,index=carim.index)
        hareketliartıs=(hareketliartıs-1)*100
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









