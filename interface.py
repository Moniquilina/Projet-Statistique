import tkinter as tk 
import random
import Outils
import projet_info

fenetre = tk.Tk()
fenetre.title("projet stat")
#je creer le canvas
canevas = tk.Canvas(fenetre, width=800, height=800, bg='white')
canevas.grid(row=0, column=0, columnspan=3, pady=0)
couleurs = ['red', 'blue', 'green', 'yellow', 'purple', 'orange'] #liste des couleurs dispo
couleur_actuelle = 'red'
def tracer_ligne():
    #juste pour tester 
    canevas.create_line(10, 10, 200, 800, fill=couleur_actuelle, width=3)

def changer_couleur():#definir la fonction pour le changement de couleur 
    global couleur_actuelle
    couleur_actuelle = random.choice(couleurs)
#creer les boutons 

bouton_tracer = tk.Button(fenetre, text="tracer la droite", command=tracer_ligne)
bouton_tracer.grid(row=1, column=0)

bouton_couleur = tk.Button(fenetre, text="Autre couleur", command=changer_couleur)
bouton_couleur.grid(row=1, column=1)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.grid(row=1, column=2)

fenetre.mainloop()