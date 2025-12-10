# # Vérifions le type de ce que l'utilisateur a entré
texte = input("Entrez quelque chose : ")   # Demande une valeur à l'utilisateur

if texte == "":                            # Si l'utilisateur appuie juste sur entrée (vide)
    print("Vous n'avez rien entré")

elif texte.isdigit():                      # .isdigit() → Vérifie si le texte contient uniquement des chiffres
    print("C'est un entier naturel")

else:
    try:                                   # On essaie de convertir en réel
        float(texte)                       # Si ça marche → c'est un nombre réel
        print("C'est un nombre réel")
    except:                                # Si la conversion en réel échoue → ce n'est pas un nombre
        if texte == "True" or texte == "False":   # On vérifie si c'est un booléen (True ou False)
            print("C'est un booléen")
    else:
        print("C'est une chaîne de caractères")  # Sinon c'est du texte normal
        
print('.........')
# #verification de l'âge
age = input("entrer votre âge:") 
age_int= int(age)
if age_int <0:
    print("l'âge ne peut pas être negative")
elif age_int < 18:
    print("l'âge entrer est minneur")
else :
    print("l'âge entrer est majeur")

print('............')

#Les tableaux en python sont des listes
couleurs = ["rouge", "vert", "bleu", "jaune", "noir", "blanc", "orange"]
print(couleurs[0])  # Affiche "rouge"
print(couleurs[3])  # Affiche "jaune"   
print(couleurs[6]) # Affiche "orange"
print(couleurs[2]) # Affiche "bleu"
print(couleurs[-1]) # Affiche "orange" (dernier élément)
print(couleurs[-2]) # Affiche "blanc" (avant-dernier élément)
print(couleurs[-3]) # Affiche "noir" (troisième élément en partant de la fin)
print(couleurs[0:6]) # Affiche ['rouge','vert', 'bleu', 'jaune','noir','blanc,'orange'] 

print('........')
#effectuer une iteration pour les afficher un  par un 
for couleur in couleurs:
    print(couleurs.index(couleur), couleur) #affiche la postion  et la couleur de la liste

for i in "salut ":
    print(i)


for i in range(1,12,2): #range() permet de creer une sequence de notre entier comme ceci et aussi range(n)=n-1
    print(i)
print('...........')

for i in range(1,11):
    for j in range(11):
        print(i*j) # le produit sera :0*10,1*10,2*10 .......
print('.............')

lst=[1,10,12,123,1]
e=["100",'bonjour', True,True]
print(type(lst[-1]),lst[-1])
print(type(e[-2]),e[-2])
print('..........')
print(len(e))
print(len(lst)) #len: permet de determiner le nombre d'element dans le tableau
print('............')
print(16 in lst) #ici in permet de te dire si une valeur existe dans ta liste avec les true et false
print('........')

print(e.index("100")) # .index permet de te donner la position de l'element
print('..........')
print(e.count(1))
print (lst.count(True))

print('.....')
lst.append(101) #lst.append permet d'ajouter un element à la liste
print(lst)
print('....')

e.extend(['mali','france','portugal']) #e.extend permet d'ajouter plusieurs element à la liste 
print(e)
print('....')

e.pop(5) #e.pop permet de supprimer les elements ou l'element de la liste donc sa sera la france aui sera supprimer de la liste
print(e) # avec .pop la personne doit entrer la position de l'element aui doit etre supprimer
print('.....')
e.remove('portugal')#ici la portugal sera supprimer et c'est sa la difference entre .pop ou .del tu entres l'element qui doit etre supprimer
print(e)


print('......')


lst.reverse() #permet d'inverser une liste
print (lst)
print('....')
lst.sort() #lst.sort() permet de trier les elements du tableau dans l'ordre croissant
print(lst)


print('....')


mot = input("entrer :")

if mot.isdigit(): #.isdigit permet de verifier si le nombre entrer est un entier
    
    print("c'est un nombre")
else :
    print("c'est pas un nombre")
    
print('....')
mali = 'bamakO Kidal tombouctou'
print(mali.upper()) # .upper permet d'ecrire ton texte en majuscule
print(mali.lower()) #.lower en minuscule
print(mali.split()) #.split  permet de separer les chaines pardefaut , les espaces


print('........')

from datetime import datetime
maintenant = datetime.now()
print(maintenant)
print(maintenant.day) #affiche le jour du mois
print(maintenant.hour) #affiche l'heure
print(maintenant.month) #affiche le mois
