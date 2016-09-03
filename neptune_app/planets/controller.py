from flask import Blueprint, render_template, jsonify
from neptune_app.planets.model import Planets

planets = Blueprint('planets', __name__, template_folder = 'templates')

@planets.route('/<planet_id>')
def show_planet_page(planet_id):
	return render_template('base.html')

@planets.route('/api/<planet_id>')
def show_planet_data(planet_id):
	planet = Planets.objects(planet_id = planet_id).first()
	return jsonify(planet.repr)