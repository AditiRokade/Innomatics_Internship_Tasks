from flask import Flask, render_template, request, redirect
import sqlite3, string, random

app = Flask(__name__)

# Initialize database
conn = sqlite3.connect('urls.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
             (id INTEGER PRIMARY KEY AUTOINCREMENT, longurl TEXT, shorturl TEXT)''')
conn.commit()
conn.close()

# Define function to generate short URLs
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT shorturl FROM urls WHERE longurl = ?', (long_url,))
    result = c.fetchone()
    if result:
        short_url = result[0]
    else:
        short_url = generate_short_url()
        c.execute('INSERT INTO urls (longurl, shorturl) VALUES (?, ?)', (long_url, short_url))
        conn.commit()
    conn.close()
    return render_template('result.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT longurl FROM urls WHERE shorturl = ?', (short_url,))
    result = c.fetchone()
    conn.close()
    if result:
        return redirect(result[0])
    else:
        return render_template('not_found.html')

if __name__ == '__main__':
    app.run(debug=True)
