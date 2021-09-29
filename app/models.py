from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(200), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model, UserMixin):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    menu_item = db.relationship("MenuItem", back_populates="menus")


class MenuItem(db.Model, UserMixin):
    __tablename__ = 'menu_items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    menu_id = db.Column(db.Integer, db.ForeignKey("menus.id"))
    menu = db.relationship("Menu", back_populates="menu_items")
    
    menu_item_type_id = db.Column(db.Integer, db.ForeignKey("menu_item_types.id"))
    type = db.relationship("MenuItemType", back_populates="menu_items")


class MenuItemType(db.Model, UserMixin):
    __tablename__ = "menu_item_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    menu_item = db.relationship("MenuItem", back_populates="menu_item_types")
