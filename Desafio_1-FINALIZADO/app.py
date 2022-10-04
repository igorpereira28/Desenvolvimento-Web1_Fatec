# flask -> framework de desenvolvimento de sites e de apis do python

#renfer_template -> ao invés de xbiri um texto, carregue uma página! ex:
#ao invés disso
    #def homepage(): 
        #return "Este é o meu terceiro site!"

#coloco isso:
    #def homepage(): 
        #return render_template("homepage.html")

from flask import Flask, render_template, url_for


#documentação do flask diz +/- que sempre que for iniciar seu site, utilize:

app = Flask(__name__)


#criar a primeira página do site


#toda página têm

#route -> caminho que vêm depois do seu domínio

#função -> o que você quer exibir naquela página

#template


#app por cause de app = Flask(__name__)

#definir route

@app.route("/")


#definindo função

def homepage(): 

    return render_template("index.html")


#criar página de contatos

@app.route("/contato")


def contato():
    return render_template("contato.html")

    

@app.route("/quemsomos")


def quemsomos():
    return render_template("quemsomos.html")


#colocar o site no ar

# app.run()

#dando debug no site, rodar automático

if __name__ == "__main__":

    app.run(debug=True)