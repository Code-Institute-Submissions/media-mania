from flask import Flask, render_template

app = Flask(__name__)

app.add_url_rule('/images/<path:filename>', ...)
app.add_url_rule('/css/<path:filename>', ...)

# Page routes
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/about-us')
def about():
    return render_template('about-us.html')

@app.route('/login')
def login():
    return render_template('login.html')