# -*- coding: utf-8 -*-
"""
Created on 26/11/2025

@author: Matthias URSET

Useful functions to work on .csv files from a tektronix oscilloscope
"""

# This functions extracts the abscise from a .tek file which has had it's first 13 lines removed. 
def absi(M):
    L=[]
    if isinstance(M[0][0], float)==False :
        print('vérifier la première ligne')
    else :
        for i in range(len(M)) :
            L.append(M[i][0])
        return(L)

# This functions extracts the ordinate from a .tek file which has had it's first 13 lines removed. 
def ordi(M):
    L=[]
    if isinstance(M[0][0], float)==False :
        print('vérifier la première ligne')
    else :
        for i in range(len(M)) :
            L.append(M[i][1])
        return(L)