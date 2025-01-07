# Analyse des données des salles de cinéma

## Objectif
Ce projet vise à analyser les données des salles de cinéma en Île-de-France, en utilisant des techniques de nettoyage, d'exploration, et d'analyse de corrélation.

---

## Étapes du projet

### Exercice 1 : Nettoyage et exploration des données (5 pts)
- **Nettoyage des données :**
  - Les valeurs manquantes ont été identifiées et remplacées par la moyenne (colonnes : `entrées 2021`).
- **Exploration :**
  - Les premières lignes du dataset ont été affichées.
  - Statistiques descriptives sur les colonnes `écrans`, `fauteuils`, et `entrées annuelles`.

### Exercice 2 : Analyse des données (4 pts)
- Calcul des **entrées moyennes par fauteuil** pour chaque région.
- Identification des **meilleures et pires régions**.
- Création d’un **graphique à barres** représentant les entrées moyennes par fauteuil.

### Exercice 3 : Corrélations entre infrastructures et fréquentation (4 pts)
- Calcul des corrélations entre :
  - Le nombre d’écrans et les entrées annuelles.
  - Le nombre de fauteuils et les entrées annuelles.
- Création de **nuages de points** avec une régression linéaire superposée.

---

## Comment exécuter les scripts ?
1. Clonez ce dépôt :
   ```bash
   git clone <URL_du_dépôt>
   cd CinemaDataAnalysis
