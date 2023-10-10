import smtplib

def register():
    name = input("Adınızı girin: ")
    email = input("E-posta adresinizi girin: ")
    password = input("Şifrenizi girin: ")

    # Burada e-posta ve şifre bilgilerini bir veritabanına kaydedebilirsiniz

    print("Kayıt başarılı!")

def login():
    email = input("E-posta adresinizi girin: ")
    password = input("Şifrenizi girin: ")

    # Burada e-posta ve şifre bilgilerini veritabanında kontrol edebilirsiniz

    if email == email and password == password:
        print("Giriş başarılı!")
    else:
        print("E-posta veya şifre hatalı!")

def send_email():
    sender_email = input("Gönderici e-posta adresini girin: ")
    sender_password = input("Gönderici e-posta şifresini girin: ")
    receiver_email = input("Alıcı e-posta adresini girin: ")
    subject = input("E-posta konusunu girin: ")
    message = input("E-posta mesajını girin: ")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")
        server.quit()
        print("E-posta gönderildi!")
    except Exception as e:
        print("E-posta gönderilirken bir hata oluştu:", str(e))

while True:
    print("1. Kayıt Ol")
    print("2. Giriş Yap")
    print("3. E-posta Gönder")
    print("4. Çıkış")

    choice = input("Seçiminizi yapın: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        send_email()
    elif choice == "4":
        break
    else:
        print("Geçersiz seçim!")