import datetime

Harcamalar = {}
Gelirler = {}
son_harcama_no = 0
son_gelir_no = 0
bugun = datetime.date.today().strftime("%d/%m/%Y")

ktg1 = "Yemek"
ktg2 = "Ulaşım"
ktg3 = "Eğlence"
ktg4 = "Maaş"
ktg5 = "Harçlık"
ktg6 = "Diğer"

def harcama():
    global son_harcama_no
    while True:
        print("Kategori seç!")
        menu0 = input("""1) Yemek
2) Ulaşım
3) Eğlence
4) Çıkış
""")

        if menu0 == "1":
            hrcm1 = input("Lütfen Harcama Miktarını Giriniz(Çıkmak için 5 yazınız): ")
            if hrcm1 == "5":
                break
            hrcm1 = float(hrcm1)
            son_harcama_no += 1
            harcama_no = son_harcama_no
            look1 = Harcamalar[harcama_no] = {"Kategori": ktg1, "Miktar": hrcm1, "Tarih": bugun}
            print(f"Başarılı şekilde eklendi\n{look1}")

        elif menu0 == "2":
            hrcm2 = input("Lütfen Harcama Miktarını Giriniz(Çıkmak için 5 yazınız): ")
            if hrcm2 == "5":
                break
            hrcm2 = float(hrcm2)
            son_harcama_no += 1
            harcama_no = son_harcama_no
            look2 = Harcamalar[harcama_no] = {"Kategori": ktg2, "Miktar": hrcm2, "Tarih": bugun}
            print(f"Başarılı şekilde eklendi\n{look2}")

        elif menu0 == "3":
            hrcm3 = input("Lütfen Harcama Miktarını Giriniz(Çıkmak için 5 yazınız): ")
            if hrcm3 == "5":
                break
            hrcm3 = float(hrcm3)
            son_harcama_no += 1
            harcama_no = son_harcama_no
            look3 = Harcamalar[harcama_no] = {"Kategori": ktg3, "Miktar": hrcm3, "Tarih": bugun}
            print(f"Başarılı şekilde eklendi\n{look3}")

        elif menu0 == "4":
            break
        else:
            print("Lütfen Geçerli Bir İşlem seçiniz\n")


def gelir():
    global son_gelir_no
    while True:
        print("Kategori seç!")
        menu1 = input("""1) Maaş
2) Harçlık
3) Diğer
4) Çıkış
""")
        if menu1 == "1":
            hrcm1 = input("Lütfen Gelir Miktarını Giriniz(Çıkmak için 5 yazınız): ")
            if hrcm1 == "5":
                break
            hrcm1 = float(hrcm1)
            son_gelir_no += 1
            gelir_no = son_gelir_no
            look1 = Gelirler[gelir_no] = {"Kategori": ktg4, "Miktar": hrcm1, "Tarih": bugun}
            print(f"Başarılı şekilde eklendi\n{look1}")
        elif menu1 == "2":
            hrcm2 = input("Lütfen Gelir Miktarını Giriniz(Çıkmak için 5 yazınız): ")
            if hrcm2 == "5":
                break
            hrcm2 = float(hrcm2)
            son_gelir_no += 1
            gelir_no = son_gelir_no
            look2 = Gelirler[gelir_no] = {"Kategori": ktg5, "Miktar": hrcm2, "Tarih": bugun}
            print(f"Başarılı şekilde eklendi\n{look2}")
        elif menu1 == "3":
            hrcm3 = input("Lütfen Gelir Miktarını Giriniz(Çıkmak için 5 yazınız): ")
            if hrcm3 == "5":
                break
            hrcm3 = float(hrcm3)
            son_gelir_no += 1
            gelir_no = son_gelir_no
            look3 = Gelirler[gelir_no] = {"Kategori": ktg6, "Miktar": hrcm3, "Tarih": bugun}
            print(f"Başarılı şekilde eklendi\n{look3}")
        elif menu1 == "4":
            break
        else:
            print("Lütfen Geçerli Bir İşlem seçiniz\n")


def listele():
    if not Harcamalar:
        print("Henüz harcama yok!")
    else:
        print("\n--- Harcamalar ---")
        for no, bilgi in Harcamalar.items():
            print(f"{no}. Harcama")
            print(f"  Kategori: {bilgi['Kategori']}")
            print(f"  Miktar: {bilgi['Miktar']} TL")
            print(f"  Tarih: {bilgi['Tarih']}")
            print("-" * 20)


def gelir_listele():
    if not Gelirler:
        print("Henüz Gelir yok!")
    else:
        print("\n--- Gelirler ---")
        for no, bilgi in Gelirler.items():
            print(f"{no}. Gelir")
            print(f"  Kategori: {bilgi['Kategori']}")
            print(f"  Miktar: {bilgi['Miktar']} TL")
            print(f"  Tarih: {bilgi['Tarih']}")
            print("-" * 20)

def ana_menu():
    while True:
        menu = input("""1) Harcama ekle
2) Gelir ekle
3) Harcamaları listele
4)Gelirleri Listele
5) Çıkış
""")
        if menu == "1":
            harcama()
        elif menu == "2":
            gelir()
        elif menu == "3":
            listele()
        elif menu == "4":
            gelir_listele()
        elif menu == "5":
            print("Görüşürüz...")
            break

ana_menu()
