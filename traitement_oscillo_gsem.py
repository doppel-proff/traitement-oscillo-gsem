"""
Created on Mon Dec 12:2025

@author: Matthias URSET
"""

#Import des modules 
import os
import files_utils as fu
import list_utils as lu
import tekfiles_utils as tu
import graph_utils as gu
import math_utils as mu
import matplotlib.pyplot as plt

Path=os.getcwd()

#ouverture des fichiers
Ubs_o = fu.open_csv("mesures\ess 10 bear volt.csv")
Ibi_o = fu.open_csv("mesures\ess 10 bear cur in.csv")
Ibo_o = fu.open_csv("mesures\ess 10 bear cur out.csv")

#Matrice [[temps],[Courant entrée]]
Ibi = lu.enlever_n_premiers_points(Ibi_o,13)

#Matrice [[temps],[Courant entrée]]
Ibo = lu.enlever_n_premiers_points(Ibo_o,13)

#Matrice [[temps],[Courant entrée]]
Ubs = lu.enlever_n_premiers_points(Ubs_o,13)

#vecteur temps des courants en entrée
XIbi = tu.absi(Ibi)
XIbi = lu.scale(XIbi,1e6)

#vecteur des temps courants en sortie 
XIbo = tu.absi(Ibo)
XIbo = lu.scale(XIbo,1e6)

#vecteur temps des tensions 
XUbs = tu.absi(Ubs)
XUbs = lu.scale(XUbs,1e6)

#vecteur des courants en entrée
YIbi = tu.ordi(Ibi)
YIbi = lu.scale(YIbi, 1e3)

#vecteur des courants en sortie 
YIbo = tu.ordi(Ibo)
YIbo = lu.scale(YIbo, 1e3)

#vecteur des tensions
YUbs = tu.ordi(Ubs)

M=[[XIbi,YIbi],[XIbo,YIbo],[XUbs,YUbs]]

#Nom du répertoire où seront enregistrés les graphs
Repo_ind = "graphs individuels"
Repo_sup = "graphs superposés"

#Titre du graph
Fig_name = ["Test #10_Io","Test #10_Is","Test #10_Ubs"]

#Titre des axes des ordonnées
Y_Axes = ["Courant en entrée des roulements en mA","Courant en sortie des roulements en mA","Tension entre l'OR des roulements et l'arbre en V"]

#Titre axe des abscises 
X_Axes = ["Temps en us","Temps en us","Temps en us"]

gu.multigraph(M,Path,Repo_ind,Fig_name,Y_Axes,X_Axes)

M2=[[XIbi,YIbi],[XIbo,YIbo]]
gu.graphsup(M2,Path,Repo_sup,"Comparaison des courants en entrée et sortie",["Test #10_Io mA","Test #10_Is mA"],"Temps en us")

"""
print(YIbi[0])
print(YIbo[0])
print(YUbs[0])
"""