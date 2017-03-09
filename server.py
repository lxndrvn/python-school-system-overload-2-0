from flask import Flask, request, session, redirect, url_for, render_template
from models import *

app = Flask(__name__, template_folder="templates")
app.secret_key = "SECRET_KEY"
tables = BaseModel.__subclasses__()


class Filter():
    def __init__(self, table):
        if session['identity'] == "Applicant":
            if table.__name__ == "Interview":
                identity = Applicant.select().where(Applicant.email == session['email'])
                self.table = table.select().where(table.applicant == identity)
            else:
                self.table = table.select().where(table.email == session['email'])
        elif session['identity'] == "Mentor":
            identity = Applicant.select().where(Applicant.email == session['email'])
            self.table = table.select().where(table.mentor == identity)
        else:
            self.table = table.select()

    def render(self):
        return self.table


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    for table in tables:
        if "email" in table._meta.fields.keys():
            records = table.select()
            for record in records:
                if record.email == request.form['user'] and record.password == request.form['password']:
                    session['email'] = record.email
                    session['identity'] = table.__name__
                    if table.__name__ == "Admin":
                        session['options'] = {"Registered applicants": "Applicant", "Interviews": "Interview"}
                    elif table.__name__ == "Mentor":
                        session['options'] = {"My Interviews": "Interview"}
                    elif table.__name__ == "Applicant":
                        session['options'] = {"My Application": "Applicant", "Calendar": "Interview"}
                    return redirect(url_for('menu', identity=session['identity']))
    message = "wrong username or password"
    return render_template('home.html', message=message)


@app.route("/<identity>", methods=['GET', 'POST'])
def menu(identity):
    if 'email' in session:
        for table in tables:
            if table.__name__ == identity:
                if session['email'] in [record.email for record in table.select()]:
                    return render_template("menu.html")
    message = "You have no " + user + " rights"
    return render_template('home.html', message=message)


@app.route('/catalogue/<option>', methods=['GET', 'POST'])
def catalogue(option):
    table = [table for table in tables if table.__name__ == option][0]
    fields = table._meta.fields.keys()
    records = Filter(table).render()
    return render_template('catalogue.html', records=records, fields=fields)


@app.route('/registration', methods=['GET'])
def form():
    return render_template('registration.html')


@app.route('/registration', methods=['POST'])
def registration():
    Applicant.create(first_name=request.form['first_name'],
                     last_name=request.form['last_name'],
                     gender=request.form['gender'],
                     email=request.form['email'],
                     city=City.select().where(City.name == request.form['city']),
                     password=request.form['password'])
    message = "Registration successful. We've sent You an email with further notices."
    return render_template('home.html', message=message)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop("email")
    message = "Logged out"
    return render_template('home.html', message=message)


if __name__ == '__main__':
    print(tables[2].__name__)
    app.run(debug=True)