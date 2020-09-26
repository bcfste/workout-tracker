from gym import app
from flask import render_template

@app.route('/')
@app.route('/gym')
def index():
    user = { 'username' : 'sdhalil'}
    return render_template('index.html', title='Home', user=user)