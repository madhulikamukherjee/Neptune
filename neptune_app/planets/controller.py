from flask import Blueprint

planets = Blueprint('planets', __name__, template_folder = 'templates')

@planets.route('/<planet_id>')
def show_planet(planet_id):
	return ("Planet is: "+ planet_id)