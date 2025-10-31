#Partie 2
#task 1
n1 = input("nombre1 : ")
n2 = input("nombre2 : ")

if n1.isnumeric() == False or n2.isnumeric() == False:
    raise SystemExit("Fin du programme")
else:
    x = int(n1)
    y = int(n2)

operation = input("le signe : ")
match operation : 
    case '+':
        print(x + y)
    case '-':
        print(x - y)
    case '*':
        print(x * y)
    case '/':
        if  y == 0 : 
            raise SystemExit("Fin du programme")
        print(x / y)
    case _:
        raise SystemExit("Fin du programme")

#task 2
nombres = input("Entrer plusieur nombre: ")
list = nombres.split(",")
list_entiers = []
for i in list :
    nombre = int(i)
    list_entiers.append(nombre)
somme = 0
for u in list_entiers :
    somme += u

x = len(list_entiers)
y = somme / x
a = 0
for v in list_entiers :
    if v > y :
        a += 1
print(a)

#task3 Regroupez des tâches en utilisant des fonctions
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

Sannuel = int(input("Écrivez votre salaire annuel: "))
htravailles = int(input("Écrivez le nombre d'heures travaillées par semaine: "))
Smensuel = salaire_mensuel(Sannuel)
Shebdomadaire = salaire_hebdomadaire(Smensuel)
Shoraire = salaire_horaire(Shebdomadaire, htravailles)
print(f"Votre salaire horaire est de {Shoraire} euros")

