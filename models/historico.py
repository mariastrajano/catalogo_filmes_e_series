import os
import datetime
import calendar
import sqlite3

from config.settings import Settings
s = Settings()

class Historico:
    """
    Gera relatórios de histórico com base no banco de dados.
    """      
    def __init__(self):
        self.conn = sqlite3.connect('banco.db')

    def converter_para_horas(self, minutos):
        return minutos * s.multiplicador_horas

    def ocupacao_por_semana(self):
        print("=== OCUPAÇÃO POR SEMANA ===")

        hoje = datetime.date.today()
        ano, num_semana, dia_semana = hoje.isocalendar()
        inicio = hoje - datetime.timedelta(days = dia_semana)
        fim = hoje + datetime.timedelta(days=6 - dia_semana)

        c = self.conn.cursor()
        c.execute("""
            SELECT SUM(duracao)
            FROM midia
            WHERE status = 'Assistido'
            AND data_conclusao BETWEEN ? AND ?
        """, (inicio, fim))

        resultado = c.fetchone()

        if resultado and resultado[0] is not None:
            duracao_semana = resultado[0]
            horas = self.converter_para_horas(duracao_semana)

            print(f"{horas:.2f} horas assistidas na semana.")
        else:
            print("Nenhuma mídia assistida esse mês encontrada.")

        print("")

    def ocupacao_por_mes(self):
        print("=== OCUPAÇÃO POR MÊS ===")

        hoje = datetime.date.today()
        inicio = hoje.replace(day=1)
        _, dias_no_mes = calendar.monthrange(hoje.year, hoje.month)
        fim = hoje.replace(day=dias_no_mes)
        
        c = self.conn.cursor()
        c.execute("""
            SELECT SUM(duracao)
            FROM midia
            WHERE status = 'Assistido'
            AND data_conclusao BETWEEN ? AND ?
        """, (inicio, fim))

        resultado = c.fetchone()

        if resultado and resultado[0] is not None:
            duracao_mes = resultado[0]
            horas = self.converter_para_horas(duracao_mes)

            print(f"{horas:.2f} horas assistidas no mês.")
        else:
            print("Nenhuma mídia assistida esse mês encontrada.")

        print("")