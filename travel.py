from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/semesterproject'
db = SQLAlchemy(app)
class Bookform(db.Model):
    '''
    '''
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    Phone_num = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=True)
    Location = db.Column(db.String(255), nullable=True)
    guests = db.Column(db.Integer, nullable=False)

class Contacts(db.Model):
    '''
    '''
    S_no  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(255), nullable=True)
    message = db.Column(db.String(255), nullable=True)

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/tabout" , methods = ['GET', 'POST'])
def tabout():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        namee = request.form.get('name')
        emaill = request.form.get('email')
        num = request.form.get('number')
        subjectt = request.form.get('subject')
        msg = request.form.get('masg')
        entry = Bookform(name=namee, email=emaill, number=num, subject=subjectt, message=msg)
        db.session.add(entry)
        db.session.commit()
    return render_template('tabout.html')


@app.route("/Package")
def package():
    return render_template('Package.html')


@app.route("/tbook" , methods = ['GET', 'POST'])
def tbook():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        location = request.form.get('location')
        guests = request.form.get('guests')
        entry = Bookform(Name=name, Email=email, Phone_num=phone, address=address, Location=location, guests=guests)
        db.session.add(entry)
        db.session.commit()
    return render_template('tbook.html')


@app.route("/hunza")
def hunza():
    return render_template('hunza.html')


app.run(debug=True)
