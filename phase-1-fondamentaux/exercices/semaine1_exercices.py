# IMPORTANT: Lisez les commentaires et complétez les exercices!
# Chaque exercice a une réponse attendue marquée par # RÉSULTAT ATTENDU


# =========================================================
# EXERCICE 1: Créer des variables et les afficher
# =========================================================
# TODO: Créez une variable 'prenom' avec votre prénom
# TODO: Créez une variable 'ville' avec votre ville
# TODO: Afficher le résultat avec print()

prenom = ""  # À compléter
ville = ""   # À compléter

print("Exercice 1:")
print("Mon prénom est", prenom)
print("Je vis à", ville)

# RÉSULTAT ATTENDU:
# Mon prénom est [votre prénom]
# Je vis à [votre ville]

print("\n" + "="*50 + "\n")  # Séparation


# =========================================================
# EXERCICE 2: Travailler avec différents types
# =========================================================
# TODO: Complétez les variables avec les bonnes valeurs

nom_complet = "Alice Martin"        # str (texte)
annee_naissance = 1998              # int (nombre entier)
hauteur_cm = 165.5                  # float (nombre décimal)
est_etudiant = True                 # bool (vrai/faux)

print("Exercice 2: Types de données")
print("Nom:", nom_complet)
print("Année de naissance:", annee_naissance)
print("Hauteur (cm):", hauteur_cm)
print("Est étudiant?", est_etudiant)

print("\n" + "="*50 + "\n")


# =========================================================
# EXERCICE 3: Utiliser type() pour vérifier les types
# =========================================================

print("Exercice 3: Vérifier les types")
print("Type de nom_complet:", type(nom_complet))
print("Type de annee_naissance:", type(annee_naissance))
print("Type de hauteur_cm:", type(hauteur_cm))
print("Type de est_etudiant:", type(est_etudiant))

# RÉSULTAT ATTENDU:
# Type de nom_complet: <class 'str'>
# Type de annee_naissance: <class 'int'>
# Type de hauteur_cm: <class 'float'>
# Type de est_etudiant: <class 'bool'>

print("\n" + "="*50 + "\n")


# =========================================================
# EXERCICE 4: Modifier des variables
# =========================================================

print("Exercice 4: Modifier des variables")

age = 20
print("Age initial:", age)

# TODO: Ajoutez 1 à l'age
age = age + 1
print("Après avoir eu un an:", age)

# TODO: Multipliez l'age par 2
age = age * 2
print("Age multiplié par 2:", age)

print("\n" + "="*50 + "\n")


# =========================================================
# EXERCICE 5: Les listes
# =========================================================

print("Exercice 5: Listes")

# TODO: Créez une liste avec 5 fruits de votre choix
fruits = ["pomme", "banane", "orange", "raisin", "fraise"]
print("Fruits:", fruits)
print("Type:", type(fruits))

# TODO: Créez une liste avec les nombres 1 à 5
nombres = [1, 2, 3, 4, 5]
print("Nombres:", nombres)

print("\n" + "="*50 + "\n")


# =========================================================
# EXERCICE 6: Les dictionnaires (bonus)
# =========================================================

print("Exercice 6: Dictionnaires")

# TODO: Créez un dictionnaire avec vos informations personnelles
infos_personnelles = {
    "nom": "Martin",
    "prenom": "Alice",
    "age": 25,
    "ville": "Paris"
}

print("Mes informations:", infos_personnelles)
print("Type:", type(infos_personnelles))

print("\n" + "="*50 + "\n")


# =========================================================
# DÉFI BONUS 🏆
# =========================================================

print("DÉFI BONUS: Créer une 'biographie' complète")
print()

# TODO: Créez des variables pour décrire quelqu'un
# et afficher une phrase complète

nom = "Jean"
prenom = "Pierre"
age = 30
couleur_yeux = "bleu"
ville = "Lyon"
profession = "Développeur"

print(f"Je m'appelle {prenom} {nom}.")
print(f"J'ai {age} ans et j'habite à {ville}.")
print(f"Ma couleur d'yeux est {couleur_yeux}.")
print(f"Je suis {profession}.")

print("\n" + "="*50 + "\n")

print("✅ Bravo! Vous avez complété tous les exercices de la Semaine 1!")
print("📝 N'hésitez pas à modifier et expérimenter avec le code.")
print("↩️  Préparez-vous pour la Semaine 2!")