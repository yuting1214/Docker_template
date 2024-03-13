from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(
        port=os.getenv("PORT", default=5000),
        debug=False,
    )