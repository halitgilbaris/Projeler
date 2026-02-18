from veri import kaydet


def level_control(veri):
    while veri["karakter"]["xp"] >= veri["karakter"]["xp_limit"]:
        veri["karakter"]["xp"] -= veri["karakter"]["xp_limit"]
        veri["karakter"]["level"] += 1
        veri["karakter"]["xp_limit"] = 100 + veri["karakter"]["level"] * 5
        print("🔥 LEVEL ATLADIN!")
    kaydet(veri)
    
def karakter_durumu(veri):
    k = veri["karakter"]
    s = veri["istatistikler"]

    print("\n===== KARAKTER DURUMU =====")
    print(f"Level : {k['level']}")
    print(f"XP    : {k['xp']} / {k['xp_limit']}")
    print(f"Streak: {k['streak']} gün")

    print("\n--- İSTATİSTİKLER ---")
    print(f"Zeka      : {s['zeka']}")
    print(f"Güç       : {s['guc']}")
    print(f"Disiplin  : {s['disiplin']}")
    print(f"Odak      : {s['odak']}")
   