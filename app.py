from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello from Flask!',
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    name = data.get('name', 'Anonymous')
    return jsonify({
        'message': f'Hello {name}! You sent: {data}',
        'received_at': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)