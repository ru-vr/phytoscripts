import os
import psycopg2
import random
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from urllib.parse import unquote

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

@app.route('/alkaloid/<alk>', methods=['GET', 'POST'])
def alkaloid(alk):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM alkaloidy WHERE nazev = %s', (alk, ))  # vybere jen jeden radek
    alkaloid = cursor.fetchall()  # a vsechna data v nem
    cursor.close()
    connection.close()
    return render_template('alkaloid.html', alkaloid=alkaloid)

@app.route('/alkaloid/', methods=['GET', 'POST'])
def find_alkaloid():
    if request.method == 'POST':
        hledany_alk = request.form['hledej_alk']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM alkaloidy WHERE nazev = %s', (hledany_alk,))  # vybere jen jeden radek
        alkaloid = cursor.fetchall()  # a vsechna data v nem
        cursor.close()
        connection.close()
        return render_template('alkaloid.html', alkaloid=alkaloid, hledany_alk=hledany_alk)

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
    vyber = cursor.fetchall()
    list_nazvu = [item[1] for item in vyber]
    list_nazvu = [s.replace("\xa0", "") for s in list_nazvu]
    list_cest = ["static/images/botanika/"+nazev for nazev in list_nazvu]
    array_of_all_pahts = []  # je to pole polí
    for polozka in list_cest:  # poloza je "static/images/botniky/Rod druh"
        soubory_v_jedne_polozce = os.listdir(polozka)
        random.shuffle(soubory_v_jedne_polozce) # nahodné promíchání obrazků
        nahodny_1_soubor = soubory_v_jedne_polozce.pop()
        nahodny_2_soubor = soubory_v_jedne_polozce.pop()
        nahodny_3_soubor = soubory_v_jedne_polozce.pop()
        cesta_1 = polozka + "/" + nahodny_1_soubor
        cesta_2 = polozka + "/" + nahodny_2_soubor
        cesta_3 = polozka + "/" + nahodny_3_soubor
        pole_cest_jedne_rostliny = [cesta_1, cesta_2, cesta_3]
        array_of_all_pahts.append(pole_cest_jedne_rostliny)
    cursor.close()
    connection.close()
    return render_template('poznavacka-botanika.html', vyber=vyber, paths=array_of_all_pahts)

@app.route('/recognition-botany', methods=['GET', 'POST'])
def recognition_botany():
   # if request.method == 'POST':
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM poznavacka_botanika ORDER BY random() LIMIT 15')
    vyber = cursor.fetchall()
    list_nazvu = [item[1] for item in vyber]
    list_nazvu = [s.replace("\xa0", "") for s in list_nazvu]
    list_cest = ["static/images/botanika/"+nazev for nazev in list_nazvu]
    array_of_all_pahts = []  # je to pole polí
    for polozka in list_cest:  # poloza je "static/images/botniky/Rod druh"
        soubory_v_jedne_polozce = os.listdir(polozka)
        random.shuffle(soubory_v_jedne_polozce) # nahodné promíchání obrazků
        nahodny_1_soubor = soubory_v_jedne_polozce.pop()
        nahodny_2_soubor = soubory_v_jedne_polozce.pop()
        nahodny_3_soubor = soubory_v_jedne_polozce.pop()
        cesta_1 = polozka + "/" + nahodny_1_soubor
        cesta_2 = polozka + "/" + nahodny_2_soubor
        cesta_3 = polozka + "/" + nahodny_3_soubor
        pole_cest_jedne_rostliny = [cesta_1, cesta_2, cesta_3]
        array_of_all_pahts.append(pole_cest_jedne_rostliny)
    cursor.close()
    connection.close()
    return render_template('recognition-botany.html', vyber=vyber, paths=array_of_all_pahts)

@app.route('/makro-gnozka', methods=['GET', 'POST'])
def makro_gnozka():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM makro_gnozka ORDER BY random() LIMIT 10')
    vyber = cursor.fetchall()
    list_nazvu = [item[1].strip() for item in vyber]
    list_nazvu = [s.replace("\xa0", "") for s in list_nazvu]
    list_cest = ["static/images/gnozka_makro/"+nazev for nazev in list_nazvu]
    array_of_all_pahts = []  # je to pole polí
    for polozka in list_cest:  # poloza je "static/images/botniky/Rod druh"
        soubory_v_jedne_polozce = os.listdir(polozka)
        random.shuffle(soubory_v_jedne_polozce) # nahodné promíchání obrazků
        nahodny_1_soubor = soubory_v_jedne_polozce.pop()
        nahodny_2_soubor = soubory_v_jedne_polozce.pop()
        nahodny_3_soubor = soubory_v_jedne_polozce.pop()
        cesta_1 = polozka + "/" + nahodny_1_soubor
        cesta_2 = polozka + "/" + nahodny_2_soubor
        cesta_3 = polozka + "/" + nahodny_3_soubor
        pole_cest_jedne_rostliny = [cesta_1, cesta_2, cesta_3]
        array_of_all_pahts.append(pole_cest_jedne_rostliny)
    cursor.close()
    connection.close()
    return render_template('makro-gnozka.html', vyber=vyber, paths=array_of_all_pahts)

@app.route('/macro-gnosy', methods=['GET', 'POST'])
def macro_gnosy():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM makro_gnozka ORDER BY random() LIMIT 10')
    vyber = cursor.fetchall()
    list_nazvu = [item[1].strip() for item in vyber]
    list_nazvu = [s.replace("\xa0", "") for s in list_nazvu]
    list_cest = ["static/images/gnozka_makro/"+nazev for nazev in list_nazvu]
    array_of_all_pahts = []  # je to pole polí
    for polozka in list_cest:  # poloza je "static/images/botniky/Rod druh"
        soubory_v_jedne_polozce = os.listdir(polozka)
        random.shuffle(soubory_v_jedne_polozce) # nahodné promíchání obrazků
        nahodny_1_soubor = soubory_v_jedne_polozce.pop()
        nahodny_2_soubor = soubory_v_jedne_polozce.pop()
        nahodny_3_soubor = soubory_v_jedne_polozce.pop()
        cesta_1 = polozka + "/" + nahodny_1_soubor
        cesta_2 = polozka + "/" + nahodny_2_soubor
        cesta_3 = polozka + "/" + nahodny_3_soubor
        pole_cest_jedne_rostliny = [cesta_1, cesta_2, cesta_3]
        array_of_all_pahts.append(pole_cest_jedne_rostliny)
    cursor.close()
    connection.close()
    return render_template('macro-gnosy.html', vyber=vyber, paths=array_of_all_pahts)

@app.route('/foto-botanika')
def foto_botanika():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT druh_latinsky FROM poznavacka_botanika')
    seznam_nazvu = cursor.fetchall()
    cursor.close()
    connection.close()
    seznam_nazvu = [item[0].strip() for item in seznam_nazvu]
    seznam_nazvu= sorted([s.replace("\xa0", "") for s in seznam_nazvu])
    return render_template('foto-botanika.html', seznam_nazvu=seznam_nazvu)

@app.route('/rostlina/<konkretni>')
def nazev(konkretni):
    konkretni = unquote(konkretni)
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM poznavacka_botanika WHERE druh_latinsky = %s', (konkretni, ))
    rostlina = cursor.fetchall()  # a vsechna data v nem
    cursor.close()
    connection.close()
    return render_template('foto-rostlina.html', rostlina=rostlina)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)


