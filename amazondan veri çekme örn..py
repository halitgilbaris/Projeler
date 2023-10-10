from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.amazon.com.tr/gp/bestsellers?ref_=nav_cs_bestsellers?ie=UTF8&tag=googlepcstdtr-21&hvadid=674177764078&hvpos=&hvexid=&hvnetw=g&hvrand=8693507102406041851&hvpone=&hvptwo=&hvqmt=e&hvdev=c&ref=pd_sl_2ihdf7d9tw_e&ext=6658-30510&ref=pd_sl_7r6v9rntlw_e&tag=trtxtgoabkde-21&hvpos=&hvnetw=g&hvrand=8693507102406041851&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012782&hvtargid=kwd-10573980&tag=trtxtgoabkde-21&ref=pd_sl_7r6v9rntlw_e&adgrpid=154611856018&hvpone=&hvptwo=&hvadid=674177764078&hvpos=&hvnetw=g&hvrand=8693507102406041851&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012782&hvtargid=kwd-10573980&hydadcr=12932_2354400&language=tr_TR&gclid=CjwKCAjwseSoBhBXEiwA9iZtxki2uELjzCGd-QNAPPuPRGW-MNFVGfJ80_ewolzCGp1MhZ-klq4RFxoC0WcQAvD_BwE")
soup = BeautifulSoup(r.content, "lxml")
header = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}6

urunler = soup.find_all("li",attrs={"class":"a-carousel-card"})
for urun in urunler:
    urun_linkleri = urun.find_all("div",attrs={"class":"zg-carousel-general-faceout"})
    for i in urun_linkleri:
        link = i.find("div",attrs={"class":"p13n-sc-uncoverable-faceout"})
        link_devam = link.a.get("href")
        link_basi = "https://www.amazon.com.tr"
        link_tamami = link_basi+link_devam

        detay = requests.get(link_tamami)
        detay_soup = BeautifulSoup(detay.content, "lxml")

        teknik_ayrintilar = detay_soup.find_all("div",attrs={"class":"a-row a-expander-container a-expander-extend-container"})

        for teknik in teknik_ayrintilar:
            detaylar = teknik.find_all("tr")
            for i in detaylar:
                etiket = i.find("th",attrs={"class":"a-color-secondary a-size-base prodDetSectionEntry"}).text
                deger = i.find("td",attrs={"class":"a-size-base prodDetAttrValue"}).text
                print(etiket,"=",deger,)







