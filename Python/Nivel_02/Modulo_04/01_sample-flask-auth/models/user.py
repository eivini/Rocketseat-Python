from database import db      # importação do db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id (int), username (text), password (text), role (text)
    id = db.Column(db.Integer, primary_key=True)             # primary_key (Chave primária)
    username = db.Column(db.String(80), nullable=False, unique=True)      # nullable=False (Não nulo/notNull)   # unique=True (Garante que é único)
    password = db.Column(db.String(80), nullable=False)       # nullable=False (Não nulo/notNull)
    role = db.Column(db.String(80), nullable=False, default='user')  # dafault == um valor padrão

    