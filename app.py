import os
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boton1')
def boton1():
    return render_template('boton1.html')

@app.route('/boton2')
def boton2():
    return render_template('boton2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))