ogrenci_listesi = []

def ekle():
    isim = input("Öğrenci ismi: ")
    soyisim = input("Öğrenci soyismi: ")
    ogrenci_listesi.append(isim + " " + soyisim)
    print("Öğrenci eklenmiştir!")

def kaldir():
    isim = input("Öğrenci ismi: ")
    soyisim = input("Öğrenci soyismi: ")
    ogrenci_listesi.remove(isim + " " + soyisim)

def coklu_ekle():
    eklemeAdedi = int(input("Kaç öğrenci ekleyeceksiniz: "))
    for i in range(eklemeAdedi):
        ekle()
        print(f"{eklemeAdedi} yeni kayıt eklendi ")

def coklu_sil():
    silmeAdedi = int(input("Kaç öğrenci ekleyeceksiniz: "))
    for i in range(silmeAdedi):
        kaldir()
        print(f"{silmeAdedi} yeni kayıt silindi ")

def yazdir():
    print(ogrenci_listesi)


while True:
    print("öğrenci bilgi sistemi")
    print("1-ogrenci ekle")
    print("2-ögrenci sil")
    print("3-çoklu ögrenci ekleme")
    print("4-çoklu öğrenci silme")
    print("5-ögrenci yazdırma ")
    print("6-çıkış")
    menuNo = int(input("İşlem Seçiniz: "))


    if menuNo == 1:
        ekle()
    elif menuNo == 2:
        kaldir()
    elif menuNo == 3:
        coklu_ekle()
    elif menuNo == 4:
        coklu_sil()
    elif menuNo == 5:
        yazdir()
    elif menuNo == 6:
        break



