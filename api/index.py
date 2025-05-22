from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
estado_botao = "unpressed"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify({"action": estado_botao, "message": "Vinda do status"})
