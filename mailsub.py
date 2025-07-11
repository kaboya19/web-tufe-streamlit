import os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from datetime import datetime
import time

# SMTP Ayarları
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "borakaya8@gmail.com"
SENDER_PASSWORD = "dqpp vgar wujr vhei"

# Abone listesi
SUBSCRIBERS_FILE = "subscribers.csv"

# E-Posta Gönderim Fonksiyonu
def send_email_with_images_and_pdf(to_email, subject, body, images, pdf_paths):
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

    # PDF Ekleri
    for pdf_path in pdf_paths:
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as f:
                pdf = MIMEApplication(f.read(), _subtype='pdf')
                pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_path))
                msg.attach(pdf)

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
def send_bulk_email_with_images_and_pdf(subject, body, images, pdf_paths):
    if os.path.exists(SUBSCRIBERS_FILE) and os.path.getsize(SUBSCRIBERS_FILE) > 0:
        df = pd.read_csv(SUBSCRIBERS_FILE)
        success_count = 0
        fail_count = 0
        for email in df["email"]:
            if send_email_with_images_and_pdf(email, subject, body, images, pdf_paths):
                success_count += 1
                time.sleep(2)
            else:
                fail_count += 1
        print(f"{success_count} e-posta başarıyla gönderildi, {fail_count} e-posta gönderilemedi.")
    else:
        print("Abone listesi bulunamadı veya boş!")

# Ana E-Posta İçeriği ve Gönderimi
if __name__ == "__main__":
    subject = f"Web-Tüketici Fiyat Endeksi Haziran 2025 Bülteni"
    body = body = body = f"""
<h2 style='color:black; font-weight:bold;'>Web-Tüketici Fiyat Endeksi Haziran 2025 Bülteni</h2>
<p>Ekli PDF dosyasında bülteni bulabilirsiniz.</p>

<h3 style='color:black;'>Özet:</h3>
<p>
Web Tüketici Fiyat Endeksi Haziran ayında yüzde 1,30 oranında yükselmiş, yılbaşından itibaren ölçülen artış yüzde 15,69 olmuştur. 
Aylık enflasyon lokanta-oteller, ev eşyası, eğlence kültür ve konut gruplarında yavaşlamış, gıda,ulaştırma ve çeşitli mal hizmetler gruplarında hızlanmıştır. 
Haziran ayında lokanta oteller grubu öne çıkmış, otel fiyatlarında görülen artış grubu önemli ölçüde yükseltmiştir. 
Gıda fiyatları aylık yüzde -0,21 ile gerileme kaydetmiştir.
</p>
<p>
Enerji grubunda,akaryakıt fiyatlarındaki yüksek artış ile yüzde 2,11 artış görüldü.
</p>
<p>
Temel mal grubunda, giyim ve ayakkabıda fiyatların ılımlı arttığı, Dayanıklı mal ile diğer temel mal grubunda kur artışının etkilerinin bitmesiyle fiyat artışlarının belirgin yavaşladığı görüldü.
</p>
<p>
Hizmetler grubunda aylık enflasyon yüzde 3,52 ile bu yılın en yüksek seviyesine hızlanmıştır.Bu gelişmede bayram etkisiyle sert yükselen ulaştırma hizmetleri etkili oldu.
</p>
<p>
Bu görünüm altında, mevsimsel düzeltilmiş veriler, B,C,Medyan ve SATRIM göstergeleri ile ana eğilim yatay seyretmiştir.
</p>
<p>
Web-TÜFE web sitesi için: <a href="https://www.webtufe.com">buraya tıklayın</a>.
</p>
<p>
Verisetine erişmek için: <a href="https://docs.google.com/spreadsheets/d/14iiu_MQwtMxHTFt6ceyFhkk6v0OL-wuoQS1IGPzSpNE">buraya tıklayın</a>.
</p>
"""



    images = {}  # İstersen görsel yollarını buraya ekle örn: {"chart1": "path/to/image1.png"}
    pdf_paths = ["Haziran 2025.pdf"]  # PDF dosya yolları

    send_bulk_email_with_images_and_pdf(subject, body, images, pdf_paths)
