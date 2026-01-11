from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask App!</h1>"

@app.route('/about')
def about():
    return "<p>This is a simple Flask web application demonstrating multiple routes.</p>"

@app.route('/greet/<name>')
def greet(name):
    return f"<h2>Hello, {name.capitalize()}! Welcome to the Flask App.</h2>"

@app.route('/api/data')
def get_data():
    data = {
        "project": "Flask Introduction",
        "version": "1.0",
        "features": ["Routing", "Dynamic URL", "JSON Response"]
    }
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
