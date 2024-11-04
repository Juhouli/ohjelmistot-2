import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Kahvia666',
         autocommit=True
         )

maa = input("Anna maakoodi: ")
sql = f"SELECT type, count(*) FROM airport WHERE iso_country = '{maa}' GROUP BY type"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}: {rivi[1]}")