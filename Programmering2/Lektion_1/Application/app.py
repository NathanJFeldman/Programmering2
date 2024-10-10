from flask import Flask

app = Flask(__name__)

@app.route("/")
def flask_test():
    return "<h>HELLO FLASK</h>"

def main():
    flask_test()

if __name__ == "__main__":
    app.run(debug=True)
