# Mon application

## Exercice 1 

```
myproject/ 
├── app.py 
├── components/ 
│ ├── __init__.py 
│ └── mymodule.py
└── README.md
```

* Créer l’arborescence de l’app
* A quoi sert `__init__.py` ? 
* Créer un environnement virtuel
* Utiliser un environnement virtuel
* Créer le composant
* Utiliser le composant depuis app
* Documenter les fonctions
* Documenter le README
* Importer numpy?

`pip install numpy`


## Exercice 2

```
myproject/ 
├── app.py 
├── components/ 
│ ├── __init__.py 
│ └── mymodule.py
├── test/ 
│ └── test.py
└── README.md
```
* Créer le dossier test
* Créer des tests 

`pip install pytest`
`pytest test/test.py`

## Exercice 3

```
myproject/ 
├── app.py 
├── components/ 
│ ├── __init__.py 
│ ├── data_sc.py 
│ └── mymodule.py
├── data/ 
│ ├── data_in.csv
│ └── data_clean.csv 
├── test/ 
│ └── test.py
└── README.md
```
* Créer le dossier data
* Créer le fichier data_sc pour analyser nettoyer et enregistrer votre csv
* Documenter le README

`pip install pandas` 

## Exercice 4 

```
myproject/ 
├── app.py 
├── components/ 
│ ├── __init__.py 
│ ├── data_sc.py 
│ └── create_model.py
├── data/ 
│ ├── data_in.csv
│ └── data_clean.csv 
├── test/ 
│ └── test.py
├── ML/ 
│ ├── encoder.sav
│ └── model.sav
└── README.md
```

* Créer le dossier ML
* Créer votre model de ML avec composant create_model
* sauvegarder votre encoder (preprocessing)
* sauvegarder votre modèle

`pip install scikit-learn`
`pip install pickle`

## Exercice 5 

* Créer un composant pour les figures
* un dossier pour sauvegarder les figures importantes
* Découvrir PIP FREEZE
* PIP INSTALL requirement.txt
  
`pip install matplotlib`

Creation static/img 

`pip freeze > requirements.txt`
`pip install -r requirements.txt`


```
app
├── app.py
├── static
│   └── css
│       └── style.css
│   └── images
│       └── logo.png
│   └── js
│       └── script.js
└── templates
    └── index.html
    ```