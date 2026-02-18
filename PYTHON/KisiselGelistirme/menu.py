from datetime import datetime
from karakter import level_control
from karakter import karakter_durumu
from veri import kaydet
from veri import work
from veri import yukle

def menu(veri):
    while True:
        menu_secim = input("""
    1- Bugün yaptığım şeyi ekle
    2- Karakter durumum
    3- Çıkış
""")
        if menu_secim == "1":
            aktivite_secim = input("""
    1-Ders → +3zeka +10xp
    2-Spor → +3guc +10xp
    3-Kitap → +2odak +8xp
    4-Kisisel Gelisim → +2disiplin +8xp
""")
            if aktivite_secim == "1":
                print("DERS CALISTIN VE 3 ZEKA 10XP PUANI ALIDN!")
                veri["istatistikler"]["zeka"] += 3
                veri["karakter"]["xp"] += 10
                tarih = str(datetime.now().date())
                veri["karakter"]["son_giris_tarihi"] = tarih
                level_control(veri)
                kaydet(veri)
            elif aktivite_secim == "2":
                print("SPOR YAPTIN VE 3 GUC 10XP PUANI ALIDN!")
                veri["istatistikler"]["guc"] += 3
                veri["karakter"]["xp"] += 10
                tarih = str(datetime.now().date())
                veri["karakter"]["son_giris_tarihi"] = tarih
                level_control(veri)
                kaydet(veri)
            elif aktivite_secim == "3":
                print("KITAP OKUDUN VE 2 ODAK 8XP PUANI ALIDN!")
                veri["istatistikler"]["odak"] += 2
                veri["karakter"]["xp"] += 8
                tarih = str(datetime.now().date())
                veri["karakter"]["son_giris_tarihi"] = tarih
                level_control(veri)
                kaydet(veri)
            elif aktivite_secim == "4":
                print("KISISEL GELISIME CALISTIN VE 2 DISIPLIN 8XP PUANI ALIDN!")
                veri["istatistikler"]["disiplin"] += 2
                veri["karakter"]["xp"] += 8
                tarih = str(datetime.now().date())
                veri["karakter"]["son_giris_tarihi"] = tarih
                level_control(veri)
                kaydet(veri)
        elif menu_secim == "2":
            karakter_durumu(veri)
        elif menu_secim == "3":
            kaydet(veri)
            break
        

if __name__ == "__main__":
    veri = yukle()
    if veri == {}:
        veri = work()
    menu(veri)
    
    
    