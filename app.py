import os
import uuid
import tempfile
import subprocess as sp
from werkzeug.utils import secure_filename
from flask import Flask, request, send_file, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return 'Welcome to chanmo/poppler'

@app.route("/pdftocairo", methods=['POST'])
def pdftocairo():
    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'file is required.'
        }

    file = request.files['file']
    infile = tempfile.NamedTemporaryFile()
    file.save(infile.name)
    outfile = str(uuid.uuid4())
    os.mkdir(f'./media/{outfile}')
    os.chdir(f'./media/{outfile}')
    sp.run(['pdftocairo', '-png', infile.name, 'output'], check=True)
    return {
        'images': [f'/media/{outfile}/{i}' for i in os.listdir('./')]
    }


@app.route("/pdftoppm", methods=['POST'])
def pdftoppm():
    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'file is required.'
        }

    file = request.files['file']
    infile = tempfile.NamedTemporaryFile()
    file.save(infile.name)
    outfile = str(uuid.uuid4())
    os.mkdir(f'./media/{outfile}')
    os.chdir(f'./media/{outfile}')
    sp.run(['pdftoppm', '-png', infile.name, 'output'], check=True)
    return {
        'images': [f'/media/{outfile}/{i}' for i in os.listdir('./')]
    }


@app.route("/pdftohtml", methods=['POST'])
def pdftohtml():
    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'file is required.'
        }

    file = request.files['file']
    infile = tempfile.NamedTemporaryFile()
    file.save(infile.name)

    output = sp.run(['pdftohtml', '-s', '-dataurls', '-noframes', '-stdout', infile.name], check=True, capture_output=True)
    return output.stdout

@app.route("/pdfinfo", methods=['POST'])
def pdfinfo():
    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'file is required.'
        }

    file = request.files['file']
    infile = tempfile.NamedTemporaryFile()
    file.save(infile.name)

    output = sp.run(['pdfinfo', infile.name], capture_output=True, check=True)
    return output.stdout

@app.route("/pdftotext", methods=['POST'])
def pdftotext():
    if 'file' not in request.files:
        return {
            'success': False,
            'message': 'file is required.'
        }

    file = request.files['file']
    infile = tempfile.NamedTemporaryFile()
    file.save(infile.name)

    output = sp.run(['pdftotext', infile.name, '-'], capture_output=True, check=True)
    return output.stdout



@app.route('/media/<path:name>')
def download_file(name):
    return send_from_directory('./media/', name)

