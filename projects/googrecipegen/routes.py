import time
from flask import render_template, request, jsonify, session, url_for, current_app
from projects.googrecipegen.lib.googgen import recipeWriter
from . import bp
import os
writer = recipeWriter()

@bp.route('/', methods=['GET'])
def index():
    # build the full URL to the generate endpoint
    generate_url = url_for('googrecipegen.generate', _external=True)
    return render_template('qook.html', path=generate_url)

@bp.route('/generate', methods=['POST'])
def generate():
    print("Data received!")
    start = time.time()

    data = request.get_json()
    input_text = data.get('inputText')
    session['inputText'] = input_text

    output_text = writer.generate(input_text)
    session['outputText'] = output_text

    print(f"Processed in {time.time() - start:.2f}s")
    return jsonify({'outputText': output_text})