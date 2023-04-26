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
    request_data = json.loads(request.data)
    user_name = request_data['username']
    nombre = request_data['nombre']
    edad = int(request_data['edad'])
    pregrado = request_data['pregrado']
    semestre_actual  = int(request_data['semestre_actual'])
    transporte = request_data['transporte']
    if validateStudent(user_name, nombre, edad, pregrado, semestre_actual, transporte):
        with conection.connect() as con:
            new_student = Student(username=user_name, nombre=nombre, edad=edad, pregrado=pregrado, semestre_actual=semestre_actual)
            ses.add(new_student)
            try:
                ses.commit()
            except:
                return jsonify({"Message": "error, wrong fields"})
            
        succes = f'User {user_name} created'
        return jsonify({f"Message": succes})
    return jsonify({"Message": "error, wrong fields"})

def validateStudent(user_name, name, edad, pregrado, semestre_actual, transporte):
     return len(name) != 0 and len(name) < 200 and len(user_name) != 0 and len(user_name) < 200 and len(pregrado) != 0 and len(pregrado) < 100 and isinstance(edad, int) and isinstance(semestre_actual, int) and len(transporte) != 0 and len(transporte) < 100
       

