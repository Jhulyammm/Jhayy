from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # For demo purposes, just print the credentials
        print(f"Login attempt: Username: {username}, Password: {password}")
        # In a real app, you'd verify credentials here
        return "Login successful! (This is just a demo)"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)