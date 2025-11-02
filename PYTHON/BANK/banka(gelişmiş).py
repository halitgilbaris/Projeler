import time
import json

blocked_accounts = {}
hesaplar = {} 
son_hesap_no = 0  # başında 0 yeterli
admin_isim = "ADmin"
admin_şifre = "250708Admin."
json_dosya = "veriler.json"  # verilerin kaydedileceği dosya

# ----------------- JSON YÜKLE -----------------
def verileri_yukle():
    global hesaplar, blocked_accounts, son_hesap_no
    try:
        with open(json_dosya, "r") as f:
            data = json.load(f)
            hesaplar = {int(k): v for k, v in data.get("hesaplar", {}).items()}
            blocked_accounts = {int(k): v for k, v in data.get("blocked_accounts", {}).items()}
            son_hesap_no = max(hesaplar.keys(), default=0)
    except FileNotFoundError:
        hesaplar = {}
        blocked_accounts = {}
        son_hesap_no = 0

# ----------------- JSON KAYDET -----------------
def verileri_kaydet():
    data = {
        "hesaplar": hesaplar,
        "blocked_accounts": blocked_accounts
    }
    with open(json_dosya, "w") as f:
        json.dump(data, f, indent=4)

# ----------------- HESAP OLUŞTUR -----------------
def hesap_olustur():
    global son_hesap_no
    hesap_kullanıcı_ismi = input("Kullanıcı ismini giriniz: ")
    hesap_kullanıcı_şifre = input("Kullanıcı şifresini giriniz: ")

    if not hesap_kullanıcı_ismi.strip() or not hesap_kullanıcı_şifre.strip():
        print("Kullanıcı ismi ve şifre boş bırakılamaz!")
        return

    for bilgiler in hesaplar.values():
        if bilgiler["isim"] == hesap_kullanıcı_ismi:
            print("Bu kullanıcı adı alınmış!")
            return
        if bilgiler["şifre"] == hesap_kullanıcı_şifre:
            print("Bu şifre zaten kullanılıyor!")
            return

    son_hesap_no += 1
    hesap_no = son_hesap_no
    hesaplar[hesap_no] = {"isim": hesap_kullanıcı_ismi, "şifre": hesap_kullanıcı_şifre, "bakiye": 0}
    verileri_kaydet()
    print(f"Hesap oluşturuldu! Hesap No: {hesap_no}")

# ----------------- HESAP AÇ -----------------
def hesap_aç():
    hesap_isim = input("Lütfen kullanıcı ismini giriniz: ")
    hesap_şifre = input("Lütfen kullanıcı şifresini giriniz: ")

    for hesap_no, bilgiler in hesaplar.items():
        # Block kontrol
        if hesap_no in blocked_accounts and time.time() < blocked_accounts[hesap_no]:
            print(f"Kullanıcı blocklu! Kalan süre: {int((blocked_accounts[hesap_no]-time.time())/60)+1} dk")
            return
        elif bilgiler["isim"] == hesap_isim and bilgiler["şifre"] == hesap_şifre:
            print(f"Giriş Başarılı! Hesap No: {hesap_no}")
            hesap_işlem(hesap_no)
            return hesap_no

    print("Hatalı İsim veya Şifre!")

