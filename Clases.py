class Hotel:
    """
    Creamos la Clase de Hotel, dando sus caracteristicas
    """
    def __init__(self,id_Hotel, nombre, telefono, estrellas, sector):
        self.id_Hotel = id_Hotel
        self.nombre = nombre
        self.telefono = telefono
        self.estrellas = estrellas
        self.sector = sector

    def __repr__(self):
        return 'El nombre del hotel es: ' + str(self.nombre) + ', su telefono es : ' + str(self.telefono) + ' su calificación es de ' + str(self.estrellas) + ' estrellas, y esta ubicada en el siguiente sector ' + str(self.sector)
