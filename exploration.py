import pandas as pd

# Charger les données
file_path = "../data/salle_de_cinema_ile-de-france.csv"
try:
    data = pd.read_csv(file_path, sep=";", encoding="utf-8")
except FileNotFoundError:
    print("Le fichier CSV n'a pas été trouvé.")
    exit()

# Identifier les valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(data.isnull().sum())

# Nettoyer les données (remplacer les valeurs manquantes)
data['entrées 2021'] = data['entrées 2021'].fillna(data['entrées 2021'].mean())

# Afficher un aperçu des données
print("\nAperçu des données après nettoyage :")
print(data.head())

# Statistiques descriptives
print("\nStatistiques descriptives :")
print(data[['écrans', 'fauteuils', 'entrées 2022']].describe())
