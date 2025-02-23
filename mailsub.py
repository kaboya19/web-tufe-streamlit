import os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import time



# SMTP Ayarları
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "borakaya8@gmail.com"
SENDER_PASSWORD = "dqpp vgar wujr vhei"

# Abone listesi
SUBSCRIBERS_FILE = "subscribers1.csv"

# E-Posta Gönderim Fonksiyonu
def send_email_with_images(to_email, subject, body, images):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    # Görselleri Ekle
    for img_id, img_path in images.items():
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                img_data = f.read()
                img = MIMEImage(img_data)
                img.add_header('Content-ID', f'<{img_id}>')
                msg.attach(img)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"E-posta başarıyla gönderildi: {to_email}")
        return True
    except Exception as e:
        print(f"E-posta gönderim hatası: {e}")
        return False

# Toplu E-Posta Gönderimi
def send_bulk_email_with_images(subject, body, images):
    if os.path.exists(SUBSCRIBERS_FILE) and os.path.getsize(SUBSCRIBERS_FILE) > 0:
        df = pd.read_csv(SUBSCRIBERS_FILE)
        success_count = 0
        fail_count = 0
        for email in df["email"]:
            if send_email_with_images(email, subject, body, images):
                success_count += 1
                time.sleep(2)
            else:
                fail_count += 1
        print(f"{success_count} e-posta başarıyla gönderildi, {fail_count} e-posta gönderilemedi.")
    else:
        print("Abone listesi bulunamadı veya boş!")

# Ana E-Posta İçeriği ve Gönderimi
if __name__ == "__main__":
    subject = f"Web-Tüketici Fiyat Endeksi Şubat 2025 Bülteni"
    body = f"""
    <h2 style='color:black; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Şubat 2025 Bülteni</h2>
    <h3 style='color:red; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Şubat'ta %3,41 arttı</h3>
    <br>
    <img src="cid:image1" style="max-width:600px; margin: 10px 0;"/>
    <p>Web-Şubat Fiyat Endeksi Şubat'ta %3,41 artış kaydederken mevsimsellikten arındırılmış artış %2,85 oldu.</p>
    <br>
    <p>En çok artış ve düşüş yaşanan maddeler:</p>
    <img src="cid:image2" style="max-width:600px; margin: 10px 0;"/>
    <p>En çok artış ve düşüş yaşanan temel başlıklar:</p>
    <img src="cid:image3" style="max-width:600px; margin: 10px 0;"/>
    <p>Özel Kapsamlı TÜFE Göstergeleri:</p>
    <img src="cid:image4" style="max-width:600px; margin: 10px 0;"/>
    <p>Özel Kapsamlı Göstergeler aylık artış oranları: </p>
    <img src="cid:image5" style="max-width:600px; margin: 10px 0;"/>
    <p>Ana gruplara ait artış oranları:  </p>
    <img src="cid:image6" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image7" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image8" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image9" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image10" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image11" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image12" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image13" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image14" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image15" style="max-width:600px; margin: 10px 0;"/>
    <img src="cid:image16" style="max-width:600px; margin: 10px 0;"/>
    <br>
    <p>Seçilmiş maddelere ait ortalama fiyatlar:</p>
    <img src="cid:image17" style="max-width:600px; margin: 10px 0;"/>
    <br>
    <p>Mevsimsellikten arındırılmış ana eğilimlere bakıldığında medyan artış %3,21 olmuştur.</p>
    <p>SATRIM(Mevsimsel Düzeltilmiş Budanmış Enflasyon) göstergesi ise %3,27 artmıştır.</p>
    <br>
    <img src="cid:image18" style="max-width:600px; margin: 10px 0;"/>
    <p><a href='https://web-tufe.streamlit.app/'>Web-Tüketici Fiyat Endeksi ile ilgili tüm verilere buradan ulaşabilirsiniz.</a></p>
    <hr>
    <small>
        *Bu bültenin bir sonraki yayınlanma tarihi 24 Mart 2025'tir. Burada yer alan bilgi ve analizler tamamen kişisel çalışma olup kesin bir doğruluk içermemekte ve yatırım tavsiyesi içermemektedir.*<br>
        *TÜİK’in hesaplamasıyla uyumlu olması açısından ayın ilk 24 günündeki veriler dikkate alınmıştır.*
    </small>
    <br>
    <p><strong>Hazırlayan:Bora Kaya</strong><br>
    <p>Twitter: <a href='https://x.com/mborathe'>https://x.com/mborathe</a></p>
    <p>Linkedin: <a href='https://www.linkedin.com/in/bora-kaya/'>https://www.linkedin.com/in/bora-kaya/</a></p>
   

    """

    # Görsellerin Yolları
    images = {
        "image1": "anagruplar.png",
        "image2": "maddeler.png",
        "image3": "temelbaşlıklar.png",
        "image4": "özelgöstergeler.png",
        "image5": "özelgöstergelerartış.png",
        "image6": "eveşyası.png",
        "image7": "eğitim.png",
        "image8": "eğlence.png",
        "image9": "Giyim ve ayakkabı.png",
        "image10": "Gıda ve alkolsüz içecekler.png",
        "image11": "Haberleşme.png",
        "image12": "Konut.png",
        "image13": "Lokanta ve oteller.png",
        "image14": "Ulaştırma.png",
        "image15": "Çeşitli mal ve hizmetler.png",
        "image16": "Giyim ve ayakkabı.png",
        "image17": "fiyatlar.png",
        "image18": "eğilim.png"
    }

    # Toplu E-Posta Gönderimi
    send_bulk_email_with_images(subject, body, images)
