from flask import Flask, request, jsonify, json
from repository.db import session, conection
from repository.models import Student

app = Flask(__name__)

ses = session()

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/ping')
def main():
    return jsonify({"Message": "Pong"})


@app.route('/v1/estudiantes', methods=["POST"])
def estudiantes():
    """ request_data = request.get_json()
    name = request_data['name'] """
    request_data = json.loads(request.data)
    name = request_data['name']
    if validateStudent(name):
        with conection.connect() as con:
            new_user = Student(username=name)
            ses.add(new_user)
            try:
                ses.commit()
            except:
                return jsonify({"Message": "error"})
            
        succes = f'User {name} created'
        return jsonify({f"Message": succes})


def validateStudent(name):
    return len(name) != 0 and len(name) < 200

