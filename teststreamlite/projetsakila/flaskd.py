from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:_xZEaR0}d0C006XiGP;ey)u7OT=P6X5s@mariadb.ownedge.fr/sakila'
db = SQLAlchemy(app)

# Modèle SQLAlchemy pour la table "actor" de la base de données Sakila
class Actor(db.Model):
    __tablename__ = 'actor'
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    last_update = db.Column(db.DateTime)

@app.route('/api/actors')
def get_actors():
    # Interrogez la base de données pour récupérer des données de la table "actor"
    actors = Actor.query.all()
    # Convertissez les données en format JSON
    actor_data = [{"actor_id": actor.actor_id, "first_name": actor.first_name, "last_name": actor.last_name} for actor in actors]
    return jsonify(actor_data)

if __name__ == '__main__':
    app.run(debug=True)