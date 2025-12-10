import sqlite3
import datetime

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

#cursor.execute("CREATE TABLE midias (titulo TEXT, tipo TEXT, genero TEXT, ano INTEGER, duracao INTEGER, classificacao TEXT, elenco TEXT, status TEXT, nota INTEGER, data_conclusao TEXT)")

#res = cursor.execute("SELECT titulo FROM midias")
#print(res.fetchall())

#cursor.execute("DELETE FROM midias WHERE nota = 10")
#banco.commit()