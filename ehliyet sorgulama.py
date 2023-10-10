girilenyas = int(input("Lütfen yaşınızı giriniz:"))

if (girilenyas > 15 and girilenyas < 18):
    input("M, A1 ve B1 sınıfı ehliyetlerİ alabilirsiniz.")
elif (girilenyas > 17 and girilenyas < 21):
    input("M, A1, B1, A2, B, BE, C1, C1E, F ve G sınıfı ehliyetlerİ alabilirsiniz.")
elif (girilenyas > 20 and girilenyas < 24):
    input("M, A1, B1, A2, B, BE, C1, C1E, F, G, C, CE, D1 ve D1E sınıfı ehliyetlerİ alabilirsiniz.")
elif (girilenyas > 23 and girilenyas < 60):
    input("M, A1, B1, A2, B, BE, C1, C1E, F, G, C, CE, D1, D1E, D ve DE sınıfı ehliyetlerİ alabilirsiniz.")
else:
    input("Üzgünüz ancak yaşınız ehliyet için uygun değil.")