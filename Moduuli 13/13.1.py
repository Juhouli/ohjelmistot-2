from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = int(luku)
        if (2 ** luku - 2) % luku == 0:
            alkuluku = f"{luku} on alkuluku."
        else:
            alkuluku = f"{luku} ei ole alkuluku."

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku": luku,
            "alkuluku": alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku"
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