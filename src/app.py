from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello,This is a classic CV Maker running to test whether everything works fine or not"

if __name__ == '__main__':
    app.run(debug=True)
