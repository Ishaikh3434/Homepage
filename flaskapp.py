# flaskapp.py
import os
import importlib
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

def create_app():
    app = Flask(__name__)
    app.secret_key=os.environ["SESSION_KEY"]
    # Define the home route
    @app.route('/')
    def home():
        return render_template('index.html')

    # Iteratively grab each project from /projects
    projects_dir = os.path.join(app.root_path, 'projects')
    for name in os.listdir(projects_dir):
        pkg_path = os.path.join(projects_dir, name)
        # only directories with an __init__.py
        if os.path.isdir(pkg_path) and os.path.isfile(os.path.join(pkg_path, '__init__.py')):
            # import projects.<name>
            module = importlib.import_module(f'projects.{name}')
            # MAKE SURE EACH PACKAGE EXPOSES A 'bp' BLUEPRINT !!!!! 
            bp = getattr(module, 'bp', None)
            if bp:
                # mount it at /<name>
                app.register_blueprint(bp, url_prefix=f'/{name}')
                print(f'🔌 Registered blueprint: {name} @ /{name}')
            else:
                print(f'⚠️  projects.{name} has no "bp" attribute, skipping')

    return app

if __name__ == '__main__':
    create_app().run(debug=True)