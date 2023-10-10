import sqlite3 as sq

cursor = sq.connect("conn.db")
print("Bağlantı başarılı")

cursor.execute("""CREATE TABLE KAYİTSİSTEMİ(
    İsim text,
    soyisim text,
    yaş integer,
    tc integer
)""")

add_command = """INSERT INTO KAYİTSİSTEMİ VALUES{}"""
data1 = ("Barış", "Halitgil", "15", "73789089382")
cursor.execute(add_command.format(data1))



cursor.commit()
cursor.close()
