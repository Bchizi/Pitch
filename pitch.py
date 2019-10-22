from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'leon bichanga',
        'title': 'post no:1',
        'content': 'First pitch ',
        'date_posted': 'September 20,2019'

    },
    {
        'author': 'Martha chitayi',
        'title': 'post no:2',
        'content': 'Second pitch ',
        'date_posted': 'September 21,2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About') 


if __name__ == '__main__':
    app.run(debug=True)
