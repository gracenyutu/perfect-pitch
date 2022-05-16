from flask import Flask, render_template
app = Flask(__name__)

pitches = [
    {
        'author': 'Barrack Obama',
        'type': 'One Word Pitch',
        'content': 'Hope',
        'date_posted': 'May 13, 2022'
    },
    {
        'author': 'Google',
        'type': 'One Word Pitch',
        'content': 'Search',
        'date_posted': 'May 1, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)