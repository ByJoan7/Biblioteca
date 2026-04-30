import json

class JSONManager:

    @staticmethod
    def guardar(ruta, datos):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    @staticmethod
    def cargar(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []