from neptune_app import create_app, app
from flask_script import Manager

manager = Manager(app)

@manager.command
def runserver():
	create_app()
	app.run(host     = app.config['SERVE_HOST'],
                port     = app.config['SERVE_PORT'],
                threaded = app.config['THREADED'])

if __name__ == "__main__":
    manager.run()