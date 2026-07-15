# 📚 Semaine 1: Variables et Types de Données

## 🎯 Objectifs
- Comprendre qu'est-ce qu'une variable
- Découvrir les types de données en Python
- Créer vos premières variables
- Afficher des données avec `print()`

---

## 1️⃣ Qu'est-ce qu'une variable?

Une **variable** est une boîte qui contient une information. Vous lui donnez un **nom** et vous pouvez y stocker des **données**.

### Analogie:
```
Boîte (Variable) → Nom de la boîte (nom_variable) → Contenu (valeur)
```

---

## 2️⃣ Créer votre première variable

### Syntaxe:
```python
nom_variable = valeur
```

### Exemples:
```python
age = 25
nom = "Alice"
taille = 1.75
actif = True
```

**Explication:**
- `age = 25` → La variable `age` contient le nombre 25
- `nom = "Alice"` → La variable `nom` contient le texte "Alice"
- `taille = 1.75` → La variable `taille` contient le nombre décimal 1.75
- `actif = True` → La variable `actif` contient une valeur booléenne (vrai/faux)

---

## 3️⃣ Les Types de Données Principaux

### **int** (Entier)
Les nombres entiers (sans décimales)
```python
age = 30
temperature = -5
annee = 2026
```

### **float** (Décimal)
Les nombres avec décimales
```python
taille = 1.75
prix = 19.99
pi = 3.14159
```

### **str** (Texte/Chaîne de caractères)
Le texte entre guillemets simples ou doubles
```python
nom = "Alice"
prenom = 'Bob'
message = "Bonjour Python!"
```

### **bool** (Booléen)
Vrai ou Faux
```python
pluie = True
soleil = False
connecte = True
```

### **list** (Liste)
Une collection d'éléments
```python
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = ["Alice", 25, True, 3.14]
```

### **dict** (Dictionnaire)
Des paires clé-valeur
```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}
```

---

## 4️⃣ Afficher des variables avec `print()`

### Syntaxe:
```python
print(variable)
print("Texte", variable)
```

### Exemples:
```python
nom = "Alice"
age = 25

print(nom)                          # Affiche: Alice
print(age)                          # Affiche: 25
print("Mon nom est", nom)          # Affiche: Mon nom est Alice
print("J'ai", age, "ans")         # Affiche: J'ai 25 ans
```

---

## 5️⃣ Connaître le type d'une variable

Utilisez `type()` pour connaître le type d'une variable:

```python
age = 25
nom = "Alice"
taille = 1.75
actif = True

print(type(age))      # <class 'int'>
print(type(nom))      # <class 'str'>
print(type(taille))   # <class 'float'>
print(type(actif))    # <class 'bool'>
```

---

## 6️⃣ Règles de nommage des variables

✅ **BON:**
```python
mon_age = 25
monAge = 25
age25 = 25
AGE = 25
_age = 25
```

❌ **MAUVAIS:**
```python
mon-age = 25      # Tiret interdit
mon age = 25      # Espace interdit
25age = 25        # Ne commence pas par un chiffre
mon@age = 25      # Caractère spécial interdit
```

**Règles clés:**
- Commencez par une lettre ou un underscore `_`
- Utilisez uniquement des lettres, chiffres, et underscores
- Pas d'espaces ni de caractères spéciaux
- Python est sensible à la casse (`Age` ≠ `age`)

---

## 7️⃣ Modifier une variable

Vous pouvez changer la valeur d'une variable:

```python
age = 25
print(age)    # Affiche: 25

age = 26
print(age)    # Affiche: 26

age = age + 1
print(age)    # Affiche: 27
```

---

## 📝 Résumé

| Concept | Exemple | Description |
|---------|---------|-------------|
| Variable | `nom = "Alice"` | Stocke une valeur |
| int | `age = 25` | Nombre entier |
| float | `taille = 1.75` | Nombre décimal |
| str | `nom = "Alice"` | Texte |
| bool | `actif = True` | Vrai ou Faux |
| list | `[1, 2, 3]` | Collection d'éléments |
| print() | `print(nom)` | Affiche une valeur |
| type() | `type(age)` | Connaît le type |

---

## 🎯 À retenir

1. **Variable** = boîte contenant une information
2. **Les 4 types de base:** int, float, str, bool
3. **print()** = afficher
4. **type()** = connaître le type
5. **Règles de nommage** = commence par lettre/underscore, sans espaces

---

**Prêt pour les exercices? 👉 Allez au dossier `exercices/`**