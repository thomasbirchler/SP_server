from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/endpoint', methods=['POST'])
def process_data():
    data = request.json
    # Process the data here
    response_data = {'message': 'Data received and processed successfully'}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
