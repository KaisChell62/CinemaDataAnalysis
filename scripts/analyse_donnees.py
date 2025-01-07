import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = "../data/salle_de_cinema_ile-de-france.csv"
data = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Calcul des entrées moyennes par fauteuil pour chaque région
data['Entrées moyennes par fauteuil'] = data['entrées 2022'] / data['fauteuils']
region_data = data.groupby('région administrative')['Entrées moyennes par fauteuil'].mean().reset_index()

# Trier les régions par entrées moyennes
region_data = region_data.sort_values(by='Entrées moyennes par fauteuil', ascending=False)

# Afficher les 3 régions avec les meilleurs et pires résultats
print("3 meilleures régions :")
print(region_data.head(3))
print("\n3 pires régions :")
print(region_data.tail(3))
