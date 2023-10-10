yes = ["Evet", "evet"]
no = ["Hayır", "hayır"]

girilen_ortalama = input("ortalamanızı yazınız.")

konusma_sorusu = input("Bu biraz zaman alabilir o sırada konuşmaya ne dersin? evet/hayır")
if konusma_sorusu in yes:
    ad = input("Adın ne?")
    soyad = input("Soyadın ne?")
    il = input("hangi ilde oturuyorsun?")
    input("İşlem bitti hadi cevaplara bakalım.")
if konusma_sorusu in no:
    input("İşlem bitti hadi cevaplara bakalım.")

if (girilen_ortalama < "50"):
    input("Birazcık ailenden utanmalısın dostum bu notlar ne biraz gayret et ve bu notlarını düzelt.")

elif(girilen_ortalama > "50" and girilen_ortalama < "80"):
    input("Evet dostum bu not mezun olman için iyi ama bilirsin aileni daha çok mutlu etmek için o lanet olası kıçını kaldır ve hemen çalışıp şu taktiri al! ")

elif(girilen_ortalama > "80" and girilen_ortalama < "100"):
    input("Tebrikler dostum sonunda şu lanet olası taktiri aldın ve aileni mutlu ettin tabi bunu 5 yıl sınıfta kalarak ypmakda ayrı bir güzellik ;)")
