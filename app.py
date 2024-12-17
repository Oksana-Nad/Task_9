from flask import Flask, render_template
import sqlite3


app = Flask(__name__, template_folder='templates')


@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/visits')
def visits():
    conn = sqlite3.connect('visits.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM visits")
    results = cursor.fetchall()

    conn.close()
    
    return render_template('visits.html', data=results)

if __name__ == '__main__':
    app.run(debug=True)
