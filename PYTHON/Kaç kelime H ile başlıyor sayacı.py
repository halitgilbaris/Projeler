message1 = "Hello"
message2 = "Hi"
message3 = "Me"
message4 = "Hidden"
message5 = "Seria"
message6 = "Hah"


message_box = [message1, message2, message3, message4, message5, message6]

count = 0

for msg in message_box:
    if msg.startswith("H"):
        count += 1
        print(f"+{count}")