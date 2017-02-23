from flask import Flask, request, session, redirect, url_for, render_template
from models import *

app = Flask(__name__)


def create_tables():
    db.connect()
    db.drop_tables([Admin, Applicant], safe=True, cascade=True)
    db.create_tables([Admin, Applicant], safe=True)
    Admin.create(email='admin@cf.com', password='trash')
    Applicant.create(application_code='000',
                     first_name='Rudolf',
                     last_name = 'Ronda',
                     gender='male',
                     email='rudolf@gmail.com',
                     status='new')


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu(table):
    if request.form['email'] in [record.email for record in table] and request.form['password'] == table.where(cls.email == request.form['email']):
        user = table.select().where(table.email == request.form['email'])
        options = user.options
    return render_template('menu.html', options=options)


@app.route('/catalogue/<table>', methods=['GET', 'POST'])
def catalogue(table=Applicant):
    fields=table._meta.fields.keys()
    records=table.select()
    return render_template('catalogue.html',records=records,fields=fields)


@app.route('/login', methods=['GET', 'POST'])
def admin_login():
    email = request.form['email']
    password = request.form['password']
    identification = Admin.select().where(Admin.email == email)
    if identification:
        admin = Admin.select().where(Admin.email == email).get()
        if admin.password == password:
            session['password'] = admin.password
    else:
        return render_template('menu.html')
    return render_template('admin.html')


@app.route('/admin_page', methods=['GET'])
def admin_page():
    return render_template('menu.html', applicants=Applicant.select(), schools=School.select(),
                           mentors=Mentor.select(), interviews=Interview.select())


@app.route('/registration', methods=['GET'])
def form():
    return render_template('registration.html')


@app.route('/registration', methods=['POST'])
def registration():
        new_app = Applicant.create(first_name=request.form['first_name'], last_name=request.form['last_name'],
                                   city=request.form['city'], email=request.form['email'])
        new_app.save()
        return redirect(url_for('home'))


if __name__ == '__main__':
    #create_tables()
    app.run(debug=True)