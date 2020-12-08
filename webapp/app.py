#!/usr/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)

# HOME LOGIN PAGE
@app.route('/')
def home_page():

    return render_template('index.html')

def run_app():
    app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
    run_app()
