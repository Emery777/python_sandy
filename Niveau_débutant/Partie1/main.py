#Task 1 Lancez votre premier programme Python
print("J'apprends Python !")
x = 17 + 35 * 2
print(x)

#task 2 Enregistrez vos données avec des variables
nom = "GBAGUIDI"
age = 18
print("Je m'appelle ", nom, " et j'ai", age, "ans maintenant.")

#task 3 Classez des données avec les types de données
taille = 1.66
est_etudiant = True
print(f"nom: {nom}")
print(f"age: {age}")
print(f"taille: {taille}")
print(f"est_etudiant: {est_etudiant}")

print(f"nom: {type(nom)}")
print(f"age: {type(age)}")
print(f"taille: {type(taille)}")
print(f"est_etudiant: {type(est_etudiant)}")

#task4 Enregistrez des groupes de données avec les listes
fruits = ["pomme", "banane", "orange"]
fruits.append("kiwi")
fruits.remove("orange")
fruits[1] = "ananas"
print(fruits)
fruits.sort()
print(fruits)

#task 5 Enregistrez des données complexes avec des dictionnaires
fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"] = "vert"
del fruits["banane"]
print(fruits.keys())

