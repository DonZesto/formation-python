# 📚 Semaine 3: Structures de Contrôle

## 🎯 Objectifs
- Comprendre et utiliser `if`, `elif`, `else`
- Maîtriser les boucles `for`
- Maîtriser les boucles `while`
- Combiner les structures de contrôle

---

## 1️⃣ Structures Conditionnelles: if, elif, else

Les structures conditionnelles permettent de **prendre des décisions** dans votre code.

### **if (Si):**

Exécute un bloc de code **si une condition est vraie**.

```python
age = 18

if age >= 18:
    print("Vous êtes adulte")

# Affiche: Vous êtes adulte
```

### **else (Sinon):**

Exécute un bloc de code **si la condition est fausse**.

```python
age = 15

if age >= 18:
    print("Vous êtes adulte")
else:
    print("Vous êtes mineur")

# Affiche: Vous êtes mineur
```

### **elif (Sinon si):**

Teste **plusieurs conditions** une après l'autre.

```python
note = 75

if note >= 90:
    print("Excellent!")
elif note >= 80:
    print("Très bien!")
elif note >= 70:
    print("Bien!")
elif note >= 60:
    print("Acceptable")
else:
    print("Échec")

# Affiche: Bien!
```

### ⚠️ Important: Indentation

Python utilise **l'indentation** (espaces) pour délimiter les blocs:

```python
if age >= 18:
    print("Ligne 1 - Dans le if")
    print("Ligne 2 - Dans le if")
print("Ligne 3 - En dehors du if")
```

---

## 2️⃣ Boucles for

La boucle `for` répète un bloc de code **un nombre de fois défini**.

### **Syntaxe Basique:**

```python
for variable in sequence:
    # Code à répéter
```

### **Exemple 1: Répéter 5 fois**

```python
for i in range(5):
    print(i)

# Affiche:
# 0
# 1
# 2
# 3
# 4
```

### **range(n):**

- `range(5)` → 0, 1, 2, 3, 4 (5 nombres)
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (pas de 2)

```python
# De 1 à 5
for i in range(1, 6):
    print(i)

# De 0 à 10 par 2
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10
```

### **Exemple 2: Parcourir une liste**

```python
fruits = ["pomme", "banane", "orange"]

for fruit in fruits:
    print(fruit)

# Affiche:
# pomme
# banane
# orange
```

### **Exemple 3: Parcourir une chaîne**

```python
mot = "Python"

for lettre in mot:
    print(lettre)

# Affiche:
# P
# y
# t
# h
# o
# n
```

### **Exemple 4: Table de Multiplication**

```python
nombre = 7

for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")

# Affiche:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
```

---

## 3️⃣ Boucles while

La boucle `while` répète un bloc **tant qu'une condition est vraie**.

### **Syntaxe:**

```python
while condition:
    # Code à répéter
    # Modification de la condition
```

### **Exemple 1: Compter jusqu'à 5**

```python
i = 0

while i < 5:
    print(i)
    i = i + 1  # Important: incrémenter!

# Affiche:
# 0
# 1
# 2
# 3
# 4
```

### **Exemple 2: Menu Interactif**

```python
choix = ""

while choix != "quitter":
    print("Menu:")
    print("1. Continuer")
    print("2. Quitter")
    choix = input("Votre choix: ")
    
    if choix == "1":
        print("Vous continuez...")
    elif choix == "2":
        print("Au revoir!")
        choix = "quitter"
```

### **⚠️ Attention: Boucle Infinie**

```python
while True:
    print("Ceci s'affiche indéfiniment!")
    # Aucun moyen de sortir!
```

**Toujours avoir une condition de sortie!**

### **break: Sortir de la boucle**

```python
i = 0

while True:
    print(i)
    if i >= 4:
        break  # Sortir de la boucle
    i = i + 1

# Affiche: 0, 1, 2, 3, 4
```

### **continue: Sauter une itération**

```python
for i in range(5):
    if i == 2:
        continue  # Sauter cette itération
    print(i)

# Affiche: 0, 1, 3, 4 (2 est sauté)
```

---

## 4️⃣ Combiner if et Boucles

### **Exemple 1: Afficher les nombres pairs**

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} est pair")

# Affiche:
# 2 est pair
# 4 est pair
# 6 est pair
# 8 est pair
# 10 est pair
```

### **Exemple 2: Somme avec Condition**

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somme = 0

for nombre in nombres:
    if nombre > 5:
        somme = somme + nombre

print(somme)  # Affiche: 40 (6+7+8+9+10)
```

### **Exemple 3: Trouver un Élément**

```python
fruits = ["pomme", "banane", "orange", "raisin"]
recherche = "banane"
trouve = False

for fruit in fruits:
    if fruit == recherche:
        trouve = True
        break

if trouve:
    print(f"{recherche} trouvé!")
else:
    print(f"{recherche} non trouvé!")

# Affiche: banane trouvé!
```

---

## 5️⃣ Exemples Pratiques

### **Exemple 1: Calculatrice Simple**

```python
nombre1 = 10
nombre2 = 3
operation = "+"

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    resultat = nombre1 / nombre2
else:
    resultat = "Opération invalide"

print(f"{nombre1} {operation} {nombre2} = {resultat}")
```

### **Exemple 2: Jeu Nombre Secret**

```python
nombre_secret = 7
tentatives = 0

while True:
    nombre = int(input("Devinez le nombre (1-10): "))
    tentatives = tentatives + 1
    
    if nombre == nombre_secret:
        print(f"Bravo! Vous avez trouvé en {tentatives} tentatives!")
        break
    elif nombre < nombre_secret:
        print("Trop petit!")
    else:
        print("Trop grand!")
```

### **Exemple 3: Pyramide d'Étoiles**

```python
hauteur = 5

for i in range(1, hauteur + 1):
    etoiles = "*" * i
    print(etoiles)

# Affiche:
# *
# **
# ***
# ****
# *****
```

---

## 📝 Résumé

| Structure | Utilisation | Exemple |
|-----------|-------------|---------|
| **if** | Tester UNE condition | `if age >= 18:` |
| **elif** | Tester PLUSIEURS conditions | `elif age >= 13:` |
| **else** | Si aucune condition | `else:` |
| **for** | Répéter un nombre DÉFINI de fois | `for i in range(5):` |
| **while** | Répéter tant qu'une condition est VRAIE | `while i < 5:` |
| **break** | Sortir d'une boucle | `break` |
| **continue** | Sauter une itération | `continue` |

---

## 🎯 À Retenir

1. **if/elif/else** = prendre des décisions
2. **for** = répéter un nombre connu de fois
3. **while** = répéter tant qu'une condition est vraie
4. **Indentation** = très importante en Python!
5. **break** = sortir d'une boucle
6. **continue** = sauter à l'itération suivante

---

**Prêt pour les exercices? 👉 Allez au dossier `exercices/`**