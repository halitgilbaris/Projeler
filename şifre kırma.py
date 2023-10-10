from random import choice
sayilar = ("a", "b", "c", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
sifre = str(input("krilacak sifreyi giriniz"))
sifres = ""
adim=0
while True:
    print("sifreniz deneniyor...",sifres)

    if sifre == sifres:
        break

    else:
        sifres = ""

    for i in range(100):
            sifres += str(choice(sayilar))
            adim += 1

print("sifreniz krilmistir ",sifre,"adimda krilmis",adim)