from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail



app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kingdom4112#$@localhost/FEEDBACK'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(200), unique=True)
    serviceprovider = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, client, serviceprovider, rating, comments):
        self.client = client
        self.serviceprovider = serviceprovider
        self.rating = rating
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        client = request.form['client']
        serviceprovider = request.form['service provider']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(client, serviceprovider, rating, comments)
        if client =='' or serviceprovider =='':
            return render_template('index.html', message='please enter required fields')
        if db.session.query(Feedback).filter(Feedback.client == client).count() == 0:
            data = Feedback(client, serviceprovider, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(client, serviceprovider, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted a feedback')

if __name__ == '__main__':
    app.run()
