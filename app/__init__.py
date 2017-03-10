
from flask import Flask
from flask_socketio import SocketIO
from .finance_news import *


app = Flask(__name__)
if not app.debug:
    import os
    base_dir = os.path.split(os.path.realpath(__file__))[0]
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(base_dir+'/finance-news.log', maxBytes=10*1024*1024,backupCount=5)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
socketio = SocketIO(app)

socketio.on_namespace(FinanceNews('/finance_news'))
