from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MongoEngine(app)

def create_app():
	from .planets.controller import planets
	from .moons.controller import moons

	app.register_blueprint(planets, url_prefix = '/planets')
	app.register_blueprint(moons, url_prefix = '/moons')

	@app.route('/')
	def home():
		return "This is home"

if __name__ == '__main__':
	create_app()