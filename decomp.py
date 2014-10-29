##Cette fonction "decomp" a pour but de décomposer une fonction
##pour afficher chacun des termes dans une liste.
##Elle a pour objectif de modifier un input "trivial" en une donnée
##exploitable pour toutes les programmes créés par la suite,
##notamment en supprimant les espaces en trop.

def decomp(f) :

    liste_termes = [] ##Liste des termes utilisés (entiers et inconnue)
    liste_op = [] ##Liste des opéateurs utilisés (+, - ou *)
    nombre = 0 

    ##Lecture des caractères un à un
    for i in range(len(f)) :
        
        ##Nombres
        try :
            int(f[i]) < 10 ##Vérifie que le terme de la chaîne est un nombre
            nombre = nombre * 10 ##Si c'est le cas, on multiplie le terme précédent par 10, ainsi pour 24, 2 devient 20 auquel on ajoute 4
            nombre = nombre + int(f[i]) ##On ajoute le nouveau nombre
            
            ##Ajout automatique des "*"
            try :
                if f[i+1] == "x" : ##Si le caractère suivant est un x
                    liste_op.append("*") ##On ajoute automatiquement un "*"
                #int(f[i+1]) < 10 ##On vérifie que le caractère suivant est un nombre

            except IndexError : ##S'il y a une erreur de taille de chaîne, c'est qu'on arrive au bout du str
                break ##Donc on break

        except ValueError : ##Si le caractère n'est pas un nombre

            if not nombre == 0 :
                liste_termes.append(nombre) ##On n'a plus besoin d'agrandir le nombre, on l'ajoute à la liste
                nombre = 0 ##On remet le nombre à 0 pour prévoir le nombre suivant
            
            ##Caractères
 
            ##Variable x
            if f[i] == "x" :
                liste_termes.append("x")

            ##Opérateurs
            elif f[i] == "+" or f[i] == "-" or f[i] == "*" :
                liste_op.append(f[i])

    if not nombre == 0:
        liste_termes.append(nombre)

    #print("==DÉCOUPAGE DES TERMES DE LA FONCTION==")
    #print("Liste des termes de la fonction :", liste_termes)
    #print("Liste des opérateurs :", liste_op,"\n")

    return(liste_termes, liste_op)

def calcul(liste_termes, liste_op, x) :

    resultat = liste_termes[0]

    #print("==CALCUL DES MULTIPLICATIONS==")
    ##Priorité aux multiplications
    for i in range(len(liste_op)) :

        resultat = liste_termes[i]
        
        if liste_op[i] == "*" :
            resultat = resultat * eval(str(liste_termes[i+1]))
            liste_termes[i] = resultat
            #print("Liste des termes de la fonction :", liste_termes)
            #print("Liste des opérateurs :", liste_op,"\n")

    i = 0
    
    #print("==SUPPRESSION DES TERMES MULTIPLICATEURS==")
    ##Suppression des "*"
    while i < len(liste_op) :

        if liste_op[i] == "*" :
            liste_op.pop(i)
            liste_termes.pop(i+1)
            #print("Liste des termes de la fonction :", liste_termes)
            #print("Liste des opérateurs :", liste_op,"\n")
            i = -1

        i = i+1
                   
        #if IndexError :
            #print(i, "Error")
            #break

    #print("==CALCUL DES ADDITIONS ET SOUSTRACTIONS==")
    ##Ensuite, additions et soustractions

    resultat = liste_termes[0]
    
    for i in range(len(liste_op)) :
        if liste_op[i] == "+" :
            resultat = resultat + eval(str(liste_termes[i+1]))
        elif liste_op[i] == "-" :
            resultat = resultat - eval(str(liste_termes[i+1]))
        #print("Liste des termes de la fonction :", liste_termes)
        #print("Liste des opérateurs :", liste_op,"\n")        

    return(resultat)

def main(f, x) :

    (liste_termes, liste_op) = decomp(f)
    resultat = calcul(liste_termes, liste_op, x)
    print("Résultat de l'opération", f,"pour x =", x, ":", resultat)
    
