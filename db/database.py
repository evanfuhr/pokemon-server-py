import sqlite3
from db import queries

path_to_db = 'db/pokedex.db'
local_language_id = 9 # English

def get_pokemon_by_id(pokemon_id, version_group_id):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(queries.get_pokemon_by_id % (pokemon_id, local_language_id))
    r = c.fetchone()
    pokemon = {
        'id': pokemon_id,
        'name': str(r[1]),
        'height': r[2],
        'weight': r[3],
        'base_exp': r[4],
        'order': r[5],
        'is_default': r[6],
        'gender_rate': r[7],
        'genus': r[8]
    }

    types = []
    c.execute(queries.get_types_by_pokemon % (pokemon_id, local_language_id))
    for row in c.fetchall():
        ptype = {
            'id': row[0],
            'slot': row[1],
            'name': row[2]
        }
        types.append(ptype)
    pokemon['types'] = types

    moves = []
    c.execute(queries.get_moves_by_pokemon % (version_group_id, pokemon_id, version_group_id, local_language_id))
    for row in c.fetchall():
        move = {
            'id': row[0],
            'method_id': row[1],
            'level': row[2],
            'TM': row[3],
            'name': row[4],
            'type_id': row[5]
        }
        moves.append(move)
    pokemon['moves'] = moves
    c.close()

    return pokemon


def get_filtered_pokemon(version_group_id, ability_id, egg_group_id, move_id, type_id):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()

    if ability_id is not None:
        c.close()
        return "ability"
    elif egg_group_id is not None:
        c.close()
        return "egg_group"
    elif move_id is not None:
        c.close()
        return "move"
    elif type_id is not None:
        c.close()
        return "type"
    else:
        c.close()
        return "error"