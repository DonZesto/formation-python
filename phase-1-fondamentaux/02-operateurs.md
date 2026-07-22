# 📚 Semaine 2: Opérateurs

## 🎯 Objectifs
- Comprendre les opérateurs arithmétiques
- Découvrir les opérateurs de comparaison
- Maîtriser les opérateurs logiques
- Utiliser les opérateurs dans vos programmes

---

## 1️⃣ Opérateurs Arithmétiques

Les opérateurs arithmétiques permettent de faire des **calculs mathématiques**.

### Les Opérateurs:

| Opérateur | Nom | Exemple | Résultat |
|-----------|-----|---------|----------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Soustraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 2` | `3.0` |
| `//` | Division entière | `7 // 2` | `3` |
| `%` | Modulo (reste) | `7 % 2` | `1` |
| `**` | Puissance | `2 ** 3` | `8` |

### Exemples:

```python
# Addition
prix = 10
taxe = 2
total = prix + taxe
print(total)  # Affiche: 12

# Multiplication
quantite = 5
prix_unitaire = 2.50
total = quantite * prix_unitaire
print(total)  # Affiche: 12.5

# Division
distance = 100
temps = 2
vitesse = distance / temps
print(vitesse)  # Affiche: 50.0

# Division entière (sans décimales)
personnes = 7
pizzas = 2
parts_par_pizza = personnes // pizzas
print(parts_par_pizza)  # Affiche: 3

# Modulo (reste)
oeufs = 13
boites = 12
reste = oeufs % boites
print(reste)  # Affiche: 1

# Puissance
base = 2
exposant = 3
resultat = base ** exposant
print(resultat)  # Affiche: 8
```

### Ordre des Opérations (PEMDAS):

Python respecte l'ordre mathématique:
1. Parenthèses `()`
2. Puissances `**`
3. Multiplication `*`, Division `/`, Division entière `//`, Modulo `%`
4. Addition `+`, Soustraction `-`

```python
# Sans parenthèses
resultat = 2 + 3 * 4
print(resultat)  # Affiche: 14 (pas 20!)

# Avec parenthèses
resultat = (2 + 3) * 4
print(resultat)  # Affiche: 20
```

---

## 2️⃣ Opérateurs de Comparaison

Les opérateurs de comparaison **comparent deux valeurs** et retournent `True` ou `False`.

### Les Opérateurs:

| Opérateur | Nom | Exemple | Résultat |
|-----------|-----|---------|----------|
| `==` | Égal à | `5 == 5` | `True` |
| `!=` | Différent de | `5 != 3` | `True` |
| `>` | Plus grand que | `5 > 3` | `True` |
| `<` | Plus petit que | `5 < 3` | `False` |
| `>=` | Plus grand ou égal | `5 >= 5` | `True` |
| `<=` | Plus petit ou égal | `3 <= 5` | `True` |

### Exemples:

```python
# Égal
age = 18
print(age == 18)  # Affiche: True
print(age == 20)  # Affiche: False

# Différent
nom = "Alice"
print(nom != "Bob")  # Affiche: True

# Plus grand / Plus petit
score = 95
print(score > 80)   # Affiche: True
print(score < 100)  # Affiche: True
print(score >= 95)  # Affiche: True

# Avec des variables
temperature = 25
print(temperature > 20)    # Affiche: True
print(temperature < 30)    # Affiche: True
```

### ⚠️ Attention:

**Ne pas confondre:**
- `=` (assignation) → `age = 18`
- `==` (comparaison) → `age == 18`

```python
age = 18      # Assign 18 à age
age == 18     # Compare si age égal 18
```

---

## 3️⃣ Opérateurs Logiques

Les opérateurs logiques permettent de **combiner plusieurs conditions**.

### Les Opérateurs:

| Opérateur | Description | Exemple | Résultat |
|-----------|-------------|---------|----------|
| `and` | ET logique | `True and True` | `True` |
| `or` | OU logique | `True or False` | `True` |
| `not` | NON logique | `not True` | `False` |

### **and** (ET):

`and` retourne `True` **si TOUS les conditions sont True**

```python
age = 25
permis = True

# Les deux conditions doivent être vraies
print(age >= 18 and permis == True)  # Affiche: True

age = 15
# Une condition est fausse
print(age >= 18 and permis == True)  # Affiche: False
```

### **or** (OU):

`or` retourne `True` **si AU MOINS UNE condition est True**

```python
jour = "samedi"

# Au moins une condition est vraie
print(jour == "samedi" or jour == "dimanche")  # Affiche: True

jour = "lundi"
# Aucune condition n'est vraie
print(jour == "samedi" or jour == "dimanche")  # Affiche: False
```

### **not** (NON):

`not` **inverse la valeur** True/False

```python
connecte = True
print(not connecte)  # Affiche: False

connecte = False
print(not connecte)  # Affiche: True
```

### Exemples Combinés:

```python
# Vérifier si quelqu'un peut entrer au cinéma
age = 16
permis_parents = True
a_de_l_argent = True

peut_entrer = (age >= 16) and (permis_parents or a_de_l_argent)
print(peut_entrer)  # Affiche: True

# Vérifier si c'est le weekend
jour = "vendredi"
est_weekend = (jour == "samedi") or (jour == "dimanche")
print(est_weekend)  # Affiche: False
```

---

## 📊 Tables de Vérité

### and (ET):

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

### or (OU):

| A | B | A or B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

### not (NON):

| A | not A |
|---|-------|
| True | **False** |
| False | **True** |

---

## 🎯 Exemples Pratiques

### Exemple 1: Calculatrice Simple

```python
nombre1 = 10
nombre2 = 3

addition = nombre1 + nombre2
soustraction = nombre1 - nombre2
multiplication = nombre1 * nombre2
division = nombre1 / nombre2
reste = nombre1 % nombre2

print("Addition:", addition)           # 13
print("Soustraction:", soustraction)   # 7
print("Multiplication:", multiplication) # 30
print("Division:", division)           # 3.333...
print("Reste:", reste)                # 1
```

### Exemple 2: Vérifier l'Âge

```python
age = 25

est_adulte = age >= 18
peut_voter = age >= 18
peut_conduire = age >= 18

print("Est adulte?", est_adulte)      # True
print("Peut voter?", peut_voter)      # True
print("Peut conduire?", peut_conduire) # True

# Avec and
peut_faire_tout = est_adulte and peut_voter and peut_conduire
print("Peut faire tout?", peut_faire_tout)  # True
```

### Exemple 3: Vérifier le Weekend

```python
jour = "samedi"
heure = 10

est_weekend = (jour == "samedi") or (jour == "dimanche")
est_matin = heure < 12

print("C'est le weekend?", est_weekend)  # True
print("C'est le matin?", est_matin)     # True
print("Weekend et matin?", est_weekend and est_matin)  # True
```

---

## 📝 Résumé

| Type | Opérateur | Description |
|------|-----------|-------------|
| **Arithmétique** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Calculs mathématiques |
| **Comparaison** | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparent deux valeurs |
| **Logique** | `and`, `or`, `not` | Combinent des conditions |

---

## 🎯 À Retenir

1. **Opérateurs arithmétiques** = font des calculs
2. **Opérateurs de comparaison** = retournent True/False
3. **Opérateurs logiques** = combinent des conditions
4. **and** = tous doivent être vrais
5. **or** = au moins un doit être vrai
6. **not** = inverse la valeur

---

**Prêt pour les exercices? 👉 Allez au dossier `exercices/`**