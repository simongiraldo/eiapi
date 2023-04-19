from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__, template_folder='../templates/', static_folder='../static/')

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/')
def main():
    response = make_response(redirect('/login'))
    return response


@app.route('/login', methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if validate(user, password):
            return make_response(redirect('/documentation'))
        return render_template('index.html', error=True)
    return render_template('index.html', error=False)


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')


def validate(u, p):
    return (u == "Usuario1" and p == "sistemaslomejor")
