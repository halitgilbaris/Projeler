# GUI/app.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import Qt, QTimer
from datetime import datetime, date
from veri import yukle, work, kaydet
from karakter import level_control

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("XP Oyunu GUI Full Havalı")
        self.setFixedSize(350, 450)

        self.veri = yukle()
        if not self.veri:
            self.veri = work()

        # Layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        # Level Label
        self.level_label = QLabel()
        self.level_label.setAlignment(Qt.AlignCenter)
        self.level_label.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.layout.addWidget(self.level_label)

        # XP Bar
        self.xp_bar = QProgressBar()
        self.xp_bar.setAlignment(Qt.AlignCenter)
        self.xp_bar.setTextVisible(True)
        self.layout.addWidget(self.xp_bar)

        # Streak
        self.streak_label = QLabel()
        self.streak_label.setAlignment(Qt.AlignCenter)
        self.streak_label.setStyleSheet("font-weight: bold; color: blue;")
        self.layout.addWidget(self.streak_label)

        # İstatistikler
        self.zeka_label = QLabel()
        self.guc_label = QLabel()
        self.disiplin_label = QLabel()
        self.odak_label = QLabel()
        for lbl in [self.zeka_label, self.guc_label, self.disiplin_label, self.odak_label]:
            lbl.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(lbl)

        # Butonlar
        self.btn_ders = QPushButton("Ders → +3 Zeka +10 XP")
        self.btn_spor = QPushButton("Spor → +3 Güç +10 XP")
        self.btn_kitap = QPushButton("Kitap → +2 Odak +8 XP")
        self.btn_kisisel = QPushButton("Kişisel Gelişim → +2 Disiplin +8 XP")
        for btn in [self.btn_ders, self.btn_spor, self.btn_kitap, self.btn_kisisel]:
            btn.setStyleSheet("""
                QPushButton {
                    padding: 6px; border-radius: 5px; background-color: lightgray;
                }
                QPushButton:hover {
                    background-color: lightblue;
                }
                QPushButton:pressed {
                    background-color: orange;
                }
            """)
            self.layout.addWidget(btn)

        # Buton sinyalleri
        self.btn_ders.clicked.connect(lambda: self.aktivite_yap("ders"))
        self.btn_spor.clicked.connect(lambda: self.aktivite_yap("spor"))
        self.btn_kitap.clicked.connect(lambda: self.aktivite_yap("kitap"))
        self.btn_kisisel.clicked.connect(lambda: self.aktivite_yap("kisisel"))

        # GUI’yi güncelle
        self.guncelle_gui()

    def aktivite_yap(self, aktivite):
        if aktivite == "ders":
            self.veri["istatistikler"]["zeka"] += 3
            self.veri["karakter"]["xp"] += 10
        elif aktivite == "spor":
            self.veri["istatistikler"]["guc"] += 3
            self.veri["karakter"]["xp"] += 10
        elif aktivite == "kitap":
            self.veri["istatistikler"]["odak"] += 2
            self.veri["karakter"]["xp"] += 8
        elif aktivite == "kisisel":
            self.veri["istatistikler"]["disiplin"] += 2
            self.veri["karakter"]["xp"] += 8

        # Tarihi güncelle ve streak kontrol
        bugun = date.today()
        son_giris = self.veri["karakter"].get("son_giris_tarihi")
        if son_giris != str(bugun):
            if son_giris:
                onceki_gun = datetime.fromisoformat(son_giris).date()
                fark = (bugun - onceki_gun).days
                if fark == 1:
                    self.veri["karakter"]["streak"] += 1
                else:
                    self.veri["karakter"]["streak"] = 1
            else:
                self.veri["karakter"]["streak"] = 1
        self.veri["karakter"]["son_giris_tarihi"] = str(bugun)

        # Level kontrol
        prev_level = self.veri["karakter"]["level"]
        level_control(self.veri)
        if self.veri["karakter"]["level"] > prev_level:
            # Level up efekti
            self.level_label.setStyleSheet("font-weight:bold; font-size:20px; color:orange;")
            QTimer.singleShot(800, lambda: self.level_label.setStyleSheet("font-weight:bold; font-size:18px; color:black;"))

        # Veriyi kaydet
        kaydet(self.veri)

        # GUI’yi güncelle (XP animasyonu)
        self.animate_xp(prev_level)

    def animate_xp(self, prev_level):
        k = self.veri["karakter"]
        # Eğer level atladıysa önce barı sıfırla
        if k["level"] > prev_level:
            self.xp_bar.setValue(0)

        # Basit animasyon: XP değerini yavaşça arttır
        target_xp = k["xp"]
        self.current_xp = 0
        def step():
            if self.current_xp < target_xp:
                self.current_xp += 1
                self.xp_bar.setValue(self.current_xp)
                # XP bar rengi
                if self.current_xp < k["xp_limit"]*0.5:
                    self.xp_bar.setStyleSheet("QProgressBar::chunk {background-color: yellow;}")
                elif self.current_xp < k["xp_limit"]:
                    self.xp_bar.setStyleSheet("QProgressBar::chunk {background-color: green;}")
                else:
                    self.xp_bar.setStyleSheet("QProgressBar::chunk {background-color: orange;}")
            else:
                timer.stop()
        timer = QTimer()
        timer.timeout.connect(step)
        timer.start(5)

        # Diğer label’ları da güncelle
        self.guncelle_labels()

    def guncelle_labels(self):
        k = self.veri["karakter"]
        s = self.veri["istatistikler"]

        self.level_label.setText(f"Level: {k['level']}")
        self.streak_label.setText(f"Streak: {k.get('streak', 0)} gün")
        self.zeka_label.setText(f"Zeka: {s['zeka']}")
        self.guc_label.setText(f"Güç: {s['guc']}")
        self.disiplin_label.setText(f"Disiplin: {s['disiplin']}")
        self.odak_label.setText(f"Odak: {s['odak']}")

    def guncelle_gui(self):
        # XP bar değerini direkt set etmeden sadece label ve bar max ayarları
        k = self.veri["karakter"]
        self.xp_bar.setMaximum(k["xp_limit"])
        self.guncelle_labels()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
