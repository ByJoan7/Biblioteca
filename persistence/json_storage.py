import json
import os

class JSONStorage:

    def __init__(self, ruta):
        self.ruta = ruta

    def guardar(self, data):
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def cargar(self):
        if not os.path.exists(self.ruta):
            return []
        with open(self.ruta, "r", encoding="utf-8") as f:
            return json.load(f)