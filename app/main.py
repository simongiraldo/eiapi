from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__, template_folder='../templates/', static_folder='../static/')

@app.route('/')
def main():
    response = make_response(redirect('/login'))
    return response

@app.route('/login')
def login():
    return render_template('documentation.html')