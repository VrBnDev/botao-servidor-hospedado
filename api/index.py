from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
estado_botao = "global"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pressed', methods=['GET','POST'])
def pressed():
    global estado_botao
    estado_botao = "pressed"
    return jsonify({"action": estado_botao, "message": "Estado atualizado para pressionado"})

@app.route('/unpressed', methods=['GET','POST'])
def unpressed():
    global estado_botao
    estado_botao = "unpressed"
    return jsonify({"action": estado_botao, "message": "Estado atualizado para solto"})

@app.route('/status')
def status():
    return jsonify({"action": estado_botao})
