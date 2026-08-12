# IMPORTANT: Lisez les commentaires et complétez les exercices!
# Chaque exercice correspond au cours 04-fonctions.md

print("="*60)
print("SEMAINE 4: LES FONCTIONS - EXERCICES")
print("="*60)
print()

# =========================================================
# EXERCICE 1: Fonction Simple sans Paramètre
# =========================================================

print("EXERCICE 1: Fonction Simple")
print("-" * 60)

# TODO: Créez une fonction qui affiche un message
def dire_bonjour():
    """Affiche un message de bienvenue."""
    print("Bonjour!")
    print("Bienvenue en Python!")

# Appeler la fonction
dire_bonjour()
print()

print("="*60)
print()

# =========================================================
# EXERCICE 2: Fonction avec Un Paramètre
# =========================================================

print("EXERCICE 2: Fonction avec Paramètre")
print("-" * 60)

# TODO: Créez une fonction qui salue quelqu'un
def saluer(nom):
    """Salue une personne par son nom."""
    print(f"Bonjour {nom}!")

# Appeler la fonction
saluer("Alice")
saluer("Bob")
saluer("Charlie")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 3: Fonction avec Plusieurs Paramètres
# =========================================================

print("EXERCICE 3: Plusieurs Paramètres")
print("-" * 60)

# TODO: Créez une fonction qui ajoute deux nombres
def additionner(a, b):
    """Additionne deux nombres et affiche le résultat."""
    resultat = a + b
    print(f"{a} + {b} = {resultat}")

# Appeler la fonction
additionner(5, 3)
additionner(10, 20)
additionner(100, 50)

print()
print("="*60)
print()

# =========================================================
# EXERCICE 4: Fonction avec Paramètre par Défaut
# =========================================================

print("EXERCICE 4: Paramètre par Défaut")
print("-" * 60)

# TODO: Créez une fonction avec un paramètre par défaut
def saluer_avec_titre(nom, titre="Monsieur"):
    """Salue avec un titre (par défaut: Monsieur)."""
    print(f"Bonjour {titre} {nom}!")

# Appeler avec valeur par défaut
saluer_avec_titre("Dupont")

# Appeler avec valeur personnalisée
saluer_avec_titre("Dupont", "Professeur")
saluer_avec_titre("Martin", "Docteur")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 5: Fonction avec Return
# =========================================================

print("EXERCICE 5: Fonction avec Return")
print("-" * 60)

# TODO: Créez une fonction qui retourne une valeur
def additionner_return(a, b):
    """Retourne la somme de deux nombres."""
    return a + b

# Récupérer et utiliser le résultat
resultat = additionner_return(5, 3)
print(f"Résultat: {resultat}")

