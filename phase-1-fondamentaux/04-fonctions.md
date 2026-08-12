# 📚 Semaine 4: Les Fonctions

## 🎯 Objectifs
- Comprendre et créer des fonctions
- Utiliser les paramètres et les arguments
- Utiliser le return (retour)
- Appeler des fonctions
- Maîtriser la réutilisabilité du code

---

## 1️⃣ Introduction aux Fonctions

Une **fonction** est un bloc de code **réutilisable** qui effectue une tâche spécifique.

### **Pourquoi les fonctions?**

```python
# Sans fonction: Répétition
print("Bonjour Alice")
print("Bonjour Bob")
print("Bonjour Charlie")

# Avec fonction: Réutilisable
def saluer(nom):
    print(f"Bonjour {nom}")

saluer("Alice")
saluer("Bob")
saluer("Charlie")
```

---

## 2️⃣ Créer une Fonction Simple

### **Syntaxe:**

```python
def nom_de_la_fonction():
    # Code à exécuter
    print("Ceci est une fonction!")
```

### **Exemple 1: Fonction sans Paramètre**

```python
def dire_bonjour():
    print("Bonjour!")
    print("Bienvenue en Python!")

# Appeler la fonction
dire_bonjour()
dire_bonjour()

# Affiche:
# Bonjour!
# Bienvenue en Python!
# Bonjour!
# Bienvenue en Python!
```

### **Exemple 2: Fonction avec Une Tâche**

```python
def afficher_info():
    nom = "Alice"
    age = 25
    print(f"Nom: {nom}")
    print(f"Age: {age}")

afficher_info()
```

---

## 3️⃣ Paramètres et Arguments

Les **paramètres** permettent à une fonction de **recevoir des données**.

### **Syntaxe:**

```python
def fonction(parametre1, parametre2):
    # Utiliser les paramètres
    print(parametre1)
    print(parametre2)

# Appel avec arguments
fonction("valeur1", "valeur2")
```

### **Exemple 1: Un Paramètre**

```python
def saluer(nom):
    print(f"Bonjour {nom}!")

saluer("Alice")      # Affiche: Bonjour Alice!
saluer("Bob")        # Affiche: Bonjour Bob!
saluer("Charlie")    # Affiche: Bonjour Charlie!
```

### **Exemple 2: Plusieurs Paramètres**

```python
def additionner(a, b):
    resultat = a + b
    print(f"{a} + {b} = {resultat}")

additionner(5, 3)     # Affiche: 5 + 3 = 8
additionner(10, 20)   # Affiche: 10 + 20 = 30
```

### **Exemple 3: Paramètres par Défaut**

```python
def saluer(nom, titre="Monsieur"):
    print(f"Bonjour {titre} {nom}!")

saluer("Dupont")                    # Monsieur Dupont
saluer("Dupont", "Professeur")      # Professeur Dupont
```

---

## 4️⃣ Return (Retour de Valeur)

Le **return** permet à une fonction de **renvoyer une valeur**.

### **Syntaxe:**

```python
def fonction(parametre):
    resultat = parametre * 2
    return resultat

valeur = fonction(5)
print(valeur)  # 10
```

### **Exemple 1: Retourner une Valeur**

```python
def additionner(a, b):
    return a + b

resultat = additionner(5, 3)
print(resultat)  # 8

# Utiliser directement
print(additionner(10, 20))  # 30
```

### **Exemple 2: Retourner un Texte**

```python
def creer_message(nom):
    message = f"Bonjour {nom}!"
    return message

resultat = creer_message("Alice")
print(resultat)  # Bonjour Alice!
```

### **Exemple 3: Retourner Plusieurs Valeurs**

```python
def obtenir_info():
    nom = "Alice"
    age = 25
    return nom, age

# Récupérer les valeurs
nom, age = obtenir_info()
print(f"{nom} a {age} ans")  # Alice a 25 ans
```

### **Exemple 4: Fonction avec Condition et Return**

