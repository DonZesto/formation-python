# IMPORTANT: Lisez les commentaires et complétez les exercices!
# Chaque exercice correspond au cours 02-operateurs.md

print("="*60)
print("SEMAINE 2: OPÉRATEURS - EXERCICES")
print("="*60)
print()

# =========================================================
# EXERCICE 1: Opérateurs Arithmétiques - Calculs Simples
# =========================================================

print("EXERCICE 1: Opérateurs Arithmétiques")
print("-" * 60)

# TODO: Complétez les calculs
nombre1 = 15
nombre2 = 4

addition = nombre1 + nombre2
soustraction = nombre1 - nombre2
multiplication = nombre1 * nombre2
division = nombre1 / nombre2
division_entiere = nombre1 // nombre2
modulo = nombre1 % nombre2
puissance = nombre1 ** 2

print(f"{nombre1} + {nombre2} = {addition}")
print(f"{nombre1} - {nombre2} = {soustraction}")
print(f"{nombre1} * {nombre2} = {multiplication}")
print(f"{nombre1} / {nombre2} = {division}")
print(f"{nombre1} // {nombre2} = {division_entiere}")
print(f"{nombre1} % {nombre2} = {modulo}")
print(f"{nombre1} ** 2 = {puissance}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 2: Calculs Pratiques
# =========================================================

print("EXERCICE 2: Calculs Pratiques")
print("-" * 60)

# TODO: Calculez le total avec TVA
prix_article = 50.00
quantite = 3
tva = 0.20  # 20% de TVA

sous_total = prix_article * quantite
montant_tva = sous_total * tva
total_ttc = sous_total + montant_tva

print(f"Prix unitaire: {prix_article}€")
print(f"Quantité: {quantite}")
print(f"Sous-total: {sous_total}€")
print(f"TVA (20%): {montant_tva}€")
print(f"Total TTC: {total_ttc}€")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 3: Opérateurs de Comparaison
# =========================================================

print("EXERCICE 3: Opérateurs de Comparaison")
print("-" * 60)

age = 25
age_minimum = 18

# TODO: Complétez les comparaisons
est_adulte = age >= age_minimum
est_majeur = age > 18
est_moins_de_30 = age < 30
est_exactement_25 = age == 25
nest_pas_20 = age != 20

print(f"Age: {age}")
print(f"Est adulte (>= 18)? {est_adulte}")
print(f"Est majeur (> 18)? {est_majeur}")
print(f"Est moins de 30 (< 30)? {est_moins_de_30}")
print(f"Est exactement 25 (== 25)? {est_exactement_25}")
print(f"N'est pas 20 (!= 20)? {nest_pas_20}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 4: Comparaison de Texte
# =========================================================

print("EXERCICE 4: Comparaison de Texte")
print("-" * 60)

nom = "Alice"
motdepasse = "python123"

# TODO: Vérifiez les valeurs
nom_correct = nom == "Alice"
motdepasse_correct = motdepasse == "python123"
nom_incorrect = nom != "Bob"

print(f"Nom: {nom}")
print(f"Nom correct? {nom_correct}")
print(f"Mot de passe correct? {motdepasse_correct}")
print(f"Nom n'est pas Bob? {nom_incorrect}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 5: Opérateurs Logiques - and (ET)
# =========================================================

print("EXERCICE 5: Opérateurs Logiques - and (ET)")
print("-" * 60)

age = 25
permis = True
assurance = True

# TODO: Utilisez and pour combiner les conditions
peut_conduire = age >= 18 and permis == True and assurance == True

print(f"Age: {age}")
print(f"Permis: {permis}")
print(f"Assurance: {assurance}")
print(f"Peut conduire (age >= 18 AND permis AND assurance)? {peut_conduire}")

# Teste avec une condition fausse
permis = False
peut_conduire_2 = age >= 18 and permis == True and assurance == True
print(f"\nSans permis: {peut_conduire_2}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 6: Opérateurs Logiques - or (OU)
# =========================================================

print("EXERCICE 6: Opérateurs Logiques - or (OU)")
print("-" * 60)

jour = "samedi"

# TODO: Utilisez or pour vérifier le weekend
est_weekend = (jour == "samedi") or (jour == "dimanche")

print(f"Jour: {jour}")
print(f"C'est le weekend? {est_weekend}")

jour = "lundi"
est_weekend = (jour == "samedi") or (jour == "dimanche")
print(f"\nJour: {jour}")
print(f"C'est le weekend? {est_weekend}")

jour = "dimanche"
est_weekend = (jour == "samedi") or (jour == "dimanche")
print(f"\nJour: {jour}")
print(f"C'est le weekend? {est_weekend}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 7: Opérateurs Logiques - not (NON)
# =========================================================

print("EXERCICE 7: Opérateurs Logiques - not (NON)")
print("-" * 60)

connecte = True
is_online = not connecte

print(f"Connecté: {connecte}")
print(f"En ligne (not connecté): {is_online}")

connecte = False
is_online = not connecte
print(f"\nConnecté: {connecte}")
print(f"En ligne (not connecté): {is_online}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 8: Combinaison Complexe d'Opérateurs
# =========================================================

print("EXERCICE 8: Combinaison Complexe")
print("-" * 60)

# Vérifier si quelqu'un peut regarder un film
age = 16
genre_film = "action"
a_de_l_argent = True
est_weekend = True

# TODO: Complétez la logique
peut_regarder = (age >= 13) and (a_de_l_argent == True)
peut_sortir = (est_weekend == True) or (age >= 18)
peut_regarder_avec_parents = (age < 18) and (genre_film != "horror")

print(f"Age: {age}")
print(f"Genre: {genre_film}")
print(f"A de l'argent: {a_de_l_argent}")
print(f"C'est le weekend: {est_weekend}")
print()
print(f"Peut regarder (>= 13 AND a l'argent)? {peut_regarder}")
print(f"Peut sortir (weekend OR age >= 18)? {peut_sortir}")
print(f"Peut regarder avec parents (< 18 AND pas horror)? {peut_regarder_avec_parents}")

print()
print("="*60)
print()

# =========================================================
# EXERCICE 9: Ordre des Opérations
# =========================================================

print("EXERCICE 9: Ordre des Opérations")
print("-" * 60)

# TODO: Calculez sans et avec parenthèses
resultat_sans_parentheses = 2 + 3 * 4
resultat_avec_parentheses = (2 + 3) * 4

print(f"2 + 3 * 4 = {resultat_sans_parentheses} (multiplication d'abord)")
print(f"(2 + 3) * 4 = {resultat_avec_parentheses} (parenthèses d'abord)")

# Autre exemple
resultat1 = 10 + 5 * 2
resultat2 = (10 + 5) * 2

print(f"\n10 + 5 * 2 = {resultat1}")
print(f"(10 + 5) * 2 = {resultat2}")

print()
print("="*60)
print()

# =========================================================
# DÉFI BONUS 🏆
# =========================================================

print("DÉFI BONUS: Système de Note")
print("-" * 60)

# TODO: Créez un système qui vérifie si quelqu'un a réussi
note = 72
note_minimum = 60
note_excellente = 90

a_reussi = note >= note_minimum
est_excellent = note >= note_excellente
est_en_danger = (note < 60) and (note >= 40)
est_echec = note < 40

print(f"Note: {note}")
print(f"A réussi (>= 60)? {a_reussi}")
print(f"Excellent (>= 90)? {est_excellent}")
print(f"En danger (40-60)? {est_en_danger}")
print(f"Échec (< 40)? {est_echec}")

# Créer un message
if a_reussi:
    if est_excellent:
        message = "Excellent travail! 🌟"
    else:
        message = "Bien joué! 👍"
else:
    if est_en_danger:
        message = "Attention, vous êtes en danger ⚠️"
    else:
        message = "Vous avez échoué 😞"

print(f"\nMessage: {message}")

print()
print("="*60)
print("✅ Bravo! Vous avez complété tous les exercices de la Semaine 2!")
print("📝 N'hésitez pas à modifier et expérimenter avec le code.")
print("↩️  Préparez-vous pour la Semaine 3!")
print("="*60)