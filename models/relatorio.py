import os
import sqlite3
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

class Relatorio:
    """
    Gera relatórios com base em listas de mídias.
    """

    def media_nota_genero(self):
        print("=== MÉDIA DAS NOTA POR GÊNERO ===")
        cursor.execute("SELECT genero, AVG(nota) AS media_notas FROM midias GROUP BY genero")

        for row in cursor.fetchall():
            print(f"{row[0]}: {row[1]}")

        print("")
        menu = input("Pressione Enter para continuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

    def top_10(self):
        print("=== TOP 10 ===")
        tipo = input("Tipo: ").capitalize()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== TOP 10 - {tipo} ===")

        top = cursor.execute("SELECT titulo, nota, status FROM midias WHERE status = 'Assistido' AND tipo = '"+tipo+"' ORDER BY nota DESC LIMIT 10")
        result_top = top.fetchall()

        if result_top and result_top[0] is not None:
            i = 0
            for row in result_top:
                i += 1
                print(f"{i}. {row[0]} - {row[1]}")

        else:
            print("Nenhuma mídia assistida encontrado.")

        print("")
        menu = input("Pressione Enter para continuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

    def tempo_total_assistido(self):
        print("=== TEMPO TOTAL ASSISTIDO ===")

        f = cursor.execute("SELECT SUM(duracao) FROM midias WHERE status = 'Assistido' AND tipo = 'Filme'")
        result_f = f.fetchone()

        s = cursor.execute("SELECT SUM(duracao) FROM midias WHERE status = 'Assistido' AND tipo = 'Serie'")
        result_s = s.fetchone()

        if result_f and result_f[0] is not None:
            duracao_f = result_f[0]
            print(f"Filmes: {duracao_f} minutos.")
        else:
            print("Nenhum filme assistido encontrado.")

        if result_s and result_s[0] is not None:
            duracao_s = result_s[0]
            print(f"Séries: {duracao_s} minutos.")
        else:
            print("Nenhuma série assistida encontrado.")

        print("")
        menu = input("Pressione Enter para continuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')