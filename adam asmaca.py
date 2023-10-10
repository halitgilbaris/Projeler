
import random

kelimeler = ["kedi", "köpek", "kablumbağa", "yunus", "balina", "fok", "arı", "atmaca", "güvercin", "aslan"]
secilen_kelime = random.choice(kelimeler)
gecerliHarfler = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
toplamHak = 5
yapilanTahmin = ""

# Oyun görselleri
ADAM_ASMACA_GORSLLERI = [
    """
      --------
      |    |
      |
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   /
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   / \
      |
    """
]

print("Adam Asmaca Oyununa Hoş Geldiniz!")

while toplamHak > 0:
    gercekKelime = ""
    for harf in secilen_kelime:
        if harf in yapilanTahmin:
            gercekKelime += harf
        else:
            gercekKelime += "_ "

    if gercekKelime == secilen_kelime:
        print(gercekKelime)
        print("Tebrikler kazandınız!")
        break

    print(ADAM_ASMACA_GORSLLERI[5 - toplamHak])
    print("Hayvan adını tahmin edin:", gercekKelime)
    print(f"Kalan hakkınız: {toplamHak}")

    tahmin = input("Bir harf tahmin edin: ").lower()

    if tahmin in gecerliHarfler:
        yapilanTahmin += tahmin
        if tahmin not in secilen_kelime:
            toplamHak -= 1
    else:
        print("Lütfen geçerli bir harf giriniz...")

else:
    print("Maalesef kaybettiniz. Doğru kelime:", secilen_kelime)