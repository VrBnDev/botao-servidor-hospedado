from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder="templates")

# Configura o SocketIO para permitir conexões de qualquer origem
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return render_template('index.html')

# Rota para comando "pressed"
@app.route('/pressed', methods=['GET', 'POST'])
def pressed():
    print("Comando: pressed")  # Imprime no console (útil para debug)
    socketio.emit('command', {'action': 'pressed'})  # Envia comando via WebSocket
    return 'Pressed command sent', 200  # Retorna uma resposta HTTP padrão

# Rota para comando "unpressed"
@app.route('/unpressed', methods=['GET', 'POST'])
def unpressed():
    print("Comando: Unpressed")  # Imprime no console (útil para debug)
    socketio.emit('command', {'action': 'unpressed'})  # Envia comando via WebSocket
    return 'Unpressed command sent', 200  # Retorna uma resposta HTTP padrão

# Vercel vai usar a variável "app" como ponto de entrada
