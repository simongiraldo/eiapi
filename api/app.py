from flask import Flask, request, jsonify
from repository.estudiantes import estudiantes

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/ping')
def main():
    return jsonify({"Message": "Pong"})


@app.route('/v1/estudiantes')
def estudiantes():
    return jsonify({"Message": "Api funciona"})
