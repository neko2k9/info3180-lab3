from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flaskmailtest'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '5c382fd5d57e47'
app.config['MAIL_PASSWORD'] = 'bdfd42d6777688'

mail = Mail(app)
from app import views