from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

@app.route("/")
def pagina_inicial():
    return "Hello World - Marcio Torquato"

if __name__ == '__main__':
    app.run()