from flask import Flask, request, session, redirect, url_for, render_template
from models import *

app = Flask(__name__,template_folder="templates")
tables=BaseModel.__subclasses__()

@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/login',methods=['POST'])
def login():
    for table in tables:
        records=table.select()
        for record in records:
            if record.email==request.form['user'] and record.password==request.form['password']:
                user = record
                return redirect(url_for('menu',user=user))
    return render_template('home.html',message="wrong username or password")


@app.route('/<user>', methods=['GET'])
def menu(user):
    options = user.options
    return render_template('menu.html',user=user,options=options)


@app.route('/catalogue/<index>', methods=['GET','POST'])
def catalogue(index):
    index=int(index)
    table=tables[index]
    fields=table._meta.fields.keys()
    records=table.select()
    return render_template('catalogue.html',records=records,fields=fields)


@app.route('/admin_page', methods=['GET'])
def admin_page():
    return render_template('menu.html', applicants=Applicant.select(), schools=School.select(),
                           mentors=Mentor.select(), interviews=Interview.select())


@app.route('/registration', methods=['GET'])
def form():
    return render_template('registration.html')


@app.route('/registration', methods=['POST'])
def registration():
    Applicant.create(first_name=request.form['first_name'],
                    last_name=request.form['last_name'],
                    gender=request.form['gender'],
                    email=request.form['email'],
                    city=City.select().where(City.name==request.form['city']),
                    password = request.form['password'])
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
