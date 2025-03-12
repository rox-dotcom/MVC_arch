class SignosVitales:
    def __init__(self, presion, frecuencia, temperatura):
        self.presion = presion
        self.frecuencia = frecuencia
        self.temperatura = temperatura

    def mostrar_signos(self):
        return f"Presión: {self.presion}, Frecuencia: {self.frecuencia}, Temperatura: {self.temperatura}°C"
