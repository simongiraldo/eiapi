from flask import Flask, request, make_response, redirect, render_template
from repository.db import session, conection
from repository.models import User

app = Flask(__name__, template_folder='../templates/', static_folder='../static/')

ses = session()
""" ejemplo """

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/')
def main():
    response = make_response(redirect('/login'))
    return response


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username, dominio = email.split("@")
        if(valdateSignUp(username, dominio, password)):
            with conection.connect() as con:
                new_user = User(email=email, password=password, username=username)
                ses.add(new_user)
                try:
                    ses.commit()
                except:
                    return render_template('index.html', error=True, signup=True)
            return make_response(redirect('/login'))
        return render_template('index.html', error=True, signup=True) 
    return render_template('index.html', error=False, signup=True)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if validateLogin(user, password):
            return make_response(redirect('/documentation'))
        return render_template('index.html', error=True, signup=False)
    return render_template('index.html', error=False, signup=False)


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')


def validateLogin(u, p):
    return ses.query(User).filter_by(username=u, password=p).first() is not None

def valdateSignUp(username, dominio, password):
    return dominio == "eia.edu.co" and len(username) < 246 and len(password) < 100