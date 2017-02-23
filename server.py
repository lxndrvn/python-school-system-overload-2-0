from flask import Flask, request, session, redirect, url_for, render_template
from models import *

app = Flask(__name__, template_folder='./')


def create_tables():
    Database.database.drop_tables([Applicant], safe=True, cascade=True)
    Database.database.create_tables([Applicant, Admin], safe=True)
    Admin.create(email='admin@cf.com', password='trash')
    Applicant.create(application_code='000',
                     first_name='Rudolf',
                     last_name = 'Turo',
                     gender='male',
                     email='rudolf@gmail.com',
                     status='new')


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')

@app.route('/{{user}}', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html',records=records,fields=fields)

@app.route('/catalogue/<table>', methods=['GET', 'POST'])
def catalogue(table=Applicant):
    fields=table._meta.fields.keys()
    records=table.select()
    return render_template('catalogue.html',records=records,fields=fields)


@app.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        identification = Admin.select().where(Admin.email == email)
        if identification:
            admin = Admin.select().where(Admin.email == email).get()
            if admin.password == password:
                session['password'] = admin.password
        else:
            return render_template('index.html')
    return render_template('admin.html')


@app.route('/admin_page', methods=['GET'])
def admin_page():
    return render_template('admin.html', applicants=Applicant.select(), schools=School.select(),
                           mentors=Mentor.select(), interviews=Interview.select())


@app.route('/registration', methods=['GET'])
def form():
    applicant=Applicant()
    header=applicant.application_code if applicant != None else None
    return render_template('registration.html',applicant=applicant,header=header)

@app.route('/register/', methods=['POST'])
def registration():
    new_applicant = Applicant.create(first_name=request.form['first_name'],
                                     last_name=request.form['last_name'],
                                     city=request.form['city'],
                                     email=request.form['email'])
    return redirect(url_for('start.html', new_applicant=new_applicant))


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)