from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Shalini Agarwal',
        'title': 'Blog Post 1',
        'content': 'Getting started with Flask',
        'date_posted': 'August 21, 2024' 
    },
    {
        'author': 'Kartik Sehgal',
        'title': 'Blog Post 2',
        'content': 'hello world!',
        'date_posted': 'September 27, 2024' 
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) # the variable name used as the argument name here, i.e. posts, will be available to us in the template

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)