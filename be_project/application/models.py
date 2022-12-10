from .database import db
from sqlalchemy import events
class Farmer(db.Model):
    __tablename__ = 'farmer'
    farmer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name= db.Column(db.String)
    state= db.Column(db.String)
    mobile=db.Column(db.String(10))
    district= db.Column(db.String)
    farms=db.relationship("Farm", backref="farmowner") 
    __table_args__ = (db.UniqueConstraint('first_name','middle_name', 'last_name', name='_names_uc'),)

class Farm(db.Model):
    __tablename__ = 'farm'
    farm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    farm_name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)
    area = db.Column(db.Float)
    farmer_id= db.Column(db.Integer,  db.ForeignKey("farmer.farmer_id"), nullable=False)
    past_data=db.relationship("PastData", backref="farm_data") 

class PastData(db.Model):
    __tablename__ = 'past_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    farm_id = db.Column(db.Integer,  db.ForeignKey("farm.farm_id"), nullable=False) 
    start_of_season = db.Column(db.DateTime)
    end_of_season = db.Column(db.DateTime)
    crop_type = db.Column(db.String)
    crop_variety = db.Column(db.String)
    crop_yield=db.Column(db.String)
