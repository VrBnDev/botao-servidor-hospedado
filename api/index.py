from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

# Rota para comando "pressed"
@app.route('/botao', methods=['GET', 'POST'])
def botao():
    status = request.args.get('status', 'undefined')
    print(f"Comando: {status}")  # Imprime no console (útil para debug)
    return f"Botão está ", 200  # Retorna uma resposta HTTP padrão

