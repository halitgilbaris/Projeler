import time
import re
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# ---------------- TARAYICI ----------------
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ---------------- ÜLKE ----------------
ulkeler = ["Russia","Portugal","Spanish","Serbia","Macedonia","Montenegro","Kosovo","Czech Republic","Slovakia",]
ulke_secim = random.choice(ulkeler)

# ---------------- ARAMA ----------------
arama_listesi = [
    "pvc window door handle company " + ulke_secim,
    #"pvc oor hardware company international",
    #"pvc door handle manufacturer international"
]

# ---------------- DATA ----------------
tum_sonuclar = []
ziyaret_edilen = set()

mail_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


# ---------------- MAIL ÇEK ----------------
def site_mail_al(url):
    try:
        driver.get(url)
        time.sleep(3)

        html = driver.page_source
        mails = re.findall(mail_regex, html)

        return list(set(mails))

    except:
        return []


# ---------------- GOOGLE TARAMA ----------------
for arama in arama_listesi:

    print("Aranıyor:", arama)

    driver.get(
        "https://www.google.com/search?q=" + arama.replace(" ", "+")
    )
    time.sleep(5)

    # ---- linkleri önce topla (stale fix) ----
    elements = driver.find_elements(By.CSS_SELECTOR, "a")

    site_linkleri = []

    for el in elements:
        try:
            href = el.get_attribute("href")

            if not href:
                continue

            if "google" in href:
                continue

            if href in ziyaret_edilen:
                continue

            ziyaret_edilen.add(href)
            site_linkleri.append(href)

        except:
            pass

    print("Bulunan link:", len(site_linkleri))

    # ---- sadece 10 site gez ----
    for site in site_linkleri[:50]:

        print("Siteye giriliyor:", site)

        mails = site_mail_al(site)

        if mails:
            tum_sonuclar.append({
                "site": site,
                "mailler": ", ".join(mails)
            })

        time.sleep(2)


driver.quit()

# ---------------- EXCEL ----------------
df = pd.DataFrame(tum_sonuclar)
df.to_excel("firmalar.xlsx", index=False)

print("✅ Bitti — bulunan firma:", len(df))
