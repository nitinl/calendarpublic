from flask import Flask, jsonify, render_template
from flask_cors import CORS
import sqlite3
#this connects to Front End

app=Flask(__name__,
                   static_folder='./frontend/dist/static',
                   template_folder='./frontend/dist')


cors = CORS(app, resources= {r"/day/*":
{"origins": "*"}})

@app.route('/days')
def mensaje():
   conn = sqlite3.connect('contentmodal.db')
   cur = conn.cursor()
   cur.execute('PRAGMA foreign_keys=on;') ## Enables the foreign key support in Sqlite
   cur.execute('SELECT * FROM modal')
   days = cur.fetchall()
   return jsonify(days)

@app.route('/day/<day>')
def get_day(day):
   conn = sqlite3.connect('contentmodal.db')
   cur = conn.cursor()
   cur.execute('PRAGMA foreign_keys=on;') ## Enables the foreign key support in Sqlite
   cur.execute('SELECT * FROM modal WHERE id_dia = ?', [day])
   days = cur.fetchall()
   return jsonify(days)

@app.route('/', defaults={'path': ''})


@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug = True)
  


