from flask import Flask, request, jsonify
from repository.db import session, conection
from repository.models import Student

app = Flask(__name__)

ses = session()

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/ping')
def main():
    return jsonify({"Message": "Pong"})


@app.route('/v1/estudiantes', methods=("POST"))
def estudiantes():
    request_data = request.get_json()
    name = request_data['name']
    if validateStudent(name):
        with conection.connect() as con:
            new_user = Student(username=name)
            ses.add(new_user)
            try:
                ses.commit()
            except:
                return jsonify({"Message": "error"})

        return jsonify({f"Message": "User '{name}' created"})


def validateStudent(name):
    return len(name) != 0 and len(name) < 200

