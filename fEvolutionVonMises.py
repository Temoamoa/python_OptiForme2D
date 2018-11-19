#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:47:15 2017

@author: temoana
"""
import sys
import subprocess
import re
#mafonction(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])

from fSyntaxeCorrecte import SyntaxeCorrecte
from fTraitement import readSubstitution, minmaxListe
import matplotlib.pyplot as plt

def construire_graphique(lx,ly,xmin,xmax,ymin,ymax,motif):
    """ À partir de la liste des x, des y, des xmin, xmax, ymin, ymax et du motif choisi, construit le graphique associé (mais ne l'affiche pas). """
    plt.plot(lx, ly,motif,linewidth=1)#,marker='+')
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.ylabel('Contrainte de Von Mises')
    plt.xlabel('Indice du point substitué')
    plt.title('Evolution de la Contrainte de Von Mises')

def EvolutionVonMises (geo,txt,dgibi) :
    CVM = [] #Contrainte de Von Mises
    if SyntaxeCorrecte (geo) :
        unv = geo.replace('.geo','.unv')
        csv = dgibi.replace('.dgibi','.csv')
        dSub,lenDSub = readSubstitution (txt)
        subprocess.run(['touch','pointEvolutif.geo'])
        for j in range(lenDSub):
            fic = open (geo,'r')
            f = open ('pointEvolutif.geo','w')
            for ligne in fic:
                r = re.search( '.*\([0-9]*\) = {(<#X>),(<#Y>).*};' , ligne )
                rx = re.search( '.*\([0-9]*\) = {(<#X>).*};' , ligne )
                ry = re.search( '.*\([0-9]*\) = {.*(<#Y>).*};' , ligne )
                if r :
                    for cleS, valS in dSub.items() :
                        if cleS == 'X' :
                            xvar = valS[j]
                        else :
                            yvar = valS[j]
                    f.write(ligne.replace('<#X>,<#Y>',str(xvar) + ',' + str(yvar)))
                    
                elif rx and r == False :
                    for cleS, valS in dSub.items() :
                        if cleS == 'X' :
                            xvar = valS[j]
                    f.write(ligne.replace('<#X>',str(xvar)))
                
                elif ry and r == False :
                    for cleS, valS in dSub.items() :
                        if cleS == 'Y' :
                            yvar = valS[j]
                    f.write(ligne.replace('<#Y>',str(yvar)))
                    
                else :
                    f.write(ligne)
                    
            f.close()
            fic.close()
            subprocess.run(['gmsh','pointEvolutif.geo','-2','-clmin','0.05','-clmax','0.05','-format','unv','-o',unv])
            subprocess.run(['/usr/local/castem17/bin/castem17',dgibi])
            
            fic = open(csv,'r')
            for ligne in fic :
                r = re.search('([0-9].*)', ligne)
                if r :
                    CVM.append(float(r.group(1)))
                    #Creer la liste des Contrainte de Von Mises
        MinVonMises, MaxVonMises = minmaxListe(CVM) #CVM min et max
        print('Evolution de la CVM pour chaque point substtué = ',CVM)
        print()
        print('Max CVM = ',MaxVonMises)
        print('Min CVM = ',MinVonMises)
        for j in range(lenDSub):
            if CVM[j] == MinVonMises :
                print()
                print('IndiceMin = ',j)
                print('Les coordonnées du point dont la CVM est minimale sont : ')
                for cleS, valS in dSub.items() :
                    print(valS[j], end = ' ')
                print()
            if CVM[j] == MaxVonMises :
                print()
                print('IndiceMax = ',j)
                print('Les coordonnées du point dont la CVM est maximale sont : ')
                for cleS, valS in dSub.items() :
                    print(valS[j], end = ' ')
                print()
        
        print()
        print('Attention les coordonnées des points ne sont pas forcément dans l\'ordre x puis y')
        construire_graphique(range(lenDSub),CVM,0,len(CVM)-1,MinVonMises,MaxVonMises,'r-')
        plt.show()
        
#==============================================================================
# geo = 'trueone.geo'
# txt = 'substitution.txt'
# dgibi = 'trueone.dgibi'
# EvolutionVonMises (geo,txt, dgibi)
#==============================================================================

# geo = sys.argv[1]
# txt = sys.argv[2]
# dgibi = sys.argv[3]   
EvolutionVonMises(sys.argv[1],sys.argv[2], sys.argv[3])



            
    
    





    
    
    
    
        


