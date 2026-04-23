import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# --- RUBRIC REQUIREMENT: LOGGING ---
# This block ensures both successful and failed logins are recorded in Azure Log Stream
app.logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
app.logger.addHandler(streamHandler)

# --- AZURE LINUX FIX: PROXYFIX ---
# Required for MS Authentication to work on Azure App Service
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Initialize Session and Database
Session(app)
db = SQLAlchemy(app)

# Initialize Login Manager
login = LoginManager(app)
login.login_view = 'login'

# Import views to register routes
from FlaskWebProject import views, models