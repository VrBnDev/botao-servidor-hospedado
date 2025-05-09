from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

# Configura o SocketIO para permitir conexões de qualquer origem
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

