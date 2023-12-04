import numpy as np
import pandas as pd 
from os.path import join
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
import pickle 
from components.drawplot import plotfig

def create_model(): 
    df = pd.read_csv(join("data","titanic_out.csv"))

    if True:
        # Séparer les données en données d'entraînement, de validation et de test
        print("train test split")
        X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["survived"]), df["survived"], test_size=0.2, random_state=42)


        # Normaliser les données numériques
        # scaler = StandardScaler()
        scaler = MinMaxScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        model = LogisticRegression()

        # Recherche d'hyperparamètres
        parameters = {"C": np.arange(0.1, 10, 0.1)}
        grid_search = GridSearchCV(model, parameters, cv=5, scoring="accuracy")
        grid_search.fit(X_train, y_train)

        # Meilleur modèle
        best_model = grid_search.best_estimator_

        # Évaluer le meilleur modèle sur les données de test
        print("Accuracy sur les données de test :", best_model.score(X_test, y_test))
        
        # save the model to disk
        filename = join('machinelearning','finalized_model.sav')
        pickle.dump(best_model, open(filename, 'wb'))

        # save the encoder to disk
        filename = join('machinelearning','encoder.sav')
        pickle.dump(scaler, open(filename, 'wb'))    

    plotfig(df)
