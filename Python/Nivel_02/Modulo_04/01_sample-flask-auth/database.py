from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Quando abrimos uma conexão com o banco de dados ela abre uma,
# Session <- conexão ativa  (Obs: não pode deixar muitas sessões abertas, porque cada banco de dados tem sua pecularidade, alguns podem aguentar muitas sessões simultaneas,
# e outros não)