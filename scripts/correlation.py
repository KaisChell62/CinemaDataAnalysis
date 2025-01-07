import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
file_path = "C:/Users/KCHELHAOUI/OneDrive - VINCI Construction/Documents/CinemaDataAnalysis/data/salle_de_cinema_ile-de-france.csv"
data = pd.read_csv(file_path, sep=";", encoding="utf-8")


# Filtrer les données pour ne garder que l'année 2022
data_2022 = data[['écrans', 'fauteuils', 'entrées 2022']].dropna()

# Calculer et afficher les corrélations
print("\nCorrélations entre les variables :")
correlations = data_2022.corr()
print(correlations)

# Graphique : Nombre d'écrans vs Entrées 2022
plt.figure(figsize=(8, 6))
sns.regplot(x='écrans', y='entrées 2022', data=data_2022, color="blue", scatter_kws={"s": 10})
plt.title("Corrélation entre le nombre d'écrans et les entrées 2022")
plt.xlabel("Nombre d'écrans")
plt.ylabel("Entrées 2022")
plt.savefig("../output/correlation_ecrans_entrees_2022.png")
plt.show()

# Graphique : Nombre de fauteuils vs Entrées 2022
plt.figure(figsize=(8, 6))
sns.regplot(x='fauteuils', y='entrées 2022', data=data_2022, color="green", scatter_kws={"s": 10})
plt.title("Corrélation entre le nombre de fauteuils et les entrées 2022")
plt.xlabel("Nombre de fauteuils")
plt.ylabel("Entrées 2022")
plt.savefig("../output/correlation_fauteuils_entrees_2022.png")
plt.show()

# Répondre à la question
print("\nSelon les corrélations et les graphiques, identifiez la variable ayant le plus d'impact.")
