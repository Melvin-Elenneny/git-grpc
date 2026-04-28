''' 
Projet Jeu du pendu, classe inversé, groupe C

IMPORTANT ! MERCI DE BIEN LIRE !

Instructions de sauvegardes si, et seulement si vous avez été ajouté en tant que COLLABORATEUR :
Respectez bien les majuscules, espace, autres caractères...

Etape 1 (entrée dans nouveau terminal): Allez dans "Terminal" en haut à gauche / New Terminal / dans le terminal qui s'affichera en bas, tapez : cd Desktop

Etape 2 (cloner) : toujours dans le terminal, tapez : git clone https://github.com/Melvin-Elenneny/git-grpc.git

Etape 3 (entrée dans le dossier) : toujours dans le terminal, tapez : cd Classe_inverse_groupeC

Etape 4 (l'ouverture du dossier dans votre logiciel VSC) : code .
ATTENTION ! il y a un espace entre "code" et "."

Etape 5 (récupération des dernières modifications du programme): toujours dans le terminal, tapez : git pull

A partir de là, vous pouvez travailler normalement sur le projet. Une fois finis faites Crtl + S , sauvegardez vos modifications :
Vous pourrez voir un "M" se rajouter sur l'onglet du haut, qui donnera ensuite "classe_inverse.py M"
le "M" signifie midifified, donc que votre programme a bien été sauvegardé

Etape 6 (sauvegarder les modifications) : dans le terminal, tapez : git add .
Il y a encore un espace entre "add" et "."

Etape 7 (création d'une sauvegarde) : dans le terminal, tapez : git commit -m "description des modifications"
Dans les guillements, mettez les changements / ajouts que vous avez fait dans le programme

Etape 8 (envoyer sur GitHub) : dans le terminal, tapez : git push


Merci de prendre en compte toutes les étapes minutieusement, et ne pas modifier / effacer le texte ci-dessus sans m'en informer.

Pour tout problème, merci de me contacter en MP sur Sonate (Melvin Lannoy), ou de passer par le forum de discussion Introduction à la programmation, ou de contacter votre tuteur.

N'oubliez pas de faire un Ctrl + S à chaques modifications ! Sinon vous perdez votre travail !

Aides: dans le cours "Introduction à la programmation", cliquez sur "Aides & récap" en bas du jalon 8
Vous y trouverez aussi ce lien : https://docs.python.org/fr/3/tutorial/inputoutput.html#reading-and-writing-files
'''




from random import random

# lecture du fichier "dictionnaire.txt"
f = open("dictionnaire.txt", "r", encoding="utf-8")
with open("dictionnaire.txt", encoding="utf-8") as f:
    lines = f.read()
    #print(lines) je teste l'affichage, ne pas prendre en compte, cette ligne sera supprimée
f.closed


# mot aléatoire



