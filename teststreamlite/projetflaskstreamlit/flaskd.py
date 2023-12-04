from flask import Flask, jsonify

app = Flask(__name__)

# Chargez le dataset 20 Newsgroups (uniquement à titre d'exemple, vous pouvez utiliser un autre jeu de données)
from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# Ajoutez la catégorie de chaque article aux données
data_with_category = [{"Category": newsgroups.target_names[newsgroups.target[i]], "Text": text} for i, text in enumerate(newsgroups.data)]

@app.route('/api/data')
def get_data():
    return jsonify(data_with_category)

if __name__ == '__main__':
    app.run(debug=True)