```python
def est_majeur(age):
    if age >= 18:
        return True
    else:
        return False

print(est_majeur(20))  # True
print(est_majeur(15))  # False
```

---

## 5️⃣ Exemples Pratiques

### **Exemple 1: Calculatrice**

```python
def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro!"

# Utiliser les fonctions
print(additionner(10, 5))      # 15
print(soustraire(10, 5))       # 5
print(multiplier(10, 5))       # 50
print(diviser(10, 5))          # 2.0
```

### **Exemple 2: Vérifications**

```python
def est_pair(nombre):
    return nombre % 2 == 0

def est_positif(nombre):
    return nombre > 0

def est_zero(nombre):
    return nombre == 0

print(est_pair(4))        # True
print(est_pair(5))        # False
print(est_positif(-5))    # False
print(est_positif(5))     # True
```

### **Exemple 3: Manipulation de Texte**

```python
def majuscules(texte):
    return texte.upper()

def minuscules(texte):
    return texte.lower()

def compter_lettres(texte):
    return len(texte)

print(majuscules("bonjour"))      # BONJOUR
print(minuscules("BONJOUR"))      # bonjour
print(compter_lettres("Python"))  # 6
```

### **Exemple 4: Avec Boucle**

```python
def somme_liste(nombres):
    total = 0
    for nombre in nombres:
        total = total + nombre
    return total

def moyenne_liste(nombres):
    if len(nombres) == 0:
        return 0
    return somme_liste(nombres) / len(nombres)

nombres = [10, 20, 30, 40, 50]
print(somme_liste(nombres))      # 150
print(moyenne_liste(nombres))    # 30.0
```

---

## 6️⃣ Scope (Portée des Variables)

Les variables à **l'intérieur** d'une fonction sont **locales**.

### **Exemple 1: Variable Locale**

```python
def fonction():
    x = 10  # Variable locale
    print(x)

fonction()  # Affiche: 10
print(x)    # Erreur! x n'existe pas ici
```

### **Exemple 2: Variable Globale**

```python
x = 10  # Variable globale

def fonction():
    print(x)  # Peut accéder à x

fonction()  # Affiche: 10
print(x)    # Affiche: 10
```

### **Exemple 3: Éviter les Confusions**

```python
def additionner(a, b):
    resultat = a + b  # Variable locale
    return resultat

x = additionner(5, 3)
print(x)  # 8
```

---

## 7️⃣ Bonnes Pratiques

### **1. Noms Significatifs**

```python
# ❌ Mauvais
def f(x):
    return x * 2

# ✅ Bon
def doubler(nombre):
    return nombre * 2
```

### **2. Documentation (Docstring)**

```python
def saluer(nom):
    """Salue une personne par son nom."""
    return f"Bonjour {nom}!"

help(saluer)  # Affiche la documentation
```

### **3. Une Fonction = Une Tâche**

```python
# ❌ Trop de tâches
def faire_tout(nom, age):
    print(f"Bonjour {nom}")
    print(f"Age: {age}")
    calcul = age * 2
    return calcul

# ✅ Fonctions spécialisées
def saluer(nom):
    return f"Bonjour {nom}"

def calculer_double_age(age):
    return age * 2
```

---

## 📝 Résumé

| Concept | Explication | Exemple |
|---------|-------------|---------|
| **def** | Définir une fonction | `def saluer(nom):` |
| **Paramètre** | Variable reçue | `def f(x, y):` |
| **Argument** | Valeur passée | `f(5, 10)` |
| **return** | Renvoyer une valeur | `return x + y` |
| **Appel** | Exécuter la fonction | `saluer("Alice")` |
| **Scope** | Portée des variables | Variables locales/globales |

---

## 🎯 À Retenir

1. **def** crée une fonction
2. **Les paramètres** permettent de passer des données
3. **return** renvoie une valeur
4. **Les fonctions** rendent le code réutilisable
5. **Les variables locales** n'existent que dans la fonction

---

**Prêt pour les exercices? 👉 Allez au dossier `exercices/`**