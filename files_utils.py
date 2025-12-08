"""
Created on Mon Oct 14 13:20:34 2024

@author: Matthias URSET
"""

#Import des modules 
import numpy as np
import os

#retourne sous forme de matrice les valeurs contenues dans un fichier .csv
def open_csv(File):
    Dcsv = open(str(File))# Dcsv variable pour la liste csv.
    D = np.genfromtxt(Dcsv, delimiter=",")# D Liste du document csv au format np.array
    return (D)

#sauvegarde une valeur dans un fichier texte à l'endroit souhaité
def save_value(Value, Path, Folder_name, File_name, Unit):
    File_name= File_name+".txt"
    new_folder_path = Path+'\\'+Folder_name #Emplacement du dossier où seront enregistrées les courbes
    os.makedirs(new_folder_path, exist_ok=True) # Création du dossier
    File_path=os.path.join(new_folder_path,File_name)
    with open(File_path, 'w') as file:
        file.write(str(Value)+ Unit)

#Sauvegarde un vecteur au format csv
#def save_csv_vect(L, Path, Folder_name, File_name):

#Sauvegarde un vecteur dans la colone N d'un fichier excel
#def save_xlsx_vect(L,N, Path, Folder_name, File_name):

#Sauvegarde une matrice au format csv
#def save_csv_vect(M, Path, Folder_name, File_name):

#Sauvegarde une matrice dans un fichier excel
#def save_xlsx_vect(M, Path, Folder_name, File_name):