from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "All the best for your AI journey"

if __name__ == '__main__':
    app.run(debug=True)
