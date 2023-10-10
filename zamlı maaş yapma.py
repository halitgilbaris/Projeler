# Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren Python örneği

while True:
    MAAS = int(input("maaşı girin"))
    ZAM_ORANI = int(input("zam oranı(%)"))
    YENI_MAAS = int(MAAS) + int(MAAS)*int(ZAM_ORANI)/100

    print("Zamlı maaş: ", YENI_MAAS)