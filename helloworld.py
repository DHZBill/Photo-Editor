from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    url_for('static', filename='homeage.js')
    return render_template('homepage.html')

@app.route('/hello')
def hello():
    app.logger.info('helwoo world')
    return 'world'
# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)
