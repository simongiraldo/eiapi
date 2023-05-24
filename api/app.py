from flask import Flask, request, jsonify, json
from repository.db import session, conection
from repository.models import Student, Curso

app = Flask(__name__)

ses = session()

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/ping')
def main():
    return jsonify({"Message": "Pong"})


@app.route('/v1/estudiantes', methods=["POST", "GET"])
def estudiantes():
    if request.method == 'POST':
        request_data = json.loads(request.data)
        user_name = request_data['username']
        nombre = request_data['nombre']
        edad = int(request_data['edad'])
        pregrado = request_data['pregrado']
        semestre_actual  = int(request_data['semestre_actual'])
        transporte = request_data['transporte']
        if validateStudent(user_name, nombre, edad, pregrado, semestre_actual, transporte):
            with conection.connect() as con:
                new_student = Student(username=user_name, nombre=nombre, edad=edad, pregrado=pregrado,  semestre_actual=semestre_actual)
                ses.add(new_student)
                try:
                    ses.commit()
                except:
                    return jsonify({"Message": "error, wrong fields"})
            
            succes = f'User {user_name} created'
            return jsonify({f"Message": succes})
        return jsonify({"Message": "error, wrong fields"})
    
    estudiantes = ses.query(Student).all()
    lista_students = []
    for c in estudiantes:
        lista_students.append({
            'id': c.id,
            'username': c.username,
            'name': c.nombre,
            'edad': c.edad,
            'pregrado': c.pregrado,
            'semestre_actual': c.semestre_actual,
            'tranporte': c.tranporte
        })

    return jsonify({f"Message": "succes"},{f"data":lista_students})

@app.route('/cursos', methods=["POST", "GET"])
def cursos():
    if request.method == 'POST':
        request_data = json.loads(request.data)
        name = request_data['name']
        description = request_data['description']
        creditos = int(request_data['creditos'])
        semestre = int(request_data['semestre'])
        if validateCurso(name, description, creditos, semestre):
            with conection.connect() as con:
                new_curso = Curso(name=name, description=description, creditos=creditos, semestre=semestre)
                ses.add(new_curso)
                try:
                    ses.commit()
                except:
                    return jsonify({"Message": "error, wrong fields"})
            
            succes = f'Curso {name} created'
            return jsonify({f"Message": succes},{f"data":{
                "name": name,
                "description": description,
                "creditos": creditos,
                "semestre": semestre,
            }})
        return jsonify({"Message": "error, wrong fields"})
    
    cursos = ses.query(Curso).all()
    lista_cursos = []
    for c in cursos:
        lista_cursos.append({
            'id': c.id,
            'name': c.name,
            'description': c.description,
            'creditos': c.creditos,
            'semestre': c.semestre
        })

    return jsonify({f"Message": "succes"},{f"data":lista_cursos})
   

def validateStudent(user_name, name, edad, pregrado, semestre_actual, transporte):
     return len(name) != 0 and len(name) < 200 and len(user_name) != 0 and len(user_name) < 200 and len(pregrado) != 0 and len(pregrado) < 100 and isinstance(edad, int) and isinstance(semestre_actual, int) and len(transporte) != 0 and len(transporte) < 100
       
def validateCurso(name, description, creditos, semestre):
    return len(name) != 0 and len(name) < 200 and len(description) != 0 and len(description) < 200 and isinstance(creditos, int) and isinstance(semestre, int)
