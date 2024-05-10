from flask import Flask


app= Flask(__name__)

@app.route('/')

def index():
    return "Plantilla de jugadores temporada 2024-2"

if __name__ == '__main__':
    app.run()