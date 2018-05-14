class Reserva:
    """
    Creamos la Clase de Reserva, dando sus caracteristicas
    """

    def __init__(self,  IdHab, hora, dia, mes, anio):
        self.IdHab = IdHab
        self.hora = hora
        self.dia = dia
        self.anio = anio


    def __repr__(self):
        return 'Usted ha escogido la siguiente ID de habitacion:\n'+str(self.IdHab+'\n Ha seleccionado la siguiente fecha para la reserva:\n'+str(self.dia)+'/'+str(self.mes)+'/'+str(self.anio)+' a las '+str(self.hora)+' horas.'

