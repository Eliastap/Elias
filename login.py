from flask import Flask
from flask import render_template
from flask import request
import csv
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

with open('nom-email-ASIX2-2324.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    email_dict = {row['NOM']: row['EMAIL'] for row in csv_reader}

@app.route('/success/<name>')
def dashboard(name):
    email = email_dict.get(name, 'no hay ningun correo encontrado')
    return f"Hola {name}, tu email es el siguiente: {email}"

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

@app.route('/addmail', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_name = request.form['new_name']
        new_email = request.form['new_email']

        # Agrega el nuevo nombre y correo al diccionario y guarda en el archivo CSV
        email_dict[new_name] = new_email
        with open('nom-email-ASIX2-2324.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([new_name, new_email])

        return redirect(url_for('dashboard', name=new_name))
    else:
        return render_template('newcorreo.html')

if __name__ == '__main__':
   app.run(debug = True)