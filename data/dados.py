import sqlite3
import datetime

from models.filme import Filme
from models.serie import Serie
from models.temporada import Temporada
from models.episodio import Episodio

class Dados:

    def __init__(self):
        self.conn = sqlite3.connect('banco.db')
        self.conn.row_factory = sqlite3.Row
        self.criar_tabelas()
        self.seed()

    def criar_tabelas(self):
        c = self.conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS midia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            tipo TEXT,
            genero TEXT,
            ano INTEGER,
            duracao INTEGER,
            classificacao TEXT,
            elenco TEXT,
            status TEXT,
            nota INTEGER,
            data_conclusao TEXT      
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS filme (
            id_midia INTEGER PRIMARY KEY,
            FOREIGN KEY(id_midia) REFERENCES midia(id)
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS serie (
            id_midia INTEGER PRIMARY KEY,
            FOREIGN KEY(id_midia) REFERENCES midia(id)
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS temporada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER,
            id_serie INTEGER,
            FOREIGN KEY(id_serie) REFERENCES serie(id_midia)
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS episodio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER,
            titulo TEXT,
            duracao INTEGER,
            status TEXT,
            nota REAL,
            id_temporada INTEGER,
            FOREIGN KEY(id_temporada) REFERENCES temporada(id)
        )
        """)

        self.conn.commit()

    # -------------------
    # SALVAR
    # -------------------

    def salvar_filme(self, filme):
        c = self.conn.cursor()

        if filme.status == "Assistido":
            filme.data_conclusao = datetime.date.today().isoformat()
        else:
            filme.data_conclusao = None

        c.execute("""
        INSERT INTO midia (titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (filme.titulo, "Filme", filme.genero, filme.ano, filme.duracao, filme.classificacao,
              filme.elenco, filme.status, filme.nota, filme.data_conclusao))
        
        id_midia = c.lastrowid

        c.execute("INSERT INTO filme (id_midia) VALUES (?)", (id_midia, ))

        self.conn.commit()

    def salvar_serie(self, serie):
        c = self.conn.cursor()

        c.execute("""
        INSERT INTO midia (titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (serie.titulo, "Serie", serie.genero, serie.ano, serie.duracao, serie.classificacao,
              serie.elenco, serie.status, serie.nota, serie.data_conclusao))

        id_midia = c.lastrowid

        c.execute("INSERT INTO serie (id_midia) VALUES (?)", (id_midia, ))
       

        for temporada in serie.temporadas:
            id_serie = c.lastrowid

            c.execute("INSERT INTO temporada (numero, id_serie) VALUES (?, ?)", (temporada.numero, id_serie))

            id_temp = c.lastrowid

            for episodio in temporada.episodios:
                c.execute("""
                INSERT INTO episodio (numero, titulo, duracao, status, nota, id_temporada)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    episodio.numero, episodio.titulo, episodio.duracao, episodio.status, episodio.nota, id_temp
                ))

        self.conn.commit()

    # -------------------
    # CARREGAR
    # -------------------

    def carregar_midias(self):

        c = self.conn.cursor()
        c.execute("SELECT * FROM midia")
        rows = c.fetchall()

        midias = []

        for m in rows:
            if m["tipo"] == "Filme":
                filme = Filme(
                    m["titulo"], "Filme", m["genero"], m["ano"], m["duracao"], 
                    m["classificacao"], m["elenco"], m["status"], m["nota"], m["data_conclusao"]
                )

                midias.append(filme)

            elif m["tipo"] == "Serie":
                serie = Serie(
                    m["titulo"], "Serie", m["genero"], m["ano"], m["duracao"], 
                    m["classificacao"], m["elenco"], m["status"], m["nota"], m["data_conclusao"]
                )

                c.execute("SELECT * FROM temporada WHERE id_serie=?", (m["id"],))
                temporadas = c.fetchall()

                for t in temporadas:
                    temporada = Temporada(t["numero"])

                    c.execute("SELECT * FROM episodio WHERE id_temporada=?", (t["id"],))
                    episodios = c.fetchall()

                    for e in episodios:
                        episodio = Episodio(
                            e["numero"], e["titulo"], e["duracao"], e["status"], e["nota"]
                        )

                midias.append(serie)

        return midias
    
    # -------------------
    # SEED
    # -------------------

    def seed(self):
        midias_seed = [
            ("Interestelar", "Filme", "Ficção", 2014, 169, 8.6, "Assistido", "2025-12-15"),
            ("Dark", "Serie", "Drama", 2017, 1620, 9.0, "Assistido", "2025-12-05"),
            ("Matrix", "Filme", "Ação", 1999, 136, 8.7, "Assistido", "2025-12-01")
        ]

        c = self.conn.cursor()

        c.execute("SELECT count(*) FROM midia")
        if c.fetchone()[0] == 0:
            for m in midias_seed:
                c.execute("""
                    INSERT OR IGNORE INTO midia
                    (titulo, tipo, genero, ano, duracao, nota, status, data_conclusao)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, m)

            self.conn.commit()