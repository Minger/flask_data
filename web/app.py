from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pprint import pprint

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres:5432/dataset'
#db = SQLAlchemy(app)
#metadata = MetaData(db.engine)
db = 'postgresql://postgres:postgres@postgres:5432/dataset'
tables = ['insurance']
engine = create_engine(db)
#metadata.reflect(bind=db.engine, only=tables)
Base = automap_base()
Base.prepare(engine, reflect=True)

session = Session(engine)

Insurance = Base.classes.insurance

@app.route("/insurance/<policyid>")   
def insurance(policyid):
    one = session.query(Insurance).filter(Insurance.policyid == policyid).one()
    return one.county

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')