import time

# Kullanıcılar
users = {
    "Barış": {"password": "2507Bhalitgil08", "Balance": 1000, "block_count":3, "is_locked":False},
    "Savaş": {"password": "252525", "Balance": 500, "block_count":3, "is_locked":False},
    "Kenan": {"password": "kenan_arkakapı69", "Balance": 500, "block_count":3, "is_locked":False}
}

# Blok süreleri (saniye)
LOCK_TIMES = [5, 10, 15]  # 1dk, 5dk, 1 saat

def login():
    username = input("Enter your username: ")
    if username not in users:
        print("User not found!")
        return login()  # tekrar sor

    user = users[username]

    while True:
        if user["is_locked"]:
            print("Your account is permanently locked. Contact admin!")
            while True:
                time.sleep(1)
                print("Account is locked!", end="\r")
        
        password = input("Enter your password: ")
        if password == user["password"]:
            print(f"Welcome {username}!")
            user["block_count"] = 3  # giriş başarılı, hakları sıfırla
            return user
        else:
            user["block_count"] -= 1
            print(f"Incorrect password! You have {user['block_count']} tries left.")

            # Blok süresi uygula
            if user["block_count"] > 0:
                lock_time = LOCK_TIMES[3 - user["block_count"] - 1]
                print(f"Account temporarily locked for {lock_time} seconds...")
                while lock_time > 0:
                    print(f"Remaining seconds: {lock_time}", end="\r")
                    time.sleep(1)
                    lock_time -= 1
            else:
                user["is_locked"] = True  # hak kalmadı, sonsuz kilit

def ATM(user):
    while True:
        choice = input("""\nATM Menu:
1-View Balance
2-Deposit
3-Withdraw
4-Exit
Enter choice: """)
        if choice == "1":
            print(f"Balance: {user['Balance']}")
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            user["Balance"] += amount
            print(f"New Balance: {user['Balance']}")
        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))
            if amount > user["Balance"]:
                print("Not enough balance!")
            else:
                user["Balance"] -= amount
                print(f"New Balance: {user['Balance']}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Program başlat
active_user = login()
ATM(active_user)
