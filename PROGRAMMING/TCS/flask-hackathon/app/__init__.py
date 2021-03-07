from flask import Flask
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = '28cd51a3bb2e0dbd90839a3d4e897f493fa13755'


bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'signin'
#login_manager.login_message_category = 'info'
#login_manager.init_app(app)


from app import routes
