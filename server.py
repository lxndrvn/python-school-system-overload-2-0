from flask import Flask, request, session, redirect, url_for, render_template
from models import *

app = Flask(__name__,template_folder="templates")
app.secret_key="SECRET_KEY"
tables=BaseModel.__subclasses__()

@app.route('/', methods=["GET","POST"])
def home(message=None):
    return render_template('home.html',message=message)


@app.route('/login',methods=['GET','POST'])
def login():
    for table in tables:
        if "email" in table._meta.fields.keys():
            records=table.select()
            for record in records:
                if record.email==request.form['user'] and record.password==request.form['password']:
                    session['user'] = record.email
                    session['options']={"Registered applicants":"Applicant","Interviews":"Interview","Logout":"Logout"}
                    return render_template('menu.html',options=session['options'])
    session['message']="wrong username or password"
    return redirect(url_for('home'))


@app.route('/catalogue/<option>', methods=['GET','POST'])
def catalogue(option):
    table=[table for table in tables if table.__name__==option][0]
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
    print(tables[2].__name__)
    app.run(debug=True)
