import tkinter as tk
import random as rd


#Variables constantes
N = 30
HEIGHT = 900
WIDTH = 900

#Variables globales
Npro = 80
Apro = 5

Npre = 5
Apre = 10
Epre = 10
Erepro = 15

chrono = 750

#Dictionnaire couleurs
colors = {0:"white", 1:"green", 2:"red"}

#Tuples proies et prédateurs
proie = (1, Apro, 0, 0)
predateur = (2, Apre, Epre, Erepro)


#Listes
liste = []

def listes():
    for i in range(N) :
        liste.append([])
    for j in range(N) :
        liste[i].append(0)


#Fonctions

def display() :#Affiche les proies et les prédateurs sur la grille
     for i in range(N) :
        for j in range(N) :
            canvas.itemconfigure(cases[i][j], fill=colors[liste[i+1][j+1][0]])#itemconfigure permet de changer la couleur, si liste[i+1][j+1][0] correspond a une proie (1), couleur = green et de meme pour le prédateur


def move():#Permet le déplacement des proies et des prédateurs
    global liste, liste2, cpt, i
    liste2 = liste
    for i in range(len(liste)) :
        cpt = 0
        for j in liste[i] :
            if j[0] == 0 or j[0] == 3 :
                cpt += 1
                continue
            if j[0] == 1 :
                cases(liste, i-1, i+1, cpt-1, cpt+1, liste[i][cpt])
                liste2[i][cpt] = (0, 0)
                liste2[line][column] = j
                cpt += 1
            if j[0] == 2 :
                cases(liste, i-1, i+1, cpt-1, cpt+1, liste[i][cpt])
                if test == True :
                    liste2[i][cpt] = (0, 0)
                    liste2[line][column] = j
                cpt += 1
    liste = liste2
    display()
    return liste


def cases(liste, x1, y1, x2, y2, position_init):#Fonction qui permet de ne pas faire apparaitre un prédateur ou une proie sur une case si elle est déja occupé
    global line
    global column
    global test
    test = True
    boucle = True
    line = rd.randint(x1, y1)
    column = rd.randint(x2, y2)
    while liste[line][column] != (0, 0) and boucle == True :
        line = rd.randint(x1, y1)
        column = rd.randint(x2, y2)
        if position_init != None and line == i and  column == cpt :
            boucle = False
        if position_init != None and liste[i][cpt][0] == 2 and liste[line][column][0] == 1 :
            liste[line][column] = (liste[i][cpt][0], liste[i][cpt][1], liste[i][cpt][2], liste[i][cpt][3])
            liste[i][cpt] = (0, 0)
            test = False
    return line, column, liste, test


def pred_repro():
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j][0] != 2 :
                continue
            if liste[i][j][0] >= Epre:
                liste[i][j] = (liste[i][j][0], liste[i][j][1], liste[i][j][2]-Erepro, liste[i][j][3])#Si le prédateur n'a pas assez d'energie, on crée un nouveau prédateur(ligne en dessous) et on retire Erepro.
                cases(liste, 1, N, 1, N)
                liste[line][column] = predateur
    return liste


def faim():
    for i in range(len(liste)) :
        for j in range(len(liste)) :
            if liste[i][j][0] != 2 :
                continue
            else :
                liste[i][j] = (liste[i][j][0], liste[i][j][1], liste[i][j][2]-1, liste[i][j][3])
            if liste[i][j][2] <= 0 :
                liste[i][j] = (0, 0)
    return liste    

def age():
    for i in range(len(liste)) :
        for j in range(len(liste)) :
            if liste[i][j][0] == 0:
                continue
            elif liste[i][j][0] == 3:
                continue
            liste[i][j] = (liste[i][j][0], liste[i][j][1]-1, liste[i][j][2], liste[i][j][3]) #On retire -1 au second élement du tuple proie ou prédateurs qui correspond a l'age
            if liste[i][j][0] != 0 and liste[i][j][1] <= 0 :#On initialise les coordonées a (0,0) si la proie ou le prédateur a un age négatif
                liste[i][j] = (0, 0)
    return liste



def boutton():#fonction qui permet d'enclencher toutes les fonctions
    move()
    pred_repro()
    age()
    faim()
    display()

def tours():
    global chrono
    chrono = canvas.after(chrono, boutton())#Permets de passer les tours automatiquement

def re


():#Permets de reinitialiser la grille et les proies/prédateurs
    listes()
    grille = []
    for i in range(N) :
        liste.append([])
    for j in range(N) :
        liste[i].append(canvas.create_rectangle(i * (WIDTH/N), j * (HEIGHT/N), i * (WIDTH/N) + WIDTH/N, j * (HEIGHT/N) + HEIGHT/N, fill=colors[0]))

#Widgets
window = tk.Tk()
window.title("Simulation proie prédateurs")
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
begin = tk.Button(window, text="Commencer", command=boutton)
initialisation = tk.Button(window, text="Réinitialisation", command=reinit)



#Placement des widgets
canvas.grid(row = 1, column = 1)
begin.grid(row = 0, column = 0)
initialisation.grid(row = 0, column = 3)

#Création de la grille position_initiale
grille = []
for i in range(N) :
    grille.append([])
    for j in range(N) :
        grille[i].append(canvas.create_rectangle(i * (WIDTH/N), j * (HEIGHT/N), i * (WIDTH/N) + WIDTH/N, j * (HEIGHT/N) + HEIGHT/N, fill=colors[0]))




#Initialisation des proies et des prédateurs sur la grille
#for i in range(Npro) :
#    cases(liste, 1, N , 1, None) #Vérifie si l'emplacement de la case est disponible
#    liste[line][column] = proie 
#for i in range(Npre) :
#    cases(liste, 1, N , 1, None) #Vérifie si l'emplacement de la case est disponible               (((Erreur : cases() missing 2 required positional arguments: 'y2' and 'init')))
#    liste[line][column] = predateur                                                                (((Ce bloc est censé initialiser en utilisant la fonction cases() )))


window.mainloop()
