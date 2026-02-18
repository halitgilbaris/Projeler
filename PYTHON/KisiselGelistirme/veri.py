import json




DOSYA = "veriler.json"


def yukle():
    try:
        with open(DOSYA, 'r') as f:
            return json.load(f)
    except:
        return {}


def kaydet(veriler):
    with open(DOSYA, 'w') as f:
        json.dump(veriler, f, indent=4)


def work():

    veri = {
    "karakter": {
        "level": 0,
        "xp": 0,
        "xp_limit": 50,
        "son_giris_tarihi": ""
    },

    "istatistikler": {
        "zeka": 0,
        "guc": 0,
        "disiplin": 0,
        "odak": 0
    },

    "gecmis_kayitlar": []
}

    kaydet(veri)

    print("✅ Kaydedildi.")
    return veri
        


    