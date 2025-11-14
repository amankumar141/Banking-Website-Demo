from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Get absolute path to the database
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../database/data.db'))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Dummy login check
        if username == 'user' and password == 'pass':
            session['user'] = username
            return redirect('/form')
        else:
            return "Invalid credentials. Try again."
    
    return render_template('login.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    user = session.get('user')
    if not user:
        return redirect('/')
    
    if request.method == 'POST':
        data = request.form.get('details')
        if not data:
            return "No data submitted."

        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("INSERT INTO bank_data (user, details) VALUES (?, ?)", (user, data))
            conn.commit()
            conn.close()
            return "Form submitted successfully!"
        except Exception as e:
            return f"Error submitting form: {str(e)}"
    
    return render_template('form.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)