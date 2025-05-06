from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, esta es una app segura con Flask!'

@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    nombre = request.args.get('nombre', 'Invitado')
    return render_template_string('<h1>Hola {{ nombre }}</h1>', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
