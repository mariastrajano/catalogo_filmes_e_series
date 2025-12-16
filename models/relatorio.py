import os
import sqlite3

from config.settings import Settings
s = Settings()

class Relatorio:
    """
    Gera relatórios com base no banco de dados.
    """
    def __init__(self):
        self.conn = sqlite3.connect('banco.db')

    def converter_para_horas(self, minutos):
        return minutos * s.multiplicador_horas
    
    def media_notas_por_genero(self):
        print("=== MÉDIA DAS NOTAS POR GÊNERO ===")

        c = self.conn.cursor()
        c.execute("""
            SELECT genero, AVG(nota)
            FROM midia
            WHERE status = 'Assistido'
            GROUP BY genero
        """)

        resultados = c.fetchall()

        if not resultados:
            print("Nenhuma avaliação encontrada.")
        
        else:
            for genero, media in resultados:
                print(f"{genero}: {media:.2f}")

        print("")

    def tempo_total_assistido(self):
        print("=== TEMPO TOTAL ASSISTIDO ===")

        c = self.conn.cursor()
        c.execute("""
            SELECT tipo, SUM(duracao)
            FROM midia
            WHERE status = 'Assistido'
            GROUP BY tipo
        """)

        resultados = c.fetchall()

        if not resultados:
            print("Nenhma mídia assistida encontrada")
        
        else:
            for tipo, minutos in resultados:
                horas = self.converter_para_horas(minutos)
                print(f"{tipo}: {horas:.2f} horas")

        print("")

    def top_10(self):
        print("=== TOP 10 ===")
        tipo = input("Tipo: ").capitalize()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== TOP 10 - {tipo} ===")

        c = self.conn.cursor()
        c.execute("""
            SELECT titulo, nota
            FROM midia
            WHERE status = 'Assistido' and tipo = ?
            ORDER BY nota DESC
            LIMIT 10
        """, (tipo, ))

        resultados = c.fetchall()

        if not resultados:
            print("Nenhuma mídia assistida encontrada.")
            return

        for i, (titulo, nota) in enumerate(resultados, 1):
            print(f"{i}. {titulo} — {nota}")

        print("")
