class Cita:
    def __init__(self, paciente, hora, estado):
        self.paciente = paciente          # Nombre del paciente o correo del paciente
        self.hora = hora                  # Hora de la cita (puede ser un string, por ejemplo: "10:00 AM")
        self.estado = estado              # Estado de la cita (ejemplo: "Pendiente", "Confirmada", etc.)

    def get_paciente(self):
        return self.paciente

    def get_hora(self):
        return self.hora

    def get_estado(self):
        return self.estado
