# __Author__ __Lencof__
# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Lencof'

app.run(host='0.0.0.0', port=81)
