# python_OptiForme2D

Le programme fEvolutionVonMises.py vous permettra de trouver la forme qui subit le moins de contrainte, selon le critère de Von Mises, en testant plusieurs configuration géométriques possibles, qui subissent la mêm force et son bloquer de la même manière. 

Pour lancer le programme principal fEvolutionVonMises.py, il vous faut avoir installer Cast3m, gmsh, une version de Python supérieure ou égale à la 3.0. Ces logiciels sont gratuit.

fTraitement.py contient les fonctions nécessaires au bon fonctionnement des deux autres .py
fSyntaxeCorrecte.py permet de vérifier si le fichier .geo est bien écrit
substitution.txt contient les coordonnées d'une centaine de points (2D)
trueone.geo est le fichier qui permet à gmsh de générer la forme géométrique, les symboles <#X>,<#Y> représentent les coordonnées des points du fichier substitution.txt
trueone.dgibi est le fichier qui permet à Cast3m d'appliquer une force (de 1000N selon la direction -Y à une partie de la géométrie), bloquer des déplacements et rotations (une partie de la géométrie) , et de faire sortir la valeur maximale de la contrainte de Von Mises.

fEvolutionVonMises.py tracera un graphique des contraintes Maximales de Von Mises (CMVM) pour toutes les géométries testées, il vous donnera également quel configuration est celle qui vous assure une CMVM minimal parmi le toute (Visible sur le graphique).

Lancer moi dans le terminal  : 
1) Placez vous là où sont les fichiers .py avec la commande cd
2) Mettez les fichiers .geo .txt et .dgibi avec les .py
3) Changer les droits d'éxécutions du fichier fEvolutioVonMises.py  : chmod 755 fEvolutioVonMises.py
4) Lancer le programme avec Python3.0 :
./fEvolutioVonMises.py  'fgeo.geo' 'fsubstitution.txt' 'fdgibi.dgibi'
