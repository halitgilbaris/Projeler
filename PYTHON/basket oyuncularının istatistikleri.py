import numpy as np


average1 = 0
average2 = 0
average3 = 0
average4 = 0
average5 = 0
average6 = 0
average7 = 0
average8 = 0
average9 = 0

def player1():
    global average1, average2, average3   # global olarak işaretle
    number_statistics = np.random.randint(0, 30, (1,5))
    ribound_statistics = np.random.randint(0, 15, (1,5))
    assist_statistics = np.random.randint(0, 10, (1,5))
    
    average1 = np.mean(number_statistics)
    average2 = np.mean(ribound_statistics)
    average3 = np.mean(assist_statistics)
    
    print(f"""AVERAGE POINTS PLAYER 1
POINTS: {average1}
RIBOUND: {average2}
ASSIST: {average3}
""")
    print("---------------------------------------------------------------------------")


def player2():
    global average4, average5, average6 
    number_statistics = np.random.randint(0, 30, (1,5))
    ribound_statistics = np.random.randint(0, 15, (1,5))
    assist_statistics = np.random.randint(0, 10, (1,5))
    average4 = np.mean(number_statistics)
    average5 = np.mean(ribound_statistics)
    average6 = np.mean(assist_statistics)
    
    print(f"""AVERAGE POİNTS PLAYER 2 
POİNTS: {average4}
RİBOUND: {average5}
ASSİST: {average6}
          """)
    print("---------------------------------------------------------------------------")
    
def player3():
    global average7, average8, average9 
    number_statistics = np.random.randint(0, 30, (1,5))
    ribound_statistics = np.random.randint(0, 15, (1,5))
    assist_statistics = np.random.randint(0, 10, (1,5))
    average7 = np.mean(number_statistics)
    average8 = np.mean(ribound_statistics)
    average9 = np.mean(assist_statistics)

    print(f"""AVERAGE POİNTS PLAYER 3
POİNTS: {average7}
RİBOUND: {average8}
ASSİST: {average9}
          """)
    print("---------------------------------------------------------------------------")

player1()
print("\n")
player2()
print("\n")
player3()
print("\n")

all_points = np.array([average1, average4, average7])
all_point_players = np.argmax(all_points)
all_points = np.max(all_points)
print(f"BEST SCORER PERSON PLAYER {all_point_players + 1} ") 
print(f"POİNTS AVERAGE İS {all_points}\n")

all_ribound = np.array([average2, average5, average8])
all_ribound_players = np.argmax(all_ribound)
all_ribound = np.max(all_ribound)
print(f"BEST RİBOUND PERSON PLAYER {all_ribound_players + 1} ") 
print(f"RİBOUND AVERAGE İS {all_ribound}\n")

all_assist = np.array([average3, average6, average9])
all_assist_players = np.argmax(all_assist)
all_assist = np.max(all_assist)
print(f"BEST ASSİST PERSON PLAYER {all_assist_players + 1} ") 
print(f"ASSİST AVERAGE İS {all_assist}")
