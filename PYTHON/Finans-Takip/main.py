import sys
import os
import json
import re
import tempfile
from datetime import datetime
from collections import defaultdict
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QWidget, QPushButton,
                             QDialog, QFormLayout, QLineEdit, QComboBox, QDialogButtonBox,
                             QHBoxLayout, QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# ---------------------------- GÜVENLİ DİZİN & DOSYA AYARI ----------------------------
# Uygulama verilerini kullanıcı belgeler klasöründe sakla (güvenli yer)
APP_DIR = os.path.join(os.path.expanduser("~"), "Documents", "FinansTakipApp")
os.makedirs(APP_DIR, exist_ok=True)

DOSYA = os.path.join(APP_DIR, "veriler.json")

# Yardımcı: dosya adı güvenli hale getir
def sanitize_filename(name: str, maxlen: int = 100) -> str:
    name = name.strip()
    # sadece izin verilen karakterler
    name = re.sub(r"[^A-Za-z0-9 _\-\.]", "_", name)
    return name[:maxlen]

# Yardımcı: text girdisinden kontrol karakterlerini temizle
def sanitize_text(s: str, maxlen: int = 100) -> str:
    if s is None:
        return ""
    s = str(s)
    s = re.sub(r"[\x00-\x1f\x7f]", "", s)  # kontrol karakterlerini kaldır
    return s.strip()[:maxlen]

