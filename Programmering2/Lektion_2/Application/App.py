from flask import Flask

app = Flask(__name__)


@app.route("/")
def flask_test():
    html = """
    <html>
        <head>
            <title>Simple flask website</title>
        </head>
        <body>
            <h1 style="color: DarkBlue;">Simple flask webiste</h1>
            <h2 style="color: Blue;">Simple flask webiste</h2>
            <h3 style="color: LightBlue;">Simple flask webiste</h3>
            <img src="./static/cover-flask.jpg" alt="image" width="200" height="200" />
            <p>This is a simple HTML flask website</p>
            <h2>Unordered List</h2>
            <ul>
                <li>Simple</li>
                <li>Flask</li>
                <li>Website</li>
            </ul>
            <h2>Ordered List</h2>
            <ol>
                <li>Simple</li>
                <li>Flask</li>
                <li>Website</li>
            </ol>
            <button>Press me</button>
        </body>
    </html>
"""
    return html
def main():
    flask_test()

if __name__ == "__main__":
    app.run(debug=True)
