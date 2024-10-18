from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)

# Configuración secreta para las sesiones
app.secret_key = 'es_una_clave_secreta'  

# Diccionario de usuarios (en una aplicación real, usarías una base de datos)
users = {'Ana': '123',  'Belen': '456', 'Juan': '789'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return render_template('error.html')    
    else:
        return render_template('login.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template("inicio.html", username = username)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug = True)