# JSON'in güvenli yüklenmesi
def load_data():
    if not os.path.exists(DOSYA):
        return []
    try:
        with open(DOSYA, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                # basit doğrulama - beklenen alanlar var mı
                clean = []
                for item in data:
                    if not isinstance(item, dict):
                        continue
                    tarih = sanitize_text(item.get("tarih", ""))
                    tip = sanitize_text(item.get("tip", ""))
                    kategori = sanitize_text(item.get("kategori", ""))
                    try:
                        miktar = float(item.get("miktar", 0))
                    except Exception:
                        miktar = 0.0
                    clean.append({"tarih": tarih, "tip": tip, "kategori": kategori, "miktar": miktar})
                return clean
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []

# Atomik güvenli yazma: önce geçici dosyaya yaz, sonra replace
def safe_write_json(path, data):
    try:
        dirn = os.path.dirname(path)
        os.makedirs(dirn, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(prefix="tmp_", dir=dirn, text=True)
        os.close(fd)
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        os.replace(tmp_path, path)
        return True, ""
    except Exception as e:
        return False, str(e)

# ---------------------------- VERİLER ----------------------------
islemler = load_data()

# ---------------------------- FORM ----------------------------
class IslemForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni İşlem Ekle")
        self.setGeometry(200, 200, 420, 280)
        self.setStyleSheet("""
            QDialog {background-color: #2b2d42; border-radius: 10px;}
            QLabel {color: #edf2f4; font-size: 14px; font-family: 'Segoe UI';}
            QLineEdit, QComboBox {font-size: 14px; padding: 8px; border-radius: 6px; font-family: 'Segoe UI';}
            QLineEdit {background-color: #8d99ae; color: white; border: none;}
            QComboBox {background-color: #8d99ae; color: white; border: none;}
        """)

        layout = QFormLayout()
        self.setLayout(layout)

        self.tip_input = QComboBox()
        self.tip_input.addItems(["gelir", "gider"])
        self.tip_input.setToolTip("İşlemin türünü seçin: gelir veya gider")
        layout.addRow("Tip:", self.tip_input)

        self.kategori_input = QLineEdit()
        self.kategori_input.setToolTip("İşlemin kategorisini yazın, örn: Maaş, Market")
        layout.addRow("Kategori:", self.kategori_input)

        self.miktar_input = QLineEdit()
        self.miktar_input.setToolTip("İşlemin miktarını yazın, sayısal değer olmalı")
        layout.addRow("Miktar:", self.miktar_input)

        self.tarih_input = QLineEdit()
        self.tarih_input.setPlaceholderText("YYYY-AA-GG (boşsa bugünün tarihi)")
        self.tarih_input.setToolTip("Tarihi YYYY-AA-GG formatında yazın, boş bırakırsanız bugünün tarihi atanır")
        layout.addRow("Tarih:", self.tarih_input)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.setStyleSheet("""
            QPushButton {background-color: #ef233c; color: white; padding: 8px 16px; border-radius: 6px;}
            QPushButton:hover {background-color: #d90429;}
        """)
        layout.addWidget(self.buttons)

        self.buttons.accepted.connect(self.validate_and_accept)
        self.buttons.rejected.connect(self.reject)

    def validate_and_accept(self):
        tip = self.tip_input.currentText()
        kategori = sanitize_text(self.kategori_input.text(), maxlen=60)
        miktar_text = self.miktar_input.text().strip()
        tarih = self.tarih_input.text().strip()

        if not kategori:
            QMessageBox.information(self, "Kategori Eksik",
                                    "Lütfen işlemin kategorisini yazın.\nÖrnek: 'Maaş', 'Market', 'Fatura'")
            return

        if len(kategori) > 60:
            QMessageBox.information(self, "Kategori Uzun",
                                    "Kategori çok uzun. En fazla 60 karakter girin.")
            return

        if not miktar_text:
            QMessageBox.information(self, "Miktar Eksik",
                                    "Lütfen işlemin miktarını girin.\nSadece sayısal değer kabul edilir.")
            return

        try:
            miktar = float(miktar_text)
        except ValueError:
            QMessageBox.information(self, "Miktar Hatalı",
                                    "Miktar sayısal olmalı.\nÖrnek: 2500, 125.50")
            return

        # miktar makul sınırlar içinde mi?
        if abs(miktar) > 1e12:
            QMessageBox.information(self, "Miktar Aşırı",
                                    "Miktar çok büyük veya hatalı görünüyor.")
            return

        if not tarih:
            tarih = datetime.now().strftime("%Y-%m-%d")
        else:
            try:
                datetime.strptime(tarih, "%Y-%m-%d")
            except ValueError:
                QMessageBox.information(self, "Tarih Hatalı",
                                        "Tarih formatı yanlış!\nDoğru format: YYYY-AA-GG\nÖrnek: 2025-09-14")
                return

        self.tip = tip
        self.kategori = kategori
        self.miktar = miktar
        self.tarih = tarih
        self.accept()

# ---------------------------- ANA PENCERE ----------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finans Takip Dashboard")
        self.setGeometry(100, 100, 1250, 750)
        self.setStyleSheet("""
            QMainWindow {background-color: #1f2937;}
            QLabel#title {font-size: 34px; font-weight: bold; color: #ffffff; font-family: 'Segoe UI';}
            QPushButton {
                font-size: 15px;
                padding: 12px 22px;
                background-color: #4caf50;
                color: white;
                border-radius: 10px;
                font-family: 'Segoe UI';
            }
            QPushButton:hover {background-color: #45a049;}
            QTableWidget {
                font-size: 14px;
                background-color: #f8f9fa;
                color: #222222;
                gridline-color: #e0e0e0;
                font-family: 'Segoe UI';
                border-radius: 8px;
            }
            QTableWidget::item:selected {background-color: #c8e6c9; color: #000000;}
            QHeaderView::section {
                background-color: #4caf50;
                color: white;
                font-weight: bold;
                height: 34px;
                font-family: 'Segoe UI';
            }
            QLineEdit {padding: 6px; border-radius: 6px; border: 1px solid #cccccc;}
            QComboBox {padding: 6px; border-radius: 6px;}
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 30, 30, 30)
        self.layout.setSpacing(20)
        self.central_widget.setLayout(self.layout)

        # Başlık
        self.label = QLabel("Finans Takip Dashboard")
        self.label.setObjectName("title")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Arama ve Filtreleme
        self.filter_layout = QHBoxLayout()
        self.layout.addLayout(self.filter_layout)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("İşlem ara (Kategori veya Tip)")
        self.search_input.textChanged.connect(self.apply_filters)
        self.filter_layout.addWidget(self.search_input)

        self.tip_filter = QComboBox()
        self.tip_filter.addItems(["Hepsi", "gelir", "gider"])
        self.tip_filter.currentIndexChanged.connect(self.apply_filters)
        self.filter_layout.addWidget(self.tip_filter)

        self.kategori_filter = QComboBox()
        self.kategori_filter.addItem("Hepsi")
        self.kategori_filter.addItems(sorted(list({i["kategori"] for i in islemler})))
        self.kategori_filter.currentIndexChanged.connect(self.apply_filters)
        self.filter_layout.addWidget(self.kategori_filter)

        # Tablo
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.setShowGrid(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)
        self.load_table()

        # Butonlar
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(16)
        self.layout.addLayout(self.button_layout)

        self.add_button = QPushButton("Yeni İşlem Ekle")
        self.add_button.clicked.connect(self.open_islem_form)
        self.button_layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Seçili İşlemi Sil")
        self.delete_button.clicked.connect(self.delete_selected)
        self.button_layout.addWidget(self.delete_button)

        self.graph_button = QPushButton("Gelir-Gider Grafiği")
        self.graph_button.clicked.connect(self.show_graph)
        self.button_layout.addWidget(self.graph_button)

        self.trend_button = QPushButton("Ay Bazlı Trend Grafiği")
        self.trend_button.clicked.connect(self.show_trend_graph)
        self.button_layout.addWidget(self.trend_button)

        self.report_button = QPushButton("Raporla / Toplam Göster")
        self.report_button.clicked.connect(self.show_report)
        self.button_layout.addWidget(self.report_button)

        self.export_button = QPushButton("CSV Dışa Aktar")
        self.export_button.clicked.connect(self.export_csv)
        self.button_layout.addWidget(self.export_button)

    # -------------------- TABLOYU YÜKLEME --------------------
    def load_table(self):
        self.table.clear()
        self.table.setRowCount(len(islemler))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Tarih", "Tip", "Kategori", "Miktar"])
        for row, islem in enumerate(islemler):
            self.table.setItem(row, 0, QTableWidgetItem(islem.get("tarih", "")))
            self.table.setItem(row, 1, QTableWidgetItem(islem.get("tip", "")))
            self.table.setItem(row, 2, QTableWidgetItem(islem.get("kategori", "")))
            self.table.setItem(row, 3, QTableWidgetItem(str(islem.get("miktar", 0))))
        # Kategori filtresi güncelle
        self.kategori_filter.clear()
        self.kategori_filter.addItem("Hepsi")
        self.kategori_filter.addItems(sorted(list({i.get("kategori", "") for i in islemler})))

    # -------------------- FİLTRE UYGULAMA --------------------
    def apply_filters(self):
        tip = self.tip_filter.currentText()
        kategori = self.kategori_filter.currentText()
        search_text = self.search_input.text().lower()

        for row in range(self.table.rowCount()):
            item_tip = self.table.item(row, 1).text()
            item_kategori = self.table.item(row, 2).text()
            item_match = search_text in item_tip.lower() or search_text in item_kategori.lower()

            tip_match = (tip == "Hepsi" or item_tip == tip)
            kategori_match = (kategori == "Hepsi" or item_kategori == kategori)

            self.table.setRowHidden(row, not (tip_match and kategori_match and item_match))

    # -------------------- RAPORLAMA --------------------
    def show_report(self):
        total_gelir = sum(i.get("miktar", 0) for i in islemler if i.get("tip") == "gelir")
        total_gider = sum(i.get("miktar", 0) for i in islemler if i.get("tip") == "gider")
        net = total_gelir - total_gider
        QMessageBox.information(self, "Rapor", f"Toplam Gelir: {total_gelir}\nToplam Gider: {total_gider}\nNet Bakiye: {net}")

    # -------------------- CSV DIŞA AKTARMA (GÜVENLİ) --------------------
    def export_csv(self):
        import csv
        # Başlangıç dizini güvenli App dizini
        start_dir = APP_DIR
        # Kullanıcıdan dosya adı seçtirelim ama kaydetme konumunu sınırlayacağız
        path, _ = QFileDialog.getSaveFileName(self, "CSV Kaydet", start_dir, "CSV Files (*.csv)")
        if not path:
            return

        # Zorunlu .csv uzantısı
        if not path.lower().endswith(".csv"):
            path = path + ".csv"

        # Eğer kullanıcı farklı bir dizine kaydetmeye çalışıyorsa, onu engelle veya uyar
        norm_app = os.path.normpath(os.path.abspath(APP_DIR))
        norm_path = os.path.normpath(os.path.abspath(path))
        if not norm_path.startswith(norm_app):
            # kullanıcı farklı yere kaydetmeye çalıştıysa: uyar ve APP_DIR içine güvenli dosya adıyla kaydet
            QMessageBox.warning(self, "Güvenlik Uyarısı",
                                "Dosya yalnızca uygulama klasörü içine kaydedilebilir. Güvenli bir dosyaya kaydediliyor.")
            fname = os.path.basename(norm_path)
            fname = sanitize_filename(fname, maxlen=80)
            if not fname.lower().endswith(".csv"):
                fname += ".csv"
            path = os.path.join(APP_DIR, fname)

        try:
            # atomik yazma: önce temp sonra replace
            fd, tmp = tempfile.mkstemp(suffix=".csv", dir=APP_DIR, text=True)
            os.close(fd)
            with open(tmp, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Tarih", "Tip", "Kategori", "Miktar"])
                for row in range(self.table.rowCount()):
                    if not self.table.isRowHidden(row):
                        writer.writerow([
                            self.table.item(row, 0).text(),
                            self.table.item(row, 1).text(),
                            self.table.item(row, 2).text(),
                            self.table.item(row, 3).text()
                        ])
            os.replace(tmp, path)
            QMessageBox.information(self, "Başarılı", f"CSV dosyası başarıyla kaydedildi:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"CSV kaydederken hata oluştu:\n{e}")

    # -------------------- TABLO ARAMA --------------------
    def search_table(self, text):
        for row in range(self.table.rowCount()):
            match = False
            for col in range(1,3):
                item = self.table.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.table.setRowHidden(row, not match)

    # -------------------- FORM AÇ --------------------
    def open_islem_form(self):
        form = IslemForm()
        if form.exec_() == QDialog.Accepted:
            yeni_islem = {
                "tarih": form.tarih,
                "tip": form.tip,
                "kategori": form.kategori,
                "miktar": form.miktar
            }

            islemler.append(yeni_islem)
            ok, err = safe_write_json(DOSYA, islemler)
            if not ok:
                QMessageBox.critical(self, "Hata", f"Veri kaydedilemedi:\n{err}")
            self.load_table()

    # -------------------- SEÇİLİ SATIRI SİL --------------------
    def delete_selected(self):
        selected = self.table.currentRow()
        if selected >= 0:
            reply = QMessageBox.question(
                self, "Onay", "Bu işlemi silmek istediğinize emin misiniz?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                try:
                    islemler.pop(selected)
                    ok, err = safe_write_json(DOSYA, islemler)
                    if not ok:
                        QMessageBox.critical(self, "Hata", f"Veri kaydedilemedi:\n{err}")
                    self.load_table()
                except Exception as e:
                    QMessageBox.critical(self, "Hata", f"Silme sırasında hata oluştu:\n{e}")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen silmek için bir satır seçin!")

    # -------------------- GELİR-GİDER GRAFİĞİ --------------------
    def show_graph(self):
        gelir = sum(i.get("miktar", 0) for i in islemler if i.get("tip") == "gelir")
        gider = sum(i.get("miktar", 0) for i in islemler if i.get("tip") == "gider")

        self.graph_window = QMainWindow()
        self.graph_window.setWindowTitle("Gelir-Gider Grafiği")
        self.graph_window.setGeometry(200, 200, 700, 500)

        fig, ax = plt.subplots()
        ax.bar(["Gelir", "Gider"], [gelir, gider], color=["#4caf50", "#ef233c"])
        ax.set_ylabel("Miktar")
        ax.set_title("Gelir-Gider Grafiği")
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, self.graph_window)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(canvas)
        central_widget.setLayout(layout)

        self.graph_window.setCentralWidget(central_widget)
        self.graph_window.show()

    # -------------------- AY BAZLI TREND GRAFİĞİ --------------------
    def show_trend_graph(self):
        aylar = defaultdict(lambda: {"gelir":0,"gider":0})
        for i in islemler:
            ay = i.get("tarih", "")[:7]
            aylar[ay][i.get("tip", "")] += i.get("miktar", 0)

        ay_list = sorted([a for a in aylar.keys() if a])
        gelir_list = [aylar[a]["gelir"] for a in ay_list]
        gider_list = [aylar[a]["gider"] for a in ay_list]

        self.trend_window = QMainWindow()
        self.trend_window.setWindowTitle("Ay Bazlı Trend Grafiği")
        self.trend_window.setGeometry(200, 200, 800, 500)

        fig, ax = plt.subplots()
        ax.plot(ay_list, gelir_list, label="Gelir", marker='o', color="#4caf50")
        ax.plot(ay_list, gider_list, label="Gider", marker='o', color="#ef233c")
        ax.set_xlabel("Ay")
        ax.set_ylabel("Miktar")
        ax.set_title("Ay Bazlı Gelir-Gider Trend Grafiği")
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()

        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, self.trend_window)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(canvas)
        central_widget.setLayout(layout)

        self.trend_window.setCentralWidget(central_widget)
        self.trend_window.show()


# ---------------------------- UYGULAMA ----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
