import sqlite3
import os
import csv
from matcherAdmin import app

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