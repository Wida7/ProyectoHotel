class Habitaciones:
    """
    Creamos la Clase de Habitaciones, dando sus caracteristicas
    """

    def __init__(self, Idhab, cuartos, cama, bano):
        self.Idhab = Idhab
        self.cuartos = cuartos
        self.cama = cama
        self.bano = bano

    def __repr__(self):
        return 'La identificacion de la habitacion es: '+str(self.Idhab)+' ,Cuenta con: '+str(self.cuartos)+' cuartos con cama '+str(self.cama)+' y '+str(self.bano)+' baño(s)'
