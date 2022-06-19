from main import db


class usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(40))
    telefone = db.Column(db.String(20))

    def __repr__(self):
        return '<Name %r>' % self.name
