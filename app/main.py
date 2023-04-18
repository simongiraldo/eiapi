from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__, template_folder='../templates/', static_folder='../static/')

@app.route('/')
def main():
    response = make_response(redirect('/login'))
    return response

@app.route('/login', methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        autenthicated = True
        if autenthicated:
            return make_response(redirect('/documentation'))
    return render_template('index.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')