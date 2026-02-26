import numpy as np

class OrdinaryLeastSquares:
    """Classe implémentant une régression linéaire OLS simple sans sklearn."""
    def __init__(self):
        self.coef_ = None  
        self.x_matrix = None      
        self.y = None     

    def fit(self, x_matrix, y):
        """
        Calcule les coefficients du modèle selon la méthode des moindres carrés :
        β̂ = (Xᵀ X)⁻¹ Xᵀ y
        """
        # Ajout d'une colonne de 1 pour l'intercept
        ones = np.ones((x_matrix.shape[0], 1))
        self.x_matrix = np.hstack([ones, x_matrix])
        self.y = y.reshape(-1, 1) if y.ndim == 1 else y

        # Calcul analytique des coefficients
        xtx_inv = np.linalg.inv(self.x_matrix.T @ self.x_matrix)
        self.coef_ = xtx_inv @ self.x_matrix.T @ self.y

    def predict(self, x_new):
        """
        Calcule les prédictions pour une nouvelle matrice X.
        """
        ones = np.ones((x_new.shape[0], 1))
        x_new_biased = np.hstack([ones, x_new])
        return x_new_biased @ self.coef_

    def get_coeffs(self):
        """
        Retourne les coefficients (intercept + pondérations)
        """
        return self.coef_.flatten()

    def determination_coefficient(self, x_test, y_test):
        """
        Calcule le R² : proportion de variance expliquée
        """
        y_test = y_test.reshape(-1, 1) if y_test.ndim == 1 else y_test
        y_pred = self.predict(x_test)
        ss_total = ((y_test - y_test.mean())**2).sum()
        ss_res = ((y_test - y_pred)**2).sum()
        return 1 - ss_res / ss_total

    def summary(self):
        """
        Affiche un résumé du modèle : coefficients et R²
        """
        print(" Résumé du modèle linéaire OLS :\n")
        print("Coefficients :")
        for idx, coef in enumerate(self.get_coeffs()):
            label = "Intercept" if idx == 0 else f"x{idx}"
            print(f"  {label} : {coef:.4f}")
        print()
