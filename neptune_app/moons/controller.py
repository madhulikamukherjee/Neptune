from flask import Blueprint, render_template, jsonify
from neptune_app.moons.model import Moons

moons = Blueprint('moons', __name__, template_folder = 'templates')

@moons.route('/<moon_id>')
def show_moon_page(moon_id):
	return render_template('base.html')

@moons.route('/api/<moon_id>')
def show_moon_data(moon_id):
	moon = Moons.objects(moon_id = moon_id).first()
	return jsonify(moon.repr)