from flask import Flask

app = Flask(__name__)

# config set up
app.config.from_object('config')

# import views
from app.views import main

# register blueprints
app.register_blueprint(main.mod)

# import helper utilities
from app import helpers
