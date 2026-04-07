from flask import Flask, abort, redirect, render_template, request, session, url_for 
import os  

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Forum')    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if "user_logged" in session:
        return redirect(url_for('profile', username= session['user_logged']))
    elif request.method == 'POST' and request.form.get('username') == "selfedu" and request.form.get('password') == "password":
        session['user_logged'] = request.form.get('username')
        return redirect(url_for('profile', username= session['user_logged']))
    
    return render_template('login.html', title='Login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print(url_for('register'))
    return render_template('register.html', title='Register')

@app.route('/Profile/<username>/<path:post_id>')
def profile(username, post_id):
    if "user_logged" not in session or session['user_logged'] != username:
        abort (401)
    print(url_for('profile', username=username))
    return render_template('profile.html', title='Profile', username=username)


@app.route('/Add_feed', methods=['GET', 'POST'])
def add_feed():
    if "user_logged" not in session:
        abort (401)
    print(url_for('add_feed'))
    return render_template('add_feed.html', title='Add feed')
    

@app.route('/Feed/<path:post_id>')
def feed(post_id):
    print(url_for('feed'))
    return render_template('feed.html', title='Feed')


if __name__ == '__main__':
    app.run(debug=True)