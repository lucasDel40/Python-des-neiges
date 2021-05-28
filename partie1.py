# -*- coding: utf-8 -*-
"""
PYHTON DES NEIGES
Created on Mon Mar 15 13:39:11 2021
@author: deliranl
"""

import turtle
from CONFIGS import *
import math


turtle.tracer(0,0)
turtle.hideturtle()


# =============================================================================
#  fonction lisant le fichier voulu pour le traduire en matrice
# =============================================================================

def lire_matrice(fichier):
       
    """
    aide fonction lire_matrice:
         Fichier = document string
         
         cette fonction permet de traduire un fichier en matrice.
         Pour cela on lui donne comme argument fichier qui sera le nom du fichier
         Uque l'on veut décoder.
         Ensuite elle va le lire par ligne et fera des listes de listes pour 
         obternir une matrice exploitable

    """
    with open (fichier, "r") as pc:
        temp=pc.readlines()
    L=[]
    for i in temp:
        inter=i.split()
        L_inter=[]
        for j in inter:
            L_inter.append(int(j))
        L.append(L_inter)
    return(L)
    
    
    
# =============================================================================
#  on définit la variable matrice comme étant le resultat de la fonction 
#  lire_matrice(fichier_plan)
# =============================================================================
matrice=lire_matrice(fichier_plan) 



# =============================================================================
#  fonction calculant la taille d'un carré pour que cela rentre dans la fenêtre
#  il calcule la hauteur minimale nécessaire en hauteur et en largeur puis
# arrondi au supérieur et décide de prendre la plus petite des deux
# =============================================================================
def calculer_pas(matrice):
    
    """
    aide fonction calculer_pas:
        Matrice = Liste à deux dimensions
        
        cette fonction permet de calculer la longeur minimal d'un coté du carré
        que l'on  appel le "pas"
        Elle calcule le pas en hauteur en prennant les coordonnées du plan 
        minimal en hauteur divisé par les coordonnées maximal en hauteur puis
        fait pareil avec la largeur.
        ensuite elle prends la plus petite valeur des deux en l'arrondissant à
        l'entier inferieur
    """
    
    pas_hauteur= (abs(ZONE_PLAN_MINI[1])+abs(ZONE_PLAN_MAXI[1])) /len(matrice)
    pas_largeur= (abs(ZONE_PLAN_MINI[0])+abs(ZONE_PLAN_MAXI[0]))/len(matrice[0]) 
    pas=int(min(pas_hauteur,pas_largeur))
    return(pas) 
    
    
# =============================================================================
#  on définit la variable pas comme étant le resultat de la fonction 
#  calculer_pas(matrice)
# =============================================================================    
pas=calculer_pas(matrice) 



# =============================================================================
#    fonction permettant le calcul des coordonnées
# =============================================================================
def coordonnees(case, pas):

    """
     Aide fonction coordonnees:
         Case = int
         Pas = int

         Cette fonction permet de calculer des coordonnes X;Y en fonction de sa case 
         et du pas calculer plus haut.
        
        Pour cela, on calcule x et y et on retourne un tuple (X,Y)
    """

    x = -240 + (pas*case[1]) 
   #calcul des coordonnées de X
    y = -240 + (pas*(26-case[0])) 
   #calcul des coordonnées de y
    return(x,y)
      
 
    
# =============================================================================
#     fonction permettant de tracer un carré en mettant en argument la
#     dimension souhaité et fait ensuite un carré avec turtle
# =============================================================================    
def tracer_carre(dimension):
    
    """
    Aide fonction tracer_carre:
    Dimension = Int
    
    Cette fonction permet de tracer un carre avec sa dimension (ici le pas)
    paramètre dimension : entier,pas 
    Pour cela, on fait faire à turtle une avance de la longueur du pas calculer 
    plus haut et tourner à gauche puis de répeter l'action 4 fois pour faire un carre
    
    
    exemple : 
        dimension = 15
        la fonction fera 4 fois (pour le carré) un trait droit de la longeur "dimension"
        puis un virage à 90°
    """
    
    for i in range(4):
       turtle.forward(dimension)
       turtle.left(90)


# =============================================================================
#     fonction qui va permettre de tracer le labyrinthe et colorier la case
#     selon le numéro de la matrice en étant appelé dans la fonction afficher_plan
# =============================================================================
def tracer_case(case,couleur,pas):
    
    """
    Aide fonction tracer_case:
        Case = Int
        Couleur = String
        Pas = Int 
        Cette fonction permet de tracer une case avec ses numéros de case, sa couleur
        et le pas calculer plus haut.
        
        Pour cela, on défini X et Y comme coordonnées
        ensuite, on leve le stylo turtle
        puis on va au coordonées X,Y et on baisse le stylo
        puis l'on définit la couleur de remplissage et on commence le remplissage
        puis on appelle la fonction trace_carre() pour faire la case
        puis l'on fini le remplissage
        
    exemple :
        on prends la case 1,1
        dimension = 15
        alors le turtule ira au coordonnées 1,1 calculé grâce à la fonction
        coordonnées puis mets la couleur de remplissage et fait un carré
   """
   
    x,y=coordonnees((case[0],case[1]),pas)
    dimension=pas
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(couleur) #Change la couleur de remplissage à jaune
    turtle.begin_fill()  #entamme le remplissage
    tracer_carre(dimension)
    turtle.end_fill()  #arrête le remplissage
    
    

# =============================================================================
#  fonction qui va permettre de tracer le labyrinthe complétement
# =============================================================================
def afficher_plan(matrice):
    """
    Aide fonction afficher plan:
        Matrice = Liste à deux dimensions
        Cette fonction permet d'afficher le labyrinthe au complet
        pour cela elle fait deux boucles for imbriqués,
        une qui prends la longueur de la matrice et l'autre
        la largeur de la matrice.
        
        Ensuite, on fait des test pour savoir quel est le numéro 
        dans la matrice associé à la case ou l'on se trouve et
        rempli la case avec la couleur correspondante au numéro.
    """
    
    for j in range(len(matrice)):
        for i in range(len(matrice[0])):
            if matrice[j][i]==0: #définit la variable couleur avec couleur case si le numéro dans la matrice est 0
                couleur= COULEUR_CASES
            elif matrice[j][i]==1: #définit la variable couleur avec couleur mur si le numéro dans la matrice est 1
                couleur = COULEUR_MUR
            elif matrice[j][i]==2: #définit la variable couleur avec couleur objectif si le numéro dans la matrice est 2
                couleur = COULEUR_OBJECTIF
            elif matrice[j][i]==3: #définit la variable couleur avec couleur porte si le numéro dans la matrice est 3
                couleur = COULEUR_PORTE
            elif matrice[j][i]==4: #définit la variable couleur avec couleur objet si le numéro dans la matrice est 4
                couleur = COULEUR_OBJET
            tracer_case((j,i),couleur,pas) 
    turtle.update()


# =============================================================================
# appel de la fonction d'affichage du plan qui permet d'appeler toutes
# les fonctions définis avant
# =============================================================================


afficher_plan(matrice)
turtle.mainloop()
      
    
