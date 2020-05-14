from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author':'michael schembri',
        'title':'cat ipsum',
        'content':'is really funny',
        'date_posted':'10-05-2020'
    },
    {
        'author':'some random guy',
        'title':'dog ipsum',
        'content':'is not a thing funny',
        'date_posted':'11-05-2020'
    }
    ]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
