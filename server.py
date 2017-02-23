from flask import *
from database import *
from models import *

app = Flask(__name__, template_folder='./')

def createtables():
    #Database.database.drop_tables([Applicant], safe=True, cascade=True)
    Database.database.create_tables([Applicant], safe=True)

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/catalogue/<table>', methods=['GET', 'POST'])
def catalogue(table=Applicant):
    fields=table._meta.fields.keys()
    records=table.select()
    return render_template('catalogue.html',records=records,fields=fields)

@app.route('/registration', methods=['GET'])
def form():
    applicant=Applicant()
    header=applicant.application_code if applicant != None else None
    return render_template('registration.html',applicant=applicant,header=header)
@app.route('/register/', methods=['POST'])
def registration():
        new_app = Applicant.create(first_name=request.form['first_name'], last_name=request.form['last_name'],
                                   city=request.form['city'], email=request.form['email'])
        flask-frontend
        return redirect(url_for('index.html'))


if __name__ == '__main__':
    createtables()
    app.run(debug=True)