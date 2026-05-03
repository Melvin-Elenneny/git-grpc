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




from random import choice

# lecture du fichier "dictionnaire.txt"
with open("dictionnaire.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()
    
f.closed


# mot aléatoire
mot = choice(lignes)
mot = mot.split(";")[0]
longueur = len(mot)


# mot caché
mot_cache = []

for lettre in mot:
    mot_cache.append("_")


# compteur de vies
vies = 5


# tentatives
def jeu(mot, mot_cache, vies):
    while vies > 0:
        print("\nMot :", " " .join(mot_cache))
        print("\nVies restantes :", vies)

        lettre = input("\nSaisissez une lettre : ")

        if lettre in mot:
            print("\nLettre trouvée ")
            
            position = 0
            for i in mot:
                if i == lettre:
                    mot_cache[position] = lettre
                
                position = position + 1
        
        else:
            print("\nCette lettre n'est pas dans le mot ")
            vies = vies -1
        
        if "_" not in mot_cache:
            print(f"\nBravo ! Le mot était: {mot} ")
            return
        
    if vies == 0:
        print(f"\nPerdu ! Le mot était: {mot}")

jeu(mot, mot_cache, vies)


