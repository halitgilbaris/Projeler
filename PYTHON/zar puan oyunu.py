import numpy as np 

zar = np.random.randint(1, 7, (3,10))

oyuncular = np.mean(zar, axis=1)
best_player = np.argmax(oyuncular)
best_scorer = np.max(oyuncular)
total_points = np.sum(oyuncular)


print(f"TOPLAM PUAN: {total_points}")

for i,avg in enumerate(oyuncular):
    print(f"OYUNCU {i + 1} PUANI: {avg}")
    
fark = best_scorer - np.sort(oyuncular)[-2]
print(f"KAZANAN: OYUNCU {best_player + 1}\nPUANI: {best_scorer}\nFARK: {fark}")


