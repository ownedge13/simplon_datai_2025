import pandas as pd
from os.path import join 

def clean_save_csv():
    """ Clean the Titanic CSV File  """
    df = pd.read_csv(join("data","titanic.csv"))
    df.columns = df.columns.str.lower()

    # Remplacer les valeurs nulles de la colonne "age" par la moyenne de la colonne
    print("clean age")
    df["age"] = df["age"].fillna(df["age"].mean())

    # Supprimer les lignes qui contiennent des valeurs nulles dans la colonne "embarked"
    print("dropna embarked")
    df = df.dropna(subset=["embarked"])
    
    # Supprimer la colonne "cabin" car elle contient beaucoup de valeurs nulles
    print("drop cabin, passengid, ticket")
    df = df.drop("cabin", axis=1)

    # Supprimer la colonne "name" et "passengerid" car elles ne servent à rien pour du ML
    df = df.drop(["name","passengerid"], axis=1)

    # Supprimer la colonne "cabin" car elle contient beaucoup de valeurs nulles
    df = df.drop("ticket", axis=1)

    # Créer une liste des colonnes catégorielles
    print("get dummies")
    categorical_columns = ["pclass","sex","sibsp","parch", "embarked"]

    # Créer des colonnes hot encoder pour chaque colonne catégorielle
    for column in categorical_columns:
        df = pd.get_dummies(df, columns=[column])

    df.to_csv("./data/titanic_out.csv")