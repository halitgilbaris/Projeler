import numpy as np

players = np.random.randint(0,100, (5,4))


average = np.mean(players, axis=1)
best_index = np.argmax(average)
best_score = np.max(average)


print("Players Scores:\n", players)
print(f"BEST SCORER PLAYER {best_index + 1} SCORE İS {best_score}")

index = 1
for i in average:
    print(f"PLAYER {index}: {i}")
    index += 1