# ----------------- HESAP İŞLEM -----------------
def hesap_işlem(hesap_no):
    global hesaplar
    while True:
        işlem1 = input("""
1) Bakiye Sorgulama
2) Bakiye Yükleme
3) Bakiye Gönderme
4) Hesap No Sorgulama
q) Çıkış
""")

        if işlem1 == "1":
            bakiye = hesaplar[hesap_no]["bakiye"]
            print(f"Bakiyeniz: {bakiye:,.2f} TL")

        elif işlem1 == "2":
            try:
                miktar = float(input("Yüklenecek miktarı girin: "))
                hesaplar[hesap_no]["bakiye"] += miktar
                verileri_kaydet()
                print(f"Güncel bakiyeniz: {hesaplar[hesap_no]['bakiye']:,.2f} TL")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz!")

        elif işlem1 == "3":
            try:
                miktar1 = float(input("Göndereceğiniz bakiye miktarı: "))
                kim = input("Göndereceğiniz kişinin kullanıcı ismi: ")
                hedef_hesap_no = None
                for no, bilgiler in hesaplar.items():
                    if bilgiler["isim"] == kim:
                        hedef_hesap_no = no
                        break
                if hedef_hesap_no is not None:
                    if hesaplar[hesap_no]["bakiye"] >= miktar1:
                        hesaplar[hesap_no]["bakiye"] -= miktar1
                        hesaplar[hedef_hesap_no]["bakiye"] += miktar1
                        verileri_kaydet()
                        print(f"Başarıyla gönderildi! Güncel bakiyeniz: {hesaplar[hesap_no]['bakiye']:,.2f} TL")
                    else:
                        print("Yeterli bakiye yok!")
                else:
                    print("Kullanıcı bulunamadı!")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz!")

        elif işlem1 == "4":
            print(f"Hesap No: {hesap_no}")

        elif işlem1 == "q":
            print("Çıkış yapıldı!")
            break
        else:
            print("Geçersiz komut!")

# ----------------- ADMIN -----------------
def admin():
    isim = input("Lütfen admin ismini giriniz: ")
    şifre = input("Lütfen admin şifresini giriniz: ")
    if isim == admin_isim and şifre == admin_şifre:
        print("Giriş Başarılı!")
        admin_panel()
    else:
        print("HATALI İSİM YA DA ŞİFRE!")

# ----------------- ADMIN PANEL -----------------
def admin_panel():
    while True:
        işlem = input("""
1) Hesapları Göster
2) Hesap Bul
q) Çıkış
""")
        if işlem == "1":
            for no, bilgiler in hesaplar.items():
                print(f"Hesap No: {no}, Kullanıcı İsmi: {bilgiler['isim']}, Bakiye: {bilgiler['bakiye']:,.2f} TL")

        elif işlem == "2":
            isim = input("Kullanıcı ismi: ")
            bulundu = False
            for hesap_no, bilgiler in hesaplar.items():
                if bilgiler["isim"] == isim:
                    bulundu = True
                    print(f"Hesap Bulundu!\nHesap No: {hesap_no}\nKullanıcı İsmi: {bilgiler['isim']}\nŞifre: {bilgiler["şifre"]}\nBakiye: {bilgiler['bakiye']:,.2f} TL")
                    secim = input("Bu kullanıcıyla ne yapmak istersiniz? (sil/block/iptal): ").lower()
                    if secim == "sil":
                        del hesaplar[hesap_no]
                        if hesap_no in blocked_accounts:
                            del blocked_accounts[hesap_no]
                        verileri_kaydet()
                        print("Kullanıcı silindi!")
                    elif secim == "block":
                        try:
                            dk = int(input("Kaç dakika block koymak istersiniz? "))
                            blocked_accounts[hesap_no] = time.time() + dk*60
                            verileri_kaydet()
                            print(f"Kullanıcı {dk} dakika blocklandı!")
                        except ValueError:
                            print("Geçerli bir sayı girin!")
                    elif secim == "iptal":
                        print("İşlem iptal edildi.")
                    else:
                        print("Geçersiz seçim!")
                    break
            if not bulundu:
                print("Kullanıcı bulunamadı!")

        elif işlem == "q":
            print("ADMİN OFF!")
            break
        else:
            print("Geçersiz işlem!")

# ----------------- ANA İŞLEM -----------------
def ana_islem():
    verileri_yukle()
    while True:
        işlem = input("""
1) Hesap Oluştur
2) Hesap Aç
3) Admin Panel
q) Çıkış
""")
        if işlem == "1":
            hesap_olustur()
        elif işlem == "2":
            hesap_aç()
        elif işlem == "3":
            admin()
        elif işlem == "q":
            print("Görüşmek üzere!")
            break
        else:
            print("Geçersiz işlem!")

# ----------------- PROGRAM BAŞLAT -----------------
ana_islem()
