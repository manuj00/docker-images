from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 * num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
