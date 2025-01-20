from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Backend URL (use the service name in Docker Compose)
BACKEND_URL = 'http://backend:5001/multiply'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        try:
            response = requests.post(BACKEND_URL, json={'num1': int(num1), 'num2': int(num2)})
            result = response.json().get('result')
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
