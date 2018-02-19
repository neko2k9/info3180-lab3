from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flaskmailtest'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '53b71d9ec1501e'
app.config['MAIL_PASSWORD'] = '077e5c798efbb9'

mail = Mail(app)
from app import views