print(f"10 + 20 = {additionner_return(10, 20)}")
print(f"100 + 50 = {additionner_return(100, 50)}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 6: Fonction Retournant un Texte
# =========================================================

print("EXERCICE 6: Return Texte")
print("-" * 60)

# TODO: Créez une fonction qui retourne un message
def creer_message(nom):
    """Crée et retourne un message personnalisé."""
    message = f"Bonjour {nom}! Bienvenue!"
    return message

# Utiliser le résultat
resultat = creer_message("Alice")
print(resultat)

print(creer_message("Bob"))
print(creer_message("Charlie"))

print()
print("="*60)
print()

# =========================================================
# EXERCICE 7: Fonction Retournant Plusieurs Valeurs
# =========================================================

print("EXERCICE 7: Return Plusieurs Valeurs")
print("-" * 60)

# TODO: Créez une fonction qui retourne plusieurs valeurs
def obtenir_info():
    """Retourne plusieurs informations."""
    nom = "Alice"
    age = 25
    ville = "Paris"
    return nom, age, ville

# Récupérer les valeurs
nom, age, ville = obtenir_info()
print(f"Nom: {nom}")
print(f"Age: {age}")
print(f"Ville: {ville}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 8: Fonction avec Condition et Return
# =========================================================

print("EXERCICE 8: Condition et Return")
print("-" * 60)

# TODO: Créez une fonction qui vérifie l'âge
def est_majeur(age):
    """Vérifie si une personne est majeure."""
    if age >= 18:
        return True
    else:
        return False

# Utiliser la fonction
print(f"20 ans -> Majeur? {est_majeur(20)}")
print(f"15 ans -> Majeur? {est_majeur(15)}")
print(f"18 ans -> Majeur? {est_majeur(18)}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 9: Fonction avec Boucle
# =========================================================

print("EXERCICE 9: Fonction avec Boucle")
print("-" * 60)

# TODO: Créez une fonction qui utilise une boucle
def afficher_n_fois(texte, n):
    """Affiche un texte n fois."""
    for i in range(n):
        print(f"{i+1}. {texte}")

# Utiliser la fonction
afficher_n_fois("Python", 3)
print()
afficher_n_fois("Fonction", 4)

print()
print("="*60)
print()

# =========================================================
# EXERCICE 10: Fonction Somme d'une Liste
# =========================================================

print("EXERCICE 10: Somme d'une Liste")
print("-" * 60)

# TODO: Créez une fonction qui somme une liste
def somme_liste(nombres):
    """Retourne la somme de tous les nombres."""
    total = 0
    for nombre in nombres:
        total = total + nombre
    return total

# Utiliser la fonction
nombres = [10, 20, 30, 40, 50]
print(f"Liste: {nombres}")
print(f"Somme: {somme_liste(nombres)}")

nombres2 = [5, 10, 15]
print(f"Liste: {nombres2}")
print(f"Somme: {somme_liste(nombres2)}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 11: Fonction Moyenne
# =========================================================

print("EXERCICE 11: Fonction Moyenne")
print("-" * 60)

# TODO: Créez une fonction qui calcule la moyenne
def moyenne_liste(nombres):
    """Retourne la moyenne des nombres."""
    if len(nombres) == 0:
        return 0
    total = somme_liste(nombres)
    return total / len(nombres)

# Utiliser la fonction
nombres = [10, 20, 30, 40, 50]
print(f"Liste: {nombres}")
print(f"Moyenne: {moyenne_liste(nombres)}")

nombres2 = [5, 10, 15, 20]
print(f"Liste: {nombres2}")
print(f"Moyenne: {moyenne_liste(nombres2)}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 12: Fonction Vérifiant un Nombre
# =========================================================

print("EXERCICE 12: Vérifications")
print("-" * 60)

# TODO: Créez des fonctions de vérification
def est_pair(nombre):
    """Vérifie si un nombre est pair."""
    return nombre % 2 == 0

def est_positif(nombre):
    """Vérifie si un nombre est positif."""
    return nombre > 0

def est_zero(nombre):
    """Vérifie si un nombre est zéro."""
    return nombre == 0

# Utiliser les fonctions
print(f"4 est pair? {est_pair(4)}")
print(f"5 est pair? {est_pair(5)}")
print(f"10 est positif? {est_positif(10)}")
print(f"-5 est positif? {est_positif(-5)}")
print(f"0 est zéro? {est_zero(0)}")
print(f"5 est zéro? {est_zero(5)}")

print()
print("="*60)
print()

# =========================================================
# DÉFI BONUS 1: Calculatrice Complète 🏆
# =========================================================

print("DÉFI BONUS 1: Calculatrice")
print("-" * 60)

# TODO: Créez des fonctions pour une calculatrice
def calculer(a, b, operation):
    """Effectue une opération entre deux nombres."""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Erreur: Division par zéro!"
    else:
        return "Opération invalide!"

# Utiliser la fonction
print(f"10 + 5 = {calculer(10, 5, '+')}")
print(f"10 - 5 = {calculer(10, 5, '-')}")
print(f"10 * 5 = {calculer(10, 5, '*')}")
print(f"10 / 5 = {calculer(10, 5, '/')}")
print(f"10 / 0 = {calculer(10, 0, '/')}")

print()
print("="*60)
print()

# =========================================================
# DÉFI BONUS 2: Jeu Nombre Secret avec Fonction 🏆
# =========================================================

print("DÉFI BONUS 2: Nombre Secret (Avec Fonction)")
print("-" * 60)

# TODO: Créez une fonction pour le jeu
def verifier_nombre(nombre, secret):
    """Vérifie et retourne un message."""
    if nombre == secret:
        return "Trouvé!"
    elif nombre < secret:
        return "Trop petit!"
    else:
        return "Trop grand!"

# Utiliser la fonction
nombre_secret = 7

predictions = [3, 8, 7]
for i, prediction in enumerate(predictions, 1):
    resultat = verifier_nombre(prediction, nombre_secret)
    print(f"Tentative {i}: {prediction} - {resultat}")
    if resultat == "Trouvé!":
        print(f"✅ Bravo! Vous avez trouvé en {i} tentatives!")
        break

print()
print("="*60)
print()

# =========================================================
# DÉFI BONUS 3: Fonction Table de Multiplication 🏆
# =========================================================

print("DÉFI BONUS 3: Table de Multiplication")
print("-" * 60)

# TODO: Créez une fonction pour les tables
def afficher_table(nombre, jusqu_a=10):
    """Affiche la table de multiplication."""
    print(f"Table de {nombre}:")
    for i in range(1, jusqu_a + 1):
        print(f"{nombre} x {i} = {nombre * i}")

# Utiliser la fonction
afficher_table(7)
print()
afficher_table(5, 5)

print()
print("="*60)
print("✅ Bravo! Vous avez complété tous les exercices de la Semaine 4!")
print("📝 N'hésitez pas à modifier et expérimenter avec le code.")
print("↩️  Préparez-vous pour la Semaine 5!")
print("="*60)