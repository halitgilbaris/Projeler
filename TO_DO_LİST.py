import random

TO_DO_LIST = []
MOTIVE = ["Senin almaya cesaret edemediğin riskleri alanlar, senin yaşamak istediğin hayatı yaşarlar.",
          "Yüzüstü yere serilseniz bile, hala ileriye doğru hareket ediyorsunuzdur.",
          "Bırakma. Şimdi acı çek ve hayatının geri kalanını bir şampiyon olarak yaşa.",
          "Hazırlamayı başaramazsanız, başarısızlığa hazırlanıyorsunuz demektir!",
          "Eğer kendi yaşam planını tasarlamazsan, başkalarının planında kendine yer bulursun. Peki onların senin için ne planladığından haberin var mı?",
          "Yüksek bir hedefe giderken, size karşı olan insanların üstesinden gelmeniz gerekir!",
          "Başka bir hedef belirlemek ve yeni rüyalarını gerçekleştirmek için asla çok geç değil!",
          "Dünyada herkesin başarılı olabileceği bir iş bulunur, önemli olan insanda bulunan yeteneklerin ortaya çıkarılmasıdır. Her insan ayrı bir dünyadır, her dünya ise yeni bir yaşamdır.",
          "Ne istediğime karar verdim ve başarana kadar asla pes etmeyeceğim.",
          "Zaferin coşkusunu hissedebilmeniz için zorlukları kabul edin.", "Pes etmeyen kişiyi asla yenemezsin.",
          "Asla geri çekilme ve açıklama yapma. Bitir ve arkalarına bakmadan gitmelerini sağla!",
          "Ya büyük oyna ya da hiç oynama. Doğru olan şu ki kaybedecek hiçbir şeyin yok!",
          "Başarı yolunda karşına birçok zorluk çıkabilir. Yenilsen bile pes etmemeyi öğrendiğin zaman kazandın demektir.",
          "Sadece bir ayağını diğerinin önüne koymalısınız! Adım atmaya başlamak bu kadar basittir!",
          "Hiç kimse geriye gidip yeni bir başlangıç yapamaz; ama bugün yeni bir son yapıp yeniden başlayabilir.",
          "İlk önce izlerler. Başarınca nefret ederler. Sonra da taklit ederler.",
          "Dışınızda, içinizdeki güçten üstün olan hiçbir sorun yoktur.",
          "İyi yapılmış bir iş, iyi söylenmiş bir işten daha iyidir!"]
while True:
    vote = int(input("""Lütfen seçiminizi yapnız
          1-listeyi görüntüle
          2-yapılacaklar listesi(ekle)
          3-yapılacaklar listesi(çıkar)
          4-motivasyon
          5-görevleri yazdır
          6-çıkış
          """))

    if vote == 1:
        print(TO_DO_LIST)
    elif vote == 2:
        write = input("lütfen ekleyeceğiniz görevi yazın: ")
        TO_DO_LIST.append(write)
        print("görev listenize başarıyla eklenmiştir listeniz eklenen görev: " + write)
        print(TO_DO_LIST)
    elif vote == 3:
        write1 = input("lütfen çıkaracağınız görevi yazın: ")
        TO_DO_LIST.remove(write1)
        print("görev listenize başarıyla silinmiştir listeniz silinen görev: " + write1)
        print(TO_DO_LIST)
    elif vote == 4:
        print(random.choice(MOTIVE))
    elif vote == 5:
        misson = open("GÖREVLER.txt", "w")
        misson.write(str(TO_DO_LIST))
    elif vote == 6:
        break
    else:
        print("Lütfen doğru sayıyı girdiğinizden emin olun!")

