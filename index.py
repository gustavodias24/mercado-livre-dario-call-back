from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    code = request.args.get('code')
    url = 'https://api.mercadolibre.com/oauth/token'

    payload = {
        'grant_type': 'authorization_code',
        'client_id': '200629904312027',
        'client_secret': 'EbCGNmbnX74KGjkaqe8FS4cv4npZqMDt',
        'code': code,
        'redirect_uri': 'https://mercado-livre-dario-call-back.vercel.app/',
    }

    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers).json()

    return jsonify(response)


if __name__ == "__main__":
    app.run()
