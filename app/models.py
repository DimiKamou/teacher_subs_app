from . import db
from datetime import date

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance_hours = db.Column(db.Float, default=0)
    absences = db.relationship('Absence', backref='teacher', lazy=True)
    replacements = db.relationship('Replacement', backref='substitute', lazy=True)

class ClassGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True)

class Period(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)  # 1–8

class Absence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    period_id = db.Column(db.Integer, db.ForeignKey('period.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class_group.id'), nullable=False)
    justified = db.Column(db.Boolean, default=False)

    period = db.relationship('Period')
    class_group = db.relationship('ClassGroup')

class Replacement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    substitute_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    absence_id = db.Column(db.Integer, db.ForeignKey('absence.id'), nullable=False)

    absence = db.relationship('Absence', backref='replacements')
