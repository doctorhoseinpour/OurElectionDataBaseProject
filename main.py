from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import  Marshmallow
import os


## init

election = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

## set up data base

election.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + os.path.join(basedir, 'election_db.sql')
election.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(election)
marsh = Marshmallow(election)


## fill database full of data lol



if __name__ == '__main__':
    election.run(debug=True)