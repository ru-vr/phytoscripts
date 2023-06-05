import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

#app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')

def get_db_connection():
    #connection = psycopg2.connect(host=os.environ['DB_HOST'], database=os.environ['DB_NAME'], user=os.environ['DB_USER'],
      #                           password=os.environ['DB_PASSWORD'])
    connection = psycopg2.connect(host='localhost', database='diplomky', user='postgres',
                                     password='loooll')
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rudolf-vrabec')
def index_rv():
    return render_template('cv.html')

@app.route('/rudolf-vrabec-cz')
def index_rv_cz():
    return render_template('cv_cz.html')

@app.route('/diplomky')
def diplomky():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM seznam_diplomek;')  # vybere tabulku
    seznam_diplomek = cursor.fetchall()  # a vsechna data
    cursor.close()
    connection.close()
    return render_template('diplomky.html', seznam_diplomek=seznam_diplomek)

@app.route('/<alk>')
def alkaloid(alk):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM alkaloidy WHERE nazev = %s', (alk, ))  # vybere jen jeden radek
    alkaloid = cursor.fetchall()  # a vsechna data v nem
    cursor.close()
    connection.close()
    return render_template('alkaloid.html', alkaloid=alkaloid)

@app.route('/alkaloidy')
def alkaloidy():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM alkaloidy')  # vybere vše
    alkaloidy = cursor.fetchall()  # a vsechna data v nem ??
    cursor.close()
    connection.close()
    return render_template('alkaloidy.html', alkaloidy=alkaloidy)

@app.route('/kfgfb')
def kfgfb():
    return render_template('kfgfb.html')

@app.route('/otacivost')
def otacivost():
    return render_template('otacivost.html')

@app.route('/poznavacka-botanika', methods=['GET', 'POST'])
def poznavacka_botanika():
   # if request.method == 'POST':
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM poznavacka_botanika ORDER BY random() LIMIT 15')
    vyber = cursor.fetchall()  #
    cursor.close()
    connection.close()
    return render_template('poznavacka-botanika.html', vyber=vyber)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)


