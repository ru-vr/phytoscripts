import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')

def get_db_connection():
    connection = psycopg2.connect(host=os.environ['DB_HOST'], database=os.environ['DB_NAME'], user=os.environ['DB_USER'],
                                 password=os.environ['DB_PASSWORD'])
    # connection = psycopg2.connect(host='localhost', database='diplomky', user='postgres',
    #                                 password='loooll')
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

@app.route('/metoplants')
def metoplants():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM seznam_diplomek;')  # vybere tabulku
    seznam_diplomek = cursor.fetchall()  # a vsechna data
    cursor.close()
    connection.close()
    return render_template('metoplants.html', seznam_diplomek=seznam_diplomek)

@app.route('/<alk>')
def alkaloid(alk):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM alkaloidy WHERE nazev = %s', (alk, ))  # vybere jen jeden radek??
    alkaloid = cursor.fetchall()  # a vsechna data v nem ??
    cursor.close()
    connection.close()
    return render_template('alkaloid.html', alkaloid=alkaloid)


if __name__ == '__main__':
    app.run(debug=True)


