# flask -> framework de desenvolvimento de sites e de apis do python

from flask import Flask, render_template, url_for, request
import mariadb

app = Flask(__name__)


#definir route

try:
    connection = mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database = "contatos"
    )
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")

@app.route("/")
#definindo função
def homepage(): 
    return render_template("index.html")


#criar página de contatos
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (?, ?, ?)", (email, assunto, descricao))
        connection.commit()
        return render_template('contato.html')
    return render_template('contato.html')
    

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route('/usuarios')
def usuarios():
    cursor = connection.cursor()
    usuarios = cursor.execute("SELECT * FROM contatos")
    if usuarios !='':
        userDetails = cursor.fetchall()

        return render_template("usuarios.html", userDetails=userDetails)
    return render_template("usuarios.html")


if __name__ == "__main__":

    app.run(debug=True)