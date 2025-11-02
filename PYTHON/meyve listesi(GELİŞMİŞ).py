import random

fruit_list = ["Apple", "Banana", "Peach", "Strawberry", "Mandarin","Grape"]

def menu():
    w = 1
    while w == 1 :
        # Fazla meyve kontrolü
        if len(fruit_list) > 6:
            response = input("\n\nOff you have so many fruits 😅. Do you want to give me some fruits (Yes or No)? ").strip()
            if response in ["Yes", "YES", "yes"]:
                print("Okay thanks, I will take some fruits :)")
                input("He takes 2 fruits...")
                random1 = random.sample(fruit_list, 2)
                for taken in random1:
                    fruit_list.remove(taken)
                print(f"Your new list: {fruit_list}\n\n")
            elif response in ["No", "NO", "no"]:
                input("So you don't give me your fruits?... ")
                print("HAHAHAHHAHAHAHAH LOLLLL")
                input("He takes 4 fruits...")
                random2 = random.sample(fruit_list, 4)
                for taken2 in random2:
                    fruit_list.remove(taken2)
                print(f"Your new list: {fruit_list}\n\n")
            else:
                input("HEY! YOU MUST RESPOND!!!") 
        
        # Menü
        question1 = input("""1-Add
2-Delete
3-View
4-Sort all fruits alphabetically
5-Quit
Select one bro:): """).strip()
        print("\n")
        if question1 == "1":
            add_fruit()
        elif question1 == "2":
            delete()
        elif question1 == "3":
            wiew()
        elif question1 == "4":
            Sort_all_fruits_alphabetically()
        elif question1 == "5":
            w = 0
        else:
            print("Please enter a valid option!")

def add_fruit():
    while True:
        print("(If you want to quit write Quit, QUİT, quit)")
        question2 = input("Please write the fruit you want to add: ").strip()
        if question2.isdigit():
            print("PLEASE ENTER FRUIT NAME!\n\n")
        elif question2 in ["QUİT", "Quit", "quit"]:
            print("Okay, exiting add menu.\n")
            break
        else:
            fruit_list.append(question2)
            print(f"Success! Your list: {fruit_list}")
            break

def delete():
    while True:
        print("(If you want to quit write Quit, QUİT, quit)")
        question3 = input("Please write the fruit you want to delete: ").strip()
        if question3.isdigit():
            print("PLEASE ENTER FRUIT NAME!\n\n")
        elif question3 in ["QUİT", "Quit", "quit"]:
            print("Okay, exiting delete menu.\n")
            break
        elif question3 in fruit_list:
            fruit_list.remove(question3)
            print(f"Success! Your list: {fruit_list}")
            break

def wiew():
    print(f"Your list: {fruit_list} \n\n")
    if len(fruit_list) < 3:
        print("POOR! 😅")
    else:
        print("LOOKS LIKE YOU ARE RICH! 😎")

def Sort_all_fruits_alphabetically():
    chance = random.randint(1, 100)
    if chance <= 80:
        fruit_list.sort()
        print(fruit_list)
        input("HMM PROBABLY YOU ARE UNEMPLOYED")
    else:
        input("HMMM YOU ARE REALLY UNEMPLOYED PLEASE ENTER")
        fruit_list.sort(reverse=True)
        print(fruit_list)

menu()
