from flask import Flask, request
from db import database
from db import queries

version_group_id = 18  # USUM

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/pokemon/<int:pokemon_id>")
def pokemon(pokemon_id):
    global version_group_id
    if request.args.get('version_group_id'):
        version_group_id = request.args.get('version_group_id')
    pokemon = database.get_pokemon_by_id(pokemon_id, version_group_id)
    return pokemon

@app.route("/pokemon")
def filtered_pokemon():
    global version_group_id
    if request.args.get('version_group_id'):
        version_group_id = request.args.get('version_group_id')
    ability_id = request.args.get('ability_id')
    egg_group_id = request.args.get('egg_group_id')
    move_id = request.args.get('move_id')
    type_id = request.args.get('type_id')
    pokemon_list = database.get_filtered_pokemon(version_group_id, ability_id, egg_group_id, move_id, type_id)
    return pokemon_list

if __name__ == "__main__":
    app.run(debug=True)