# IMPORTANT: Lisez les commentaires et complétez les exercices!
# Chaque exercice correspond au cours 03-structures-controle.md

print("="*60)
print("SEMAINE 3: STRUCTURES DE CONTRÔLE - EXERCICES")
print("="*60)
print()

# =========================================================
# EXERCICE 1: Structures if/else Simples
# =========================================================

print("EXERCICE 1: Structures if/else")
print("-" * 60)

# TODO: Vérifiez si quelqu'un est majeur
age = 20
age_minimum = 18

if age >= age_minimum:
    print(f"Vous avez {age} ans.")
    print("Vous êtes majeur! ✅")
else:
    print(f"Vous avez {age} ans.")
    print("Vous êtes mineur. ⛔")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 2: Structures if/elif/else
# =========================================================

print("EXERCICE 2: if/elif/else - Notes")
print("-" * 60)

# TODO: Évaluez une note
note = 85

if note >= 90:
    mention = "Excellent! 🌟"
elif note >= 80:
    mention = "Très bien! 👍"
elif note >= 70:
    mention = "Bien! 🙂"
elif note >= 60:
    mention = "Acceptable. 😐"
else:
    mention = "Échec. 😞"

print(f"Note: {note}/100")
print(f"Résultat: {mention}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 3: Boucle for avec range
# =========================================================

print("EXERCICE 3: Boucle for avec range()")
print("-" * 60)

# TODO: Affichage les nombres de 1 à 5
print("Les nombres de 1 à 5:")
for i in range(1, 6):
    print(i, end=" ")

print()
print()

# TODO: Affichage les nombres pairs de 0 à 10
print("Les nombres pairs de 0 à 10:")
for i in range(0, 11, 2):
    print(i, end=" ")

print()
print()

print("="*60)
print()

# =========================================================
# EXERCICE 4: Boucle for avec une liste
# =========================================================

print("EXERCICE 4: Boucle for avec une liste")
print("-" * 60)

# TODO: Parcourez une liste de fruits
fruits = ["pomme", "banane", "orange", "raisin", "fraise"]

print("Liste de fruits:")
for fruit in fruits:
    print(f"- {fruit}")

print()

# TODO: Comptez les fruits
print(f"Nombre de fruits: {len(fruits)}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 5: Boucle for avec condition
# =========================================================

print("EXERCICE 5: Boucle for avec condition")
print("-" * 60)

# TODO: Affichage les nombres pairs
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Les nombres pairs:")
for nombre in nombres:
    if nombre % 2 == 0:
        print(nombre, end=" ")

print()
print()

# TODO: Affichage les nombres > 5
print("Les nombres supérieurs à 5:")
for nombre in nombres:
    if nombre > 5:
        print(nombre, end=" ")

print()
print()

print("="*60)
print()

# =========================================================
# EXERCICE 6: Table de Multiplication
# =========================================================

print("EXERCICE 6: Table de Multiplication")
print("-" * 60)

# TODO: Affichage la table de 7
nombre = 7

print(f"Table de multiplication de {nombre}:")
for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 7: Boucle while Simple
# =========================================================

print("EXERCICE 7: Boucle while")
print("-" * 60)

# TODO: Comptez de 0 à 4 avec while
print("Compter de 0 à 4:")
i = 0
while i < 5:
    print(i, end=" ")
    i = i + 1

print()
print()

print("="*60)
print()

# =========================================================
# EXERCICE 8: Boucle while avec Condition
# =========================================================

print("EXERCICE 8: while avec Condition")
print("-" * 60)

# TODO: Trouvez le nombre secret
nombre_secret = 7
nombre_devin = 0
tentatives = 0

print("Jeu: Devinez le nombre secret (1-10)")
print()

# Simulation du jeu (au lieu de input)
predictions = [3, 8, 7]  # Les prédictions
index = 0

while nombre_devin != nombre_secret and index < len(predictions):
    nombre_devin = predictions[index]
    tentatives = tentatives + 1
    
    if nombre_devin == nombre_secret:
        print(f"✅ Bravo! Vous avez trouvé {nombre_secret} en {tentatives} tentatives!")
    elif nombre_devin < nombre_secret:
        print(f"Tentative {tentatives}: {nombre_devin} - Trop petit!")
    else:
        print(f"Tentative {tentatives}: {nombre_devin} - Trop grand!")
    
    index = index + 1

print()
print("="*60)
print()

# =========================================================
# EXERCICE 9: break et continue
# =========================================================

print("EXERCICE 9: break et continue")
print("-" * 60)

# TODO: Utilisez continue pour sauter 5
print("Nombres de 0 à 9 (sauf 5):")
for i in range(10):
    if i == 5:
        continue  # Sauter cette itération
    print(i, end=" ")

print()
print()

# TODO: Utilisez break pour sortir à 7
print("Nombres de 0 à 9 (arrêt à 7):")
for i in range(10):
    if i == 7:
        break  # Sortir de la boucle
    print(i, end=" ")

print()
print()

print("="*60)
print()

# =========================================================
# EXERCICE 10: Somme avec Boucle et Condition
# =========================================================

print("EXERCICE 10: Somme avec Boucle et Condition")
print("-" * 60)

# TODO: Calculez la somme des nombres > 5
nombres = [2, 5, 8, 3, 10, 1, 7, 4, 9, 6]
somme = 0

for nombre in nombres:
    if nombre > 5:
        somme = somme + nombre

print(f"Liste: {nombres}")
print(f"Somme des nombres > 5: {somme}")
print(f"Explication: 8 + 10 + 7 + 9 + 6 = {somme}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 11: Pyramide d'Étoiles
# =========================================================

print("EXERCICE 11: Pyramide d'Étoiles")
print("-" * 60)

# TODO: Créez une pyramide
hauteur = 5

print("Pyramide:")
for i in range(1, hauteur + 1):
    etoiles = "*" * i
    print(etoiles)

print()
print("="*60)
print()

# =========================================================
# EXERCICE 12: Chercher dans une Liste
# =========================================================

print("EXERCICE 12: Chercher dans une Liste")
print("-" * 60)

# TODO: Trouvez un fruit dans la liste
fruits = ["pomme", "banane", "orange", "raisin", "fraise"]
recherche = "banane"
trouve = False

for fruit in fruits:
    if fruit == recherche:
        trouve = True
        break

if trouve:
    print(f"✅ '{recherche}' trouvé dans la liste!")
else:
    print(f"❌ '{recherche}' non trouvé dans la liste!")

print()

# TODO: Cherchez un autre fruit
recherche = "kiwi"
trouve = False

for fruit in fruits:
    if fruit == recherche:
        trouve = True
        break

if trouve:
    print(f"✅ '{recherche}' trouvé dans la liste!")
else:
    print(f"❌ '{recherche}' non trouvé dans la liste!")

print()
print("="*60)
print()

# =========================================================
# DÉFI BONUS 1: Jeu Nombre Secret (Amélioré) 🏆
# =========================================================

print("DÉFI BONUS 1: Jeu Nombre Secret")
print("-" * 60)

nombre_secret = 5
trouve = False
tentatives = 0

print("Devinez le nombre secret (1-10)")
print()

# Simulation avec prédéfinies
predictions = [7, 3, 5]

for prediction in predictions:
    tentatives = tentatives + 1
    
    if prediction == nombre_secret:
        print(f"✅ Bravo! Vous avez trouvé {nombre_secret} en {tentatives} tentatives!")
        trouve = True
        break
    elif prediction < nombre_secret:
        print(f"Tentative {tentatives}: {prediction} - Trop petit! 📈")
    else:
        print(f"Tentative {tentatives}: {prediction} - Trop grand! 📉")

if not trouve:
    print(f"Dommage! Le nombre secret était {nombre_secret}.")

print()
print("="*60)
print()

# =========================================================
# DÉFI BONUS 2: Calculatrice Simple 🏆
# =========================================================

print("DÉFI BONUS 2: Calculatrice Simple")
print("-" * 60)

nombre1 = 10
nombre2 = 3
operation = "*"

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        resultat = "Erreur: Division par zéro!"
else:
    resultat = "Opération invalide!"

print(f"Calcul: {nombre1} {operation} {nombre2}")
print(f"Résultat: {resultat}")

print()
print("="*60)
print("✅ Bravo! Vous avez complété tous les exercices de la Semaine 3!")
print("📝 N'hésitez pas à modifier et expérimenter avec le code.")
print("↩️  Préparez-vous pour la Semaine 4!")
print("="*60)