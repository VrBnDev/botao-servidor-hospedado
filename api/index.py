from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html') 

# Rota para comando "pressed"
@app.route('/status', methods=['GET', 'POST'])
def botao():
    return jsonify({"action":"pressed"})
