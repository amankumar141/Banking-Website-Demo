from flask import Flask, render_template, request, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'admin_secret_key'  # Replace with a secure key

# Get absolute path to the database
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../database/data.db'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'adminpass':
            session['admin'] = True
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute("SELECT * FROM bank_data")
                data = c.fetchall()
                conn.close()
                return render_template('admin.html', data=data)
            except Exception as e:
                return f"Error loading data: {str(e)}"
        else:
            return "Invalid admin password."
    
    return '''
        <form method="POST">
            <input type="password" name="password" placeholder="Admin Password" />
            <button type="submit">View Data</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(port=5001, debug=True)