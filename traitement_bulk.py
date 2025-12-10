"""
Created on Mon Dec 12:2025

@author: Matthias URSET
"""
#Import des modules 
import os
from utils import files_utils as fu
from utils import list_utils as lu
from utils import tekfiles_utils as tu
from utils import graph_utils as gu
from utils import math_utils as mu
import matplotlib.pyplot as plt

Path=os.getcwd()

#ouverture des fichiers
fu.sort_ext("bulk_mesures")
Bulk_Path = os.path.join("bulk_mesures","csv")
Fichiers = fu.parcour(Bulk_Path)

L_o=[]
for i in range(len(Fichiers)):
    F=Fichiers[i]
    Meas_Path = os.path.join(Bulk_Path,F)
    Li = fu.open_csv(Meas_Path)
    L_o.append(Li)

#On tronque les lignes de texte
L=[]
for i in range(len(L_o)):
    Li= lu.enlever_n_premiers_points(L_o[i],13)
    L.append(Li)

#On crée la matrice des vecteurs abscises
MX=[]
for i in range(len(L)):
    MXi = tu.absi(L[i])
    MX.append(MXi)

#Mise à l'échelle des abscises
for i in range(len(L)):
    MX[i] = lu.scale(MX[i],1e6)

#On crée la matrice des vecteurs ordonnées 
MY=[]
for i in range(len(L)):
    MYi = tu.ordi(L[i])
    MY.append(MYi)

#Liste des titres des abscises
X_Axes=[]
for i in range(len(MX)):
    X_Axes.append("Temps en ms")

#Liste des titres des ordonnées
Y_Axes=[]
for i in range(len(MY)):
    Y_Axes.append("Valeur mesurées en USI")

#Lise des titres des figures 
Fig_name=[]
for i in range(len(Fichiers)):
    F = fu.del_ext(Fichiers[i])
    Fig_name.append(F)

#Répertoire où sont enregistrés les résultats
Repo = "Bulk graphs"

#Matrice des couples [Absi, Ordo] à tracer
M=[]
for i in range(len(MX)):
    M.append([MX[i],MY[i]])

gu.multigraph(M,Path,Repo,Fig_name,Y_Axes,X_Axes)
fu.sort_ext(Repo)

print("programme exécuté")