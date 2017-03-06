from flask import Flask, request, session, redirect, url_for, render_template
from models import *

app = Flask(__name__,template_folder="templates")
database=create_database()
tables=BaseModel.__subclasses__()

def create_tables():
    db.connect()
    db.drop_tables([Admin, Applicant], safe=True, cascade=True)
    db.create_tables([Admin, Applicant], safe=True)


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/login',methods=['POST'])
def login():
    index=int(request.form['index'])
    table=tables[index]
    for record in table.select():
      if record.email==request.form['email'] and record.password==request.form['password']:
        user = record
        return redirect(url_for('menu',user=user))
    return render_template('home.html')


@app.route('/menu', methods=['GET'])
def menu(user):
    options = user.options
    return render_template('menu.html',options=options)


@app.route('/catalogue/<index>', methods=['GET','POST'])
def catalogue(index):
    index=int(index)
    table=tables[index]
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
                               city=request.form['city'],
                               status="new",
                               gender=request.form['gender'],
                               email=request.form['email'])
    return redirect(url_for('home'))


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
