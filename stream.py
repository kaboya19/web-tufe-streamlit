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
st.set_page_config(page_title="Web-Tüketici Fiyat Endeksi",layout="wide")
social_media_links = {
    "X": {"url": "https://x.com/mborathe", "color": "#000000"},
    "GitHub": {"url": "https://github.com/kaboya19", "color": "#000000"},
    "LinkedIn": {"url": "https://www.linkedin.com/in/bora-kaya/", "color": "#000000"}
}
tabs=["Tüketici Fiyat Endeksi","Ana Gruplar","Harcama Grupları","Özel Kapsamlı Göstergeler","Metodoloji Notu"]
tabs = option_menu(
    menu_title=None,
    options=["Tüketici Fiyat Endeksi","Ana Gruplar","Harcama Grupları","Özel Kapsamlı Göstergeler" ,"Metodoloji Notu"],
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
            "height": "70px",  # Set a fixed height for all buttons
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



if page=="Metodoloji Notu":
    
     

    # Başlık
    st.title("Web Tüketici Fiyat Endeksi (Web-TÜFE) Metodoloji Açıklaması")

    # Analitik Çerçeve ve Kapsam
    st.subheader("Analitik Çerçeve ve Kapsam")
    st.write("""
    Web Tüketici Fiyat Endeksinin amacı, TÜFE'de yer alan Alkollü içecekler ve Sağlık grubu dışında kalan ürünlerin günlük değişimini ölçerek enflasyon oranını hesaplamaktır. 
    Alkollü içecekler ve Sağlık grubunun ölçümü web üzerinden yapılamamaktadır.Bu bağlamda bu gruplar dışında yer alan 385 maddenin 318 adedi derlenmektedir.
    TÜİK sepetinin ağırlık bazında %81,7'si ölçülebilmiştir.
    Bu çerçevede, 6 Ocak 2025 endeksi baz olarak "100" seçilmiştir.

    """)
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
    st.image("4.png")
    st.image("5.png")

    # Mevsimsel Düzeltme
    st.subheader("Mevsimsel Düzeltme")
    st.write("""
    İlk aşamada verilerde mevsimsel düzeltme yapılmayacaktır. Ancak verilerin birikmesiyle ilerleyen dönemlerde, TÜİK’in açıklamış olduğu metodolojiye uygun olarak mevsimsel düzeltme yapılacaktır. 
    Bu sonuçlar web sitesinde ve e-posta aboneliği olan kullanıcılara ayrıca yeni bir endeks olarak bildirilecektir.
    """)

    # Veri Derleme
    st.subheader("Veri Derleme")
    st.write("""
    Toplanan veriler web scraping yöntemiyle Python üzerinden derlenmektedir. Şu an itibariyle her gün 37.000'den fazla fiyat toplanmaktadır. 

    """)

    # Sonuçların Açıklanması
    st.subheader("Sonuçların Açıklanması")
    st.write("""
    Her ayın 24'inde aylık enflasyon oranları duyurulacaktır. Aynı zamanda her bir ürün için kullanılan fiyatlar tablo olarak yayınlanmaktadır. 
    Bu sayede şeffaf bir şekilde yaşanan fiyat değişimleri izlenebilmektedir.
    """)

    # İmza
    st.write("""
    ---
    Hazırlayan
    Bora Kaya  
    """)




     

if page=="Tüketici Fiyat Endeksi":

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
    
    


    
    tüfe = pd.read_csv("tüfe.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)

    endeksler=pd.read_csv("endeksler.csv",index_col=0)
    endeksler.index=pd.to_datetime(endeksler.index)
    sira=np.sort(endeksler.columns.values)
    endeksler=endeksler[sira]
   
    

    

    
    ağırlıklar=pd.read_csv("ağırlıklartüfe.csv",index_col=0)
    
    
    endeksler["TÜFE"]=tüfe["TÜFE"]

    sira = ['TÜFE'] + [col for col in endeksler.columns if col != 'TÜFE']


    endeksler = endeksler[sira]


    

    

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
    first_value = selected_group_data.iloc[0,0]  # İlk değer
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
    

    def hareketli_aylik_ortalama1(df):
            değer=df.name
            df=pd.DataFrame(df)
            df["Tarih"]=pd.to_datetime(df.index)
            df['Aylık Ortalama'] = df.groupby(df['Tarih'].dt.to_period('M'))[değer].expanding().mean().reset_index(level=0, drop=True)
            df.index=pd.to_datetime(df.index)
            return df


# Hareketli aylık ortalama hesaplama
    hareketlima = hareketli_aylik_ortalama(selected_group_data.iloc[:,0])
    hareketlima["Aylık Ortalama"]=hareketlima["Aylık Ortalama"].fillna(method="ffill")
    hareketlima1 = hareketli_aylik_ortalama1(selected_group_data.iloc[:,0])
    




    if selected_group == "TÜFE":

    
        st.markdown(f"<h2 style='text-align:left; color:black;'>Web Tüketici Fiyat Endeksi</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Fiyat Endeksi</h2>", unsafe_allow_html=True)
    
    
    
  
    

    

    

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

        st.markdown(
    f"""
    <h3 style='text-align:left; color:black;'>
        {first_date} - {last_date} Değişimi: 
        <span style='color:red;'>%{change_percent}</span>
        <br>
        <span style='font-size:15px;'>
        </span>
    </h3>
    """,
    unsafe_allow_html=True
)

        
        st.plotly_chart(figgalt)


        
    elif selected_group=="TÜFE":

        



        figgalt.add_trace(go.Scatter(
                x=tüfe.index,
                y=tüfe["TÜFE"].values,
                mode='lines+markers',
                name=selected_group,
                line=dict(color='blue', width=4),
                marker=dict(size=8, color="black"),
                hovertemplate='%{x|%d.%m.%Y}<br>%{y:.2f}<extra></extra>'
            ))

        

   
        st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                {first_date} - {last_date} Değişimi: <span style='color:red;'>%{change_percent}</span><br>
                

            </h3>
            """, unsafe_allow_html=True)
        
      
        st.plotly_chart(figgalt)

        gruplar=pd.read_csv("anagruplar.csv",index_col=0)
        gruplar.index=pd.to_datetime(gruplar.index)
        
        tüfe=pd.read_csv("tüfe.csv",index_col=0)
        tüfe.index=pd.to_datetime(tüfe.index)
        gruplar["TÜFE"]=tüfe["TÜFE"]

        harcama_artıs=((gruplar.iloc[-1]/gruplar.iloc[0])-1)*100
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

    data=pd.read_csv("gıdalı.csv",index_col=0)
    data=data.sort_index()


    fiyatlar=pd.read_csv("gıdalı.csv",index_col=0)
    fiyatlar=fiyatlar.sort_index()
   
    fiyatlar=fiyatlar.sort_index()
   
    excel_data = to_excel(fiyatlar)
    


    
    if selected_group!="TÜFE":
   
        fiyat = fiyatlar.loc[selected_group]
        


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


        
        

        


        
        
       
       

        
      

        
          


        
    else:
        if selected_group!="TÜFE":
            st.markdown(f"<h2 style='text-align:left; color:black;'>Fiyat Listesi</h2>", unsafe_allow_html=True)
        try:
            st.dataframe(fiyat)
        except:
             pass
        
if page=="Ana Gruplar":


    gruplar=pd.read_csv("anagruplar.csv",index_col=0)
    gruplar.index=pd.to_datetime(gruplar.index)
    
    ana = gruplar.columns


    selected_group = st.sidebar.selectbox("Ana Grup Seçin:", ana)

    selected_group_data=gruplar[selected_group]

    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Endeksi</h2>", unsafe_allow_html=True)

    first_date = selected_group_data.index[0].strftime("%d.%m.%Y")  # İlk tarihi formatlama
    last_date = selected_group_data.index[-1].strftime("%d.%m.%Y")  # Son tarihi formatlama
  

        # Değişim yüzdesini hesaplama
    first_value = selected_group_data.iloc[0]  # İlk değer
    last_value = selected_group_data.iloc[-1] # Son değer
    change_percent = ((last_value - first_value) / first_value) * 100  # Yüzde değişim
    change_percent = round(change_percent, 2)

    

    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                {first_date} - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                

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



    

    ürüngrupları=pd.read_csv("harcamaürünleri.csv",index_col=0)
    ürüngrupları=ürüngrupları[ürüngrupları["Ana Grup"]==selected_group]

    harcama = ürüngrupları["Grup"].unique()


 

    harcama_grupları=pd.read_csv("harcama_grupları.csv",index_col=0)
    harcama_grupları.index=pd.to_datetime(harcama_grupları.index)

    selected_harcamagrupları=harcama_grupları[harcama]
    anagruplar=pd.read_csv("anagruplar.csv",index_col=0)

    selected_harcamagrupları[selected_group]=anagruplar[selected_group].values

    

   


    

    selected_harcamagruplarıartıs=((selected_harcamagrupları.iloc[-1]/selected_harcamagrupları.iloc[0])-1)*100
    selected_harcamagruplarıartıs=selected_harcamagruplarıartıs.sort_values()

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
    harcama_grupları=pd.read_csv("harcama_grupları.csv",index_col=0)
    harcama_grupları.index=pd.to_datetime(harcama_grupları.index)
    ana = harcama_grupları.columns
    selected_group = st.sidebar.selectbox("Harcama Grubu Seçin:", ana)

    selected_group_data=harcama_grupları[selected_group]

    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Endeksi</h2>", unsafe_allow_html=True)

    first_date = selected_group_data.index[0].strftime("%d.%m.%Y")  # İlk tarihi formatlama
    last_date = selected_group_data.index[-1].strftime("%d.%m.%Y")  # Son tarihi formatlama
  

        # Değişim yüzdesini hesaplama
    first_value = selected_group_data.iloc[0]  # İlk değer
    last_value = selected_group_data.iloc[-1] # Son değer
    change_percent = ((last_value - first_value) / first_value) * 100  # Yüzde değişim
    change_percent = round(change_percent, 2)

    

    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                {first_date} - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                

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

    tüfe=pd.read_csv("tüfe.csv",index_col=0)
    tüfe.index=pd.to_datetime(tüfe.index)
    harcama_grupları["TÜFE"]=tüfe["TÜFE"]

    harcama_artıs=((harcama_grupları.iloc[-1]/harcama_grupları.iloc[0])-1)*100
    harcama_artıs=harcama_artıs.sort_values()

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
    özelgöstergeler=pd.read_csv("özelgöstergeler.csv",index_col=0)
    özelgöstergeler.index=pd.to_datetime(özelgöstergeler.index)
    gösterge=özelgöstergeler.columns.values

    selected_group = st.sidebar.selectbox("Özel Kapsamlı Gösterge Seçin:", gösterge)

    selected_group_data=özelgöstergeler[selected_group]

    st.markdown(f"<h2 style='text-align:left; color:black;'>{selected_group} Endeksi</h2>", unsafe_allow_html=True)

    first_date = selected_group_data.index[0].strftime("%d.%m.%Y")  # İlk tarihi formatlama
    last_date = selected_group_data.index[-1].strftime("%d.%m.%Y")  # Son tarihi formatlama
  

        # Değişim yüzdesini hesaplama
    first_value = selected_group_data.iloc[0]  # İlk değer
    last_value = selected_group_data.iloc[-1] # Son değer
    change_percent = ((last_value - first_value) / first_value) * 100  # Yüzde değişim
    change_percent = round(change_percent, 2)

    

    st.markdown(f"""
            <h3 style='text-align:left; color:black;'>
                {first_date} - {last_date} Değişimi: <span style='color:red;'>% {change_percent}</span><br>
                

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




    gösterge_artıs=((özelgöstergeler.iloc[-1]/özelgöstergeler.iloc[0])-1)*100
    gösterge_artıs=gösterge_artıs.sort_values()

    colors = ['red' if label == 'TÜFE' else 'blue' for label in gösterge_artıs.index]

    # İlk 42 karakteri almak için index etiketlerini kısaltma
    shortened_index = [label[:42] for label in gösterge_artıs.index]

    # Grafik oluşturma
    figartıs = go.Figure()

    # Verileri ekleme
    figartıs.add_trace(go.Bar(
        y=shortened_index,  # Kısaltılmış index etiketleri
        x=gösterge_artıs.values,
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
            tickvals=list(range(len(gösterge_artıs.index))),  # Her bir index için bir yer belirle
            ticktext=shortened_index  # Kısaltılmış index etiketleri
        )
    )

    # Etiket ekleme
    for i, value in enumerate(gösterge_artıs.values):
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









