import mysql.connector
from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/kentta/<icao>')
def alkuluku(icao):
    try:
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='Kahvia666',
            autocommit=True
        )
        sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{icao}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        tilakoodi = 200
        vastaus = {
            "ICAO": tulos[0][0],
            "Name": tulos[0][1],
            "Municipality": tulos[0][2],
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöte"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)