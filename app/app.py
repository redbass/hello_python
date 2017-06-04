from flask import Flask


def run_app():

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    app.run()

if __name__ == "__main__":
    run_app()
