import requests
from flask import Flask, jsonify
from flask_cors import CORS
from urllib.parse import quote

app = Flask(__name__)
CORS(app)

@app.route('/')
def lmafo():
    return '''
    <body>
        <p>hosted by @cooking.faded</h1>
        <p>to keep hosting going, donate to:</p>
        <p><strong>LQ4j1Aeah5sz8nFeFDYaUTEXRuKZTHkK5J</strong></p>
        <p>you big black nice guy</p>
        <p>https://weao.xyz</p>
    </body>
    '''
@app.route('/docs')
def docs():
    return '''
    <body>
        <p>redirecting to weao in 5 seconds..</p>
        <script>
            setTimeout(function() { window.location.href = "https://docs.weao.xyz"; }, 5000);
        </script>
    </body>
    '''

@app.route('/api/status/exploits')
def getallexploits():
    try:
        response = requests.get('https://weao.xyz/api/status/exploits', headers={
            'User-Agent': 'WEAO-3PService',
            'Accept': 'application/json'
        })        
        if not response.ok:
            return jsonify({'error': f'http nigger, status: {response.status_code}'}), response.status_code
        return jsonify(response.json())
    except Exception as error:
        return jsonify({'error': str(error) or 'error getting data'}), 500

@app.route('/api/status/exploits/<exploit>')
def getexploitstatus(exploit):
    try:
        response = requests.get(f'https://weao.xyz/api/status/exploits/{quote(exploit)}', headers={
            'User-Agent': 'WEAO-3PService',
            'Accept': 'application/json'
        })
        
        if not response.ok:
            return jsonify({'error': f'http nigger, status: {response.status_code}'}), response.status_code
        
        return jsonify(response.json())
    except Exception as error:
        return jsonify({'error': str(error) or 'error getting data'}), 500

@app.route('/api/versions/current')
def getcurrentversion():
    try:
        response = requests.get('https://weao.xyz/api/versions/current', headers={
            'User-Agent': 'WEAO-3PService',
            'Accept': 'application/json'
        })        
        if not response.ok:
            return jsonify({'error': f'http nigger, status: {response.status_code}'}), response.status_code
        return jsonify(response.json())
    except Exception as error:
        return jsonify({'error': str(error) or 'error getting data'}), 500
    
@app.route('/api/versions/future')
def getfutureversion():
    try:
        response = requests.get('https://weao.xyz/api/versions/future', headers={
            'User-Agent': 'WEAO-3PService',
            'Accept': 'application/json'
        })        
        if not response.ok:
            return jsonify({'error': f'http nigger, status: {response.status_code}'}), response.status_code
        return jsonify(response.json())
    except Exception as error:
        return jsonify({'error': str(error) or 'error getting data'}), 500    

@app.errorhandler(429)
def ratelimithandler(e):
    return jsonify({'error': 'too many gooning snicker'}), 429

app.run(debug=True, host='0.0.0.0', port=6767)
