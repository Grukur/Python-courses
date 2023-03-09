from flask import Flask
from clase_5.my_price_app.blueprint.learning import learning_blueprint


app = Flask(__name__)

app.register_blueprint(learning_blueprint, url_prefix='/greetings')

if __name__ == '__main__':
    app.run()