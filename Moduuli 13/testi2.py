import mysql.connector
from flask import Flask, Response
import json
icao = "EFHK"
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Kahvia666',
         autocommit=True
         )
sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{icao}' GROUP BY type"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
tilakoodi = 200
vastaus = {
    "ICAO": tulos[0][0],
    "luku": tulos[0][1],
    "alkuluku": tulos[0][2],
}
print(vastaus)
