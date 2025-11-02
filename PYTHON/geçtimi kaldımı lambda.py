note1 = float(input("Please enter the note 1: "))
note2 = float(input("Please enter the note 2: "))
note3 = float(input("Please enter the note 3: "))

average = lambda note1, note2, note3: (note1 + note2 + note3) / 3
x = average(note1, note2, note3)
if x >= 50:
    print("Congratulations you pass the class!")
else:
    print("You dont pass the class!")
