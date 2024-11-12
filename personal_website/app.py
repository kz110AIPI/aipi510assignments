from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/education')
def education():
    return render_template('education.html', title='Education')

@app.route('/experience')
def experience():
    return render_template('experience.html', title='Experience')

@app.route('/skills')
def skills():
    return render_template('skills.html', title='Skills')

@app.route('/publications')
def publications():
    return render_template('publications.html', title='Publications')

if __name__ == '__main__':
    app.run(debug=True)
