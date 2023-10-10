def BMI():
    Boy = float(input("Lütfen Boyunuzu Giriniz: "))
    Kilo = int(input("Lütfen Kilonuzu Giriniz: "))
    bmi = float((Kilo / (Boy * Boy)))
    print(bmi)
    pass


while True:
    panel = int(input("1 - BMI Hesaplama\n2 - Çıkış\n>>"))
    if panel == 1:
        BMI()
    elif panel == 2:
        break
