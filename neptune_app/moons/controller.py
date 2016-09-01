from flask import Blueprint

moons = Blueprint('moons', __name__, template_folder = 'templates')

@moons.route('/<moon_id>')
def show_moon(moon_id):
	return ("Moon is: "+ moon_id)