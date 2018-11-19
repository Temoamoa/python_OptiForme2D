#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:43:14 2017

@author: temoana
"""
import re

#Renvoie un dictionnaire de cle Fonction(indice) et valeur une liste de valeur 
def readGEO(filegeo):
    d={}
    lval = []
    fic = open (filegeo,'r')
    for ligne in fic:
        r = re.search( '(.*)\(([0-9]*)\) = ({.*});' , ligne ) 
        if r : 
            fonction = r.group(1)
            indice = r.group (2)
            val = r.group(3)
            val = val.strip('{}')
            lval = val.split(',')
            d[fonction+'('+indice+')'] = lval
    fic.close()
    return d

#d = readGEO('trueone.geo')
#for cle,val in d.items():
#    print (cle + ' = ' + str(val)) 
#print ()

# Renvoie un dictionnaire qui a X et Y en clé et les coordonnees a changé en valeur
#filetxt = 'substitution.txt'
def readSubstitution (filetxt):
    dico={}
    fic = open (filetxt,'r')
    for ligne in fic:
        r = re.search( '<#(.)>:(.*)' , ligne ) 
        if r : 
            cle = r.group(1)
            val = r.group(2)
            l = val.split(';')
        dico[cle]=l
    fic.close()
    return dico, len(l)

#dico, l = readSubstitution('substitution.txt')
#for cle,val in dico.items():
    #print (str(cle) + " = " + str(val))

#Renvoie deux listes la premiere est la str(Fonction) et l'autre son int(indice) associé
#Peut etre construit dans read
def DecomposeCle(dic):
    l = []
    k = []
    for cle in dic:
        r = re.search('(.*)\(([0-9]*)\)', cle)
        if r :
            l.append(str(r.group(1)))
            k.append(str(r.group(2)))
    return l,k

#fonction,indice = DecomposeCle(d) 
#for i in range(len(fonction)) :
#   print (fonction[i] + " a pour indice " + indice[i])

    
#Renvoie les indices de la Fonction du dictionnaire 
def IndiceFonction (dic,fonction) :
    l,k = DecomposeCle (dic)
    ListeIndice = []
    for n in range(len(dic)) :
        if l[n] == fonction :
            ListeIndice.append(k[n])
    return ListeIndice

#a = IndiceFonction(d,'Point')
#print  (a)

def minmaxListe (l) :
    minl = l[0]
    maxl = l[0]
    for i in range(1,len(l)) :
        if minl > l[i] :
            minl = l[i]
        elif maxl < l[i] :
            maxl = l[i]            
    return minl, maxl

#l = [ 145, 7, 52, 5, 221, 8]
#print(minListe(l))

            
        


#Renvoie True si un élément appartient a une liste ou False sinon
#def appartient (liste, element) :
#   a = False
#    for i in range(len(liste)) :
#       if liste[i] == element:
#           a = True
#   return a 




