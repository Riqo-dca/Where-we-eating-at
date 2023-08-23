from flask import Flask, render_template, jsonify
from restaurant_api import get_random_restaurant

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_restaurant')
def get_random_restaurant_route():
    restaurant = get_random_restaurant('Nashville')
    return jsonify({'restaurant_name': restaurant})

if __name__ == '__main__':
    app.run(debug=True)
