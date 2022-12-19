from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/planets')
def planets():
    return render_template('planets_page.html')

@app.route('/constellations')
def constellations():
    return render_template('constellations_page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)