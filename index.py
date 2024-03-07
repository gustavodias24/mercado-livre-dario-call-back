from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    json = request.json
    args = request.args

    json.update(args)

    return jsonify(json)


if __name__ == "__main__":
    app.run()
