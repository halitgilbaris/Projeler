import random
import json

# -----------------------------
# Player Class
# -----------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.inventory = {}
        self.level = 1
        self.exp = 0

    def add_item(self, item, amount):
        self.inventory[item] = self.inventory.get(item, 0) + amount
        print(f"✅ {amount} {item} eklendi!")

    def remove_item(self, item, amount):
        if self.inventory.get(item, 0) >= amount:
            self.inventory[item] -= amount
            if self.inventory[item] == 0:
                del self.inventory[item]
            print(f"❌ {amount} {item} silindi!")
        else:
            print("⚠️ Envanterinde bu kadar yok!")

    def show_inventory(self):
        print("\n--- Envanter ---")
        if not self.inventory:
            print("Boş 😢")
        else:
            for item, amount in self.inventory.items():
                print(f"{item}: {amount}")
        print(f"💰 Para: {self.money}")
        print("----------------\n")

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            print(f"🎉 Level atladın! Şu an Level {self.level}")


# -----------------------------
# Shop Class
# -----------------------------
class Shop:
    def __init__(self):
        self.items = {"Apple": 10, "Banana": 15, "Peach": 20, "Strawberry": 25}

    def show_items(self):
        print("\n--- DÜKKAN ---")
        for item, price in self.items.items():
            print(f"{item} - {price}💰")
        print("----------------\n")

    def buy(self, player, item, amount):
        if item not in self.items:
            print("⚠️ Böyle bir ürün yok!")
            return
        total_price = self.items[item] * amount
        if player.money >= total_price:
            player.money -= total_price
            player.add_item(item, amount)
            player.gain_exp(10)
        else:
            print("💸 Paran yetmiyor!")

    def sell(self, player, item, amount):
        if item in player.inventory and player.inventory[item] >= amount:
            player.remove_item(item, amount)
            player.money += (self.items.get(item, 5) * amount) // 2
            print(f"💰 {amount} {item} sattın!")
            player.gain_exp(5)
        else:
            print("⚠️ Bu kadar eşyan yok!")


# -----------------------------
# Random Events
# -----------------------------
def random_event(player):
    events = [
        ("Bir maymun envanterinden 1 elma çaldı!", lambda: player.remove_item("Apple", 1)),
        ("Yolda 20💰 buldun!", lambda: setattr(player, "money", player.money + 20)),
        ("Yağmur yağdı, 2 muz yetişti!", lambda: player.add_item("Banana", 2)),
        ("Tüccar sana 10 exp verdi!", lambda: player.gain_exp(10))
    ]
    event = random.choice(events)
    print("🌟 OLAY: " + event[0])
    try:
        event[1]()
    except:
        print("Ama envanterinde yoktu 😅")


# -----------------------------
# Save / Load
# -----------------------------
def save_game(player):
    data = {
        "name": player.name,
        "money": player.money,
        "inventory": player.inventory,
        "level": player.level,
        "exp": player.exp
    }
    with open("save.json", "w") as f:
        json.dump(data, f)
    print("💾 Oyun kaydedildi!")


def load_game():
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
        player = Player(data["name"])
        player.money = data["money"]
        player.inventory = data["inventory"]
        player.level = data["level"]
        player.exp = data["exp"]
        print("📂 Kayıt yüklendi!")
        return player
    except FileNotFoundError:
        print("⚠️ Kayıt bulunamadı!")
        return None


# -----------------------------
# Main Game Loop
# -----------------------------
def main():
    print("=== FRUIT EMPIRE RPG ===")
    choice = input("1- Yeni Oyun\n2- Kaydı Yükle\nSeçim: ")

    if choice == "2":
        player = load_game()
        if not player:
            name = input("İsmini gir: ")
            player = Player(name)
    else:
        name = input("İsmini gir: ")
        player = Player(name)

    shop = Shop()

    while True:
        print("\n--- MENÜ ---")
        print("1- Envanteri Göster")
        print("2- Meyve Satın Al")
        print("3- Meyve Sat")
        print("4- Rastgele Olay")
        print("5- Kaydet")
        print("6- Çıkış")

        secim = input("Seçim yap: ")

        if secim == "1":
            player.show_inventory()
        elif secim == "2":
            shop.show_items()
            item = input("Hangi ürünü almak istiyorsun?: ")
            amount = int(input("Kaç tane?: "))
            shop.buy(player, item, amount)
        elif secim == "3":
            player.show_inventory()
            item = input("Hangi ürünü satmak istiyorsun?: ")
            amount = int(input("Kaç tane?: "))
            shop.sell(player, item, amount)
        elif secim == "4":
            random_event(player)
        elif secim == "5":
            save_game(player)
        elif secim == "6":
            print("👋 Görüşürüz!")
            break
        else:
            print("⚠️ Geçersiz seçim!")


if __name__ == "__main__":
    main()
