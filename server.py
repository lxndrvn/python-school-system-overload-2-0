from models import *
from flask import *
from user_interfaces import *
app = Flask(__name__, template_folder='templates')
from build import *


@app.route('/registration', methods=['GET', 'POST'])
def registration():
        new_app = Applicant.create(first_name=request.form['first_name'], last_name=request.form['last_name'],
                                   city=request.form['city'], email=request.form['email'])
        new_app.save()
        return redirect(url_for('index.html'))


if __name__ == '__main__':
    db.connect()
    db.drop_tables([Applicant], safe=True, cascade=True)
    db.create_tables([Applicant], safe=True)
    app.run(debug=True)