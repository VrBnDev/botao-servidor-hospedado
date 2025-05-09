from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

# Vercel vai usar a variável "app" como ponto de entrada
