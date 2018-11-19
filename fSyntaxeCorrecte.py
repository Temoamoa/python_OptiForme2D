#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:29:13 2017

@author: mi4
"""

from fTraitement import readGEO, DecomposeCle, IndiceFonction
print()

#a=b=1

#dic = readGEO ('test.geo') 
def SyntaxeCorrecte(fgeo):
#if a==b :
    dic = readGEO (fgeo)
    Syntaxe = True
    i = 0
    l,k = DecomposeCle (dic)

    #Liste des indices des fonctions
    IndicePoint = IndiceFonction (dic,'Point')
    IndiceCircle = IndiceFonction (dic,'Circle')
    IndiceLine = IndiceFonction (dic,'Line')
    IndiceLineLoop = IndiceFonction (dic,'Line Loop')
    IndiceBSpline = IndiceFonction (dic,'BSpline')
    IndicePlaneSurface = IndiceFonction (dic,'Plane Surface')
    IndiceCircleLine = IndiceCircle + IndiceLine
    ICircleLineBSpline = IndiceCircleLine + IndiceBSpline

    for cle,val in dic.items() :

        #Point : 4 arguments (3 coordonnées+densité de maillage)   
        if (l[i] == 'Point') and (len(val) != 4) :
            print ('Erreur de type : nbr d\'argument')
            print ('Votre fonction Point a besoin de 4 arguments,', end =' ')
            print ('mais il en a ' + str(len(val)))
            print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
            print ('Il doit comporter 3 coordonnées et la densité de maillage')
            print ()
            Syntaxe = False
        
        
        #Circle : 3 arguments (indices de Point)       
        elif (l[i] == 'Circle') :
            if (len(val) != 3) :
                print ('Erreur de type : nbr d\'argument')
                print ('Votre fonction Circle a besoin de 3 arguments,', end =' ')
                print ('mais il en a ' + str(len(val)))
                print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
                print ()
                Syntaxe = False
        
            else : 
                b = []
                for arg in range(3) :
                    for n in range(len(IndicePoint)): 
                        if val[arg] == IndicePoint[n] :
                            b.append(1)                
                if len(b) != 3 :
                    print ('Erreur de type : argument mauvais')
                    print ('Circle doit avoir pour argument des indices de Points qui existent')
                    print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))  
                    print ('Un des indices n\'est pas celui d\'un point !')
                    print ('Vous avez le choix entre les indices de Points suivant', end = ' : ')
                    print (IndicePoint)
                    print ()
                    Syntaxe = False
            
        #Line : 2 arguments (indices de Point)
        elif (l[i] == 'Line') :
            if (len(val) != 2) :
                print ('Erreur de type : nbr d\'argument')
                print ('Votre fonction Line a besoin de 2 arguments,', end =' ')
                print ('mais il en a ' + str(len(val)))
                print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
                print ()
                Syntaxe = False
        
            else :
                b = []
                for arg in range(2) :
                    for n in range(len(IndicePoint)): 
                        if val[arg] == IndicePoint[n] :
                            b.append(1)                
                if len(b) != 2 :
                    print ('Erreur de type : argument mauvais')
                    print ('Line doit avoir pour argument des indices de Points qui existent')
                    print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))  
                    print ('Un des indices n\'est pas celui d\'un point !')
                    print ('Vous avez le choix entre les indices de Points suivant', end = ' : ')
                    print (IndicePoint)
                    print ()
                    Syntaxe = False
            
        #BSpline : 3 arguments (indices de Point)
        elif (l[i] == 'BSpline') :
            if (len(val) != 3) :
                print ('Erreur de type : nbr d\'argument')
                print ('Votre fonction BSpline a besoin de 3 arguments,', end =' ')
                print ('mais il en a ' + str(len(val)))
                print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
                print ()
                Syntaxe = False
        
            else :
                b = []
                for arg in range(3) :
                    for n in range(len(IndicePoint)): 
                        if val[arg] == IndicePoint[n] :
                            b.append(1)                
                if len(b) != 3 :
                    print ('Erreur de type : argument mauvais')
                    print ('BSpline doit avoir pour argument des indices de Points qui existent')
                    print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))  
                    print ('Un des indices n\'est pas celui d\'un point !')
                    print ('Vous avez le choix entre les indices de Points suivant', end = ' : ')
                    print (IndicePoint)
                    print ()
                    Syntaxe = False

    
    #Line Loop : au moins 2 arg (indices de Circle et Line, ...)
        elif (l[i] == 'Line Loop') :
            if (len(val) < 2) :
                print ('Erreur de type : nbr d\'argument')
                print ('Votre fonction Line Loop a besoin d\'au moins 2 arguments,', end =' ')
                print ('mais il n\'en a que' + str(len(val)))
                print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
                print ()
                Syntaxe = False
        
            else :
                b = []
                arg = 0
                while arg < len(val) :
                    for n in range(len(ICircleLineBSpline)): 
                        if (val[arg] == ICircleLineBSpline[n]) or (val[arg] == '-'+ICircleLineBSpline[n]):
                            b.append(1)
                    arg += 1
                if len(b) != len(val) :
                    print ('Erreur de type : argument mauvais')
                    print ('Line Loop doit avoir pour argument des indices de type lignes cad Circle, Line et BSpline qui existent')
                    print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))  
                    print ('Un des indices n\'est pas celui d\'un cercle ou d\'une ligne ... !')
                    print ('Vous avez le choix entre les indices de Circle suivant', end = ' : ')
                    print (IndiceCircle)
                    print ('Vous avez le choix entre les indices de Line suivant', end = ' : ')
                    print (IndiceLine)
                    print ('Vous avez le choix entre les indices de BSpline suivant', end = ' : ')
                    print (IndiceBSpline)
                    print ()
                    Syntaxe = False
    
    
        #Plane Surface : au moins 1 arg (indices de Line Loop)
        elif (l[i] == 'Plane Surface') :
            if (len(val) == 0) :
                print ('Erreur de type : nbr d\'argument')
                print ('Votre fonction Plane Surface a besoin d\'au moins 1 argument,', end =' ')
                print ('mais il n\'en a pas, taille = ' + str(len(val)))
                print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
                print ()
                Syntaxe = False
            
            else :
                b = []
                arg = 0
                while arg < len(val) :
                    for n in range(len(IndiceLineLoop)): 
                        if val[arg] == IndiceLineLoop[n] :
                            b.append(1)
                    arg += 1
                if len(b) != len(val) :
                    print ('Erreur de type : argument mauvais')
                    print ('Plane Surface doit avoir pour argument des indices de Line Loop qui existent')
                    print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))  
                    print ('Un des indices n\'est pas celui d\'un Ligne Loop !')
                    print ('Vous avez le choix entre les indices de Line Loop suivant', end = ' : ')
                    print (IndiceLineLoop)
                    print ()
                    Syntaxe = False
            
        #Physical Line : au moins 1 arg (indices de Circle, Line, ...)
        elif (l[i] == 'Physical Line') :
            if (len(val) == 0) :
                print ('Erreur de type : nbr d\'argument')
                print ('Votre fonction Physical Line a besoin d\'au moins 1 argument,', end =' ')
                print ('mais il n\'en a pas, taille = ' + str(len(val)))
                print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
                print ()
                Syntaxe = False
            
            else :
                b = []
                arg = 0
                while arg < len(val) :
                    for n in range(len(ICircleLineBSpline)): 
                        if val[arg] == ICircleLineBSpline[n] :
                            b.append(1)
                    arg += 1
                if len(b) != len(val) :
                    print ('Erreur de type : argument mauvais')
                    print ('Physical Line doit avoir pour argument des indices de Circle, Line et BSpline qui existent')
                    print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))  
                    print ('Un des indices n\'est pas celui d\'un cercle, d\'une ligne ou d\'un BSpline !')
                    print ('Vous avez le choix entre les indices de Circle suivant', end = ' : ')
                    print (IndiceCircle)
                    print ('Vous avez le choix entre les indices de Line suivant', end = ' : ')
                    print (IndiceLine)
                    print ('Vous avez le choix entre les indices de BSpline suivant', end = ' : ')
                    print (IndiceBSpline)
                    print ()
                    Syntaxe = False
                
                
        #Physical Surface : au moins 1 arg (indices de Plane Surface)
        elif (l[i] == 'Physical Surface') :
            if (len(val) == 0) :
                print ('Erreur de type : nbr d\'argument')
                print ('Votre fonction Physical Surface a besoin d\'au moins 1 argument,', end =' ')
                print ('mais il n\'en a pas, taille = ' + str(len(val)))
                print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))
                print ()
                Syntaxe = False
        
            else :
                b = []
                arg = 0
                while arg < len(val) :
                    for n in range(len(IndicePlaneSurface)): 
                        if val[arg] == IndicePlaneSurface[n] :
                            b.append(1)
                    arg += 1
                if len(b) != len(val) :
                    print ('Erreur de type : argument mauvais')
                    print ('Physical Surface doit avoir pour argument des indices de Plane Surface')
                    print ('Modifier votre .geo à cette ligne => ' + str(cle) + ' = ' + str(val))  
                    print ('Un des indices n\'est pas celui d\'un Plane Surface !')
                    print ('Vous avez le choix entre les indices de Plane Surface suivant', end = ' : ')
                    print (IndicePlaneSurface)
                    print ()
                    Syntaxe = False
        i+=1
    return Syntaxe

#fgeo = 'trueone.geo'
#print(SyntaxeCorrecte(fgeo))



            

            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 

    

    
    