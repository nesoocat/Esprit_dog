import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
import joblib

# Charger le jeu de données diabetes
diabetes = pd.read_csv('data/diabetes.csv', sep=',')
X = diabetes.drop(columns='Outcome')
y = diabetes['Outcome']

# Diviser le jeu de données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Créer un pipeline avec un scaler et un classificateur RandomForest
pipeline = make_pipeline(
    StandardScaler(),
    RandomForestClassifier(n_estimators=100, random_state=42)
)

#tuner les hyperparamètres (optionnel)
param_grid = {
    'randomforestclassifier__n_estimators': [50, 100, 200],
    'randomforestclassifier__max_depth': [None, 10, 20],
    'randomforestclassifier__min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)
pipeline = grid_search.best_estimator_

# Entraîner le modèle
pipeline.fit(X_train, y_train)
# Faire des prédictions
y_pred = pipeline.predict(X_test)

# Évaluer le modèle
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Sauvegarder le modèle entraîné
joblib.dump(pipeline, 'diabetes_model.pkl')