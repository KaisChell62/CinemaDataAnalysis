import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Charger les données
file_path = "../data/salle_de_cinema_ile-de-france.csv"
data = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Ajouter une colonne "année" au dataset si elle n'existe pas
if 'année' not in data.columns:
    print("Ajout de la colonne 'année' avec une valeur par défaut (par exemple, 2021).")
    data['année'] = 2021  # Ajustez cette valeur si nécessaire

# Gérer les valeurs manquantes dans la colonne 'entrées 2021'
if data['entrées 2021'].isnull().any():
    print("Des valeurs manquantes ont été détectées dans 'entrées 2021'. Elles seront remplacées par la moyenne.")
    data['entrées 2021'] = data['entrées 2021'].fillna(data['entrées 2021'].mean())

# Filtrer les données de 2018 à 2021
data_filtered = data[data['année'] <= 2021]

# Variables explicatives et cible
X = data_filtered[['écrans', 'fauteuils', 'population de la commune']]
y = data_filtered['entrées 2021']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Évaluer les performances
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

mae_train = mean_absolute_error(y_train, y_pred_train)
mae_test = mean_absolute_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)

print("\nPerformances du modèle :")
print(f"Erreur moyenne absolue (MAE) - Entraînement : {mae_train:.2f}")
print(f"Erreur moyenne absolue (MAE) - Test : {mae_test:.2f}")
print(f"Coefficient de détermination (R²) - Test : {r2:.2f}")
