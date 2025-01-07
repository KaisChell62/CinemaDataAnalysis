import pandas as pd

# Données actuelles du cinéma fictif
ecrans_actuels = 2
fauteuils_actuels = 120
population_commune = 20000

# Coefficients moyens estimés des corrélations (d'après l'exercice 3)
coeff_ecrans = 50000  # Entrées supplémentaires par écran
coeff_fauteuils = 200  # Entrées supplémentaires par fauteuil

# Stratégies possibles
# Option 1 : Augmenter le nombre d'écrans
nouveaux_ecrans = ecrans_actuels + 1
impact_augmentation_ecrans = (nouveaux_ecrans - ecrans_actuels) * coeff_ecrans

# Option 2 : Augmenter le nombre de fauteuils
nouveaux_fauteuils = fauteuils_actuels + 50
impact_augmentation_fauteuils = (nouveaux_fauteuils - fauteuils_actuels) * coeff_fauteuils

# Résultats des stratégies
print("Stratégie 1 : Augmenter le nombre d'écrans")
print(f"Nombre d'écrans : {nouveaux_ecrans}")
print(f"Impact estimé : {impact_augmentation_ecrans} entrées annuelles supplémentaires\n")

print("Stratégie 2 : Augmenter le nombre de fauteuils")
print(f"Nombre de fauteuils : {nouveaux_fauteuils}")
print(f"Impact estimé : {impact_augmentation_fauteuils} entrées annuelles supplémentaires\n")

# Recommandation
if impact_augmentation_ecrans > impact_augmentation_fauteuils:
    print("Recommandation : Augmenter le nombre d'écrans")
else:
    print("Recommandation : Augmenter le nombre de fauteuils")
