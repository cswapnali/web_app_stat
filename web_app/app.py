from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

ISRO_API_ENDPOINT = "https://services.isrostats.in/api/launches"

def fetch_isro_data():
    response = requests.get(ISRO_API_ENDPOINT)
    data = response.json()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    isro_data = fetch_isro_data()
    return jsonify(isro_data)

if __name__ == '__main__':
    app.run(debug=True)
