import os
import psycopg2
import random
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

#app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')

def get_db_connection():
    connection = psycopg2.connect(host=os.environ['DB_HOST'], database=os.environ['DB_NAME'], user=os.environ['DB_USER'],
                                password=os.environ['DB_PASSWORD'])

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
        try:
            nahodny_2_soubor = soubory_v_jedne_polozce.pop()
        except:
            print(polozka + " je chybná")
        try:
            nahodny_3_soubor = soubory_v_jedne_polozce.pop()
        except:
            print(polozka + " je chybná")
        cesta_1 = polozka + "/" + nahodny_1_soubor
        cesta_2 = polozka + "/" + nahodny_2_soubor
        cesta_3 = polozka + "/" + nahodny_3_soubor
        pole_cest_jedne_rostliny = [cesta_1, cesta_2, cesta_3]
        array_of_all_pahts.append(pole_cest_jedne_rostliny)
    cursor.close()
    connection.close()
    return render_template('macro-gnosy.html', vyber=vyber, paths=array_of_all_pahts)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)


