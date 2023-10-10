soru1 = input("Öğrenci misiniz?E/H")
soru2 = input("Sinemaya mı gitmek istersin tiyatroya mı?")

if soru1 == "E":
    input("Öğrenci olduğunuz için indirim alacaksiniz.")
else:
    input("Öğrenci olmadığınız için indirim almayacaksiniz.")

if soru2 == "sinema" or "Sinema" and soru1 == "E":
    input("Ücretiniz 7,5TL")
elif soru2 == "sinema" or "Sinema" and soru1 == "H":
        input("Ücretiniz 15TL")
elif soru2 == "Tiyatro" or "tiyatro" and soru1 == "E":
        input("Ücretiniz 5TL")
elif soru2 == "Tiyatro" or "tiyatro" and soru1 == "H":
    input("Ücretiniz 10TL")
