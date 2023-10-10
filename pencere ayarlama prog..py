import tkinter as tk
import random as rd

pencere = tk.Tk()
pencere.title("Ders")
pencere.geometry("500x500+350+250")
liste=[]
for i in range(5):
    while len(liste)!=6:
        a = rd.randint(1, 50)
        if a not in liste:
            liste.append(a)
def goster():
    label.config(text="liste",bg="green")
def saydamlastir():
    pencere.wm_attributes("-alpha",0.5)
def dondur():
    pencere.wm_attributes("-alpha", 0.9)

def maxyap():
    pencere.state("zoomed")
def minyap():
    pencere.state("iconic")

label = tk.Label(fg="red",bg="red",font="times 20 bold")
label.pack()

goster = tk.Button(text="göster", fg="black",bg="yellow",command=goster)
goster.pack(side=tk.LEFT)
goster = tk.Button(text="saydamlaştır", fg="black",bg="yellow",command=saydamlastir)
goster.pack(side=tk.LEFT)
goster = tk.Button(text="döndür", fg="black",bg="yellow",command=dondur)
goster.pack(side=tk.LEFT)
goster = tk.Button(text="max yap", fg="black",bg="yellow",command=maxyap)
goster.pack(side=tk.LEFT)
goster = tk.Button(text="min yap", fg="black",bg="yellow",command=minyap)
goster.pack(side=tk.LEFT)


pencere.mainloop()