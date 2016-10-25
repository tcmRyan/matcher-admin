import sqlite3
import os
import csv
from matcherAdmin import app, db
from matcherAdmin.models import Gamedata, Gametable

COL1 = "base"
COL2 = "combination"
COL3 = "result"
TABLE = "combinations"

def connect_db(filename):
    return sqlite3.connect(os.path.join(app.config['DB_FOLDER'], filename))

def load_from_csv(filename, replace=False):
    db_name =  filename.split('.')[0] + '.db'
    conn = connect_db(db_name)
    cursor = conn.cursor()
    if replace:
        cursor.executescript('DROP TABLE IF EXISTS {}'.format(TABLE))
  
    cursor.execute('CREATE TABLE IF NOT EXISTS {} ({} TEXT, {} TEXT, {} TEXT);'.format(TABLE, COL1, COL2, COL3))
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(file, 'r+') as fin:
        dict_reader = csv.DictReader(fin)
        loaded_dict = [(i[COL1], i[COL2], i[COL3]) for i in dict_reader]
    
    cursor.executemany('INSERT INTO {} ({}, {}, {}) VALUES (?, ?, ?);'.format(TABLE, COL1, COL2, COL3),
                       loaded_dict)
    conn.commit()


    
def upload_to_db(filename, author):
    game_table_name = filename.split('.')[0]
    game_table = Gametable.query.filter_by(author=author, table=game_table_name).first()
    if not game_table:
        game_table = Gametable(game_table_name, author)
    # Remove all existing data to avoid dealing with upserts
    game_data = Gamedata.query(table_pk=game_table.pk).delete()
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(file, 'r+') as fin:
        dict_reader = csv.DictReader(fin)
        for i in dict_reader:
            new_entry = Gamedata(i[COL1], i[COL2], i[COL3])
            db.session.add(new_entry)

    db.session.commit()
