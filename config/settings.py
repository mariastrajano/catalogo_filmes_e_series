import json

class Settings:
    def __init__(self, caminho="settings.json"):
        with open(caminho, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    @property
    def limite_listas(self):
        return self.config["limite_listas_personalizadas"]

    @property
    def multiplicador_horas(self):
        return self.config["multiplicador_minutos_para_horas"]