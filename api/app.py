from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/ping')
def main():
    return jsonify({"Message": "Pong"})


@app.route('/v1/estudiantes', methods=("GET", "POST"))
def estudiantes():
    if request.method == 'POST':
        """ request_data = request.get_json()
        name = request_data['name']
        error = estudiantes.addEstudiante(name) """
    return jsonify({"Message": "Api funciona"})
