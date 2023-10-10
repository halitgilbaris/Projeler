import time

print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")
time.sleep(0.3)
print("UYARI NOKTALAR VİRGÜLÜN YERİNE ALINMIŞTIR.")

D = ("dolar", "Dolar", "DOLAR")
E = ("euro", "Euro", "EURO")
S = ("Sterlin", "sterlin", "STERLİN")
T = ("Tl", "tl", "TL")
ED = float(1.08)
ET = float(28.66)
ES = float(0.86)
DE = float(0.93)
DS = float(0.79)
DT = float(26.55)
SD = float(1.26)
SE = float(1.17)
ST = float(33.40)
TD = float(0.038)
TE = float(0.035)
TS = float(0.030)

secilen_para_birimi = input("Para birimini seçiniz Dolar/Euro/Sterlin/TL: ")
neye_donussun = input("Lütfen hangi para birimine dönüşsün yazınız lütfen seçtiğiniz para birimini yazmayın Dolar/Euro/Sterlin/TL: ")
Kac = float(input("Lütfen elinizdeki para miktarını giriniz: "))

if secilen_para_birimi in E and neye_donussun in D:
    input(Kac * ED)
elif secilen_para_birimi in E and neye_donussun in T:
    input(Kac * ET)
elif secilen_para_birimi in E and neye_donussun in S:
    input(Kac * ES)
elif secilen_para_birimi in D and neye_donussun in E:
    input(Kac * DE)
elif secilen_para_birimi in D and neye_donussun in S:
    input(Kac * DS)
elif secilen_para_birimi in D and neye_donussun in T:
    input(Kac * DT)
elif secilen_para_birimi in S and neye_donussun in D:
    input(Kac * SD)
elif secilen_para_birimi in S and neye_donussun in E:
    input(Kac * SE)
elif secilen_para_birimi in S and neye_donussun in T:
    input(Kac * ST)
elif secilen_para_birimi in T and neye_donussun in D:
    input(Kac * TD)
elif secilen_para_birimi in T and neye_donussun in E:
    input(Kac * TE)
elif secilen_para_birimi in T and neye_donussun in S:
    input(Kac * TS)
else:
    input("Lütfen kelimeleri doğru karakter ile yazdığınızdan emin olun!")



