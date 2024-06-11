from app import db


class Illness(db.Model):
    __tablename__ = 'illness'
    mkb10 = db.Column(db.String(5), index=True, primary_key=True)
    name = db.Column(db.String(500), nullable=False)

    # therapy = db.relationship('Therapy', lazy='dynamic')
    # diagnostic = db.relationship('Diagnostic', lazy='dynamic')

    def __repr__(self):
        return f'<Illness {self.mkb10}: {self.name}>'

    def get_name(self):
        return self.name

    def get_mkb10(self):
        return self.mkb10

    def to_dict(self):
        return dict({"mkb10": self.mkb10, "name": self.name})


class Therapy(db.Model):
    __tablename__ = 'therapy'
    mkb10 = db.Column(db.String(5), db.ForeignKey('Illness.mkb10'), index=True, primary_key=True)
    therapy_info = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Therapy for illness {self.mkb10}: {self.therapy_info}>'

    def get_mkb10(self):
        return self.mkb10

    def get_therapy(self):
        return self.therapy_info

    def to_dict(self):
        return dict({"mkb10": self.mkb10, "therapy_info": self.therapy_info})


class Diagnostic(db.Model):
    __tablename__ = 'diagnosis'
    mkb10 = db.Column(db.String(5), db.ForeignKey('Illness.mkb10'), index=True, primary_key=True)
    diagnosis_info = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Diagnostic for illness {self.mkb10}: {self.diagnosis_info}>'

    def get_mkb10(self):
        return self.mkb10

    def get_diagnosis(self):
        return self.diagnosis_info

    def to_dict(self):
        return dict({"mkb10": self.mkb10, "diagnosis_info": self.diagnosis_info})
