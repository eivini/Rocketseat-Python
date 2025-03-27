from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)     # Método usado só para teste de projetos, não é algo feito para o servidor/cliente, apenas desenvolvimento local

# Obs: 127.0.0.1 - - [12/Mar/2025 20:16:19] "GET /about HTTP/1.1" 200 -
# é uma requisição, o 200 significa que deu certo