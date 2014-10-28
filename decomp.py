##Cette fonction "decomp" a pour but de décomposer une fonction
##pour afficher chacun des termes dans une liste.
##Elle a pour objectif de modifier un input "trivial" en une donnée
##exploitable pour toutes les programmes créés par la suite,
##notamment en supprimant les espaces en trop.

def decomp(f) :

    liste_termes = []
    liste_op = []
    nombre = 0

    ##Lecture des caractères un à un
    for i in range(len(f)) :
        
        ##Nombres
        try :
            int(f[i]) < 10
            nombre = nombre * 10
            nombre = nombre + int(f[i])
            
            ##Ajout automatique des "*"
            try :
                if f[i+1] == "x" :
                    liste_op.append("*")
                int(f[i+1]) < 10

            except IndexError :
                break

        except ValueError :

            if not nombre == 0 :
                liste_termes.append(nombre)
                nombre = 0
            
            ##Caractères
 
            ##Variable x
            if f[i] == "x" :
                liste_termes.append("x")

            ##Opérateurs
            elif f[i] == "+" or f[i] == "-" or f[i] == "*" :
                liste_op.append(f[i])

    if not nombre == 0:
        liste_termes.append(nombre)

    print("Liste des termes de l'équation :", liste_termes)
    print("Liste des opérateurs de l'équation :", liste_op)

    
