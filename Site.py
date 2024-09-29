from flask import Flask, render_template

app = Flask(__name__)
# Primeira pagina:
# route -> metatimvinicios.com/
#função -> oque exibir

@app.route("/")
def homepag():
    return render_template("Homepag.html")

@app.route("/meta")
def metas():
    return render_template("Meta.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("Usuarios.html", nome_usuario=nome_usuario)

# Colocar site no ar:
if __name__ == "__main__":
    app.run(debug=True)

    #servidor do heroku