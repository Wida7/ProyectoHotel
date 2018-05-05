def Crear_reserva(hora,dia,mes,año,IdHab):
    """
    Creamos una funcion donde nos valide una reserva para guardar en un txt
    :param hora: ingresa hora reserva
    :param dia: ingresa dia reserva
    :param mes: ingresa mes reserva
    :param año: ingresa año reserva
    :param IdHab: ingresa identificacion de la reserva
    :return: validacion de reserva y guardar
    """

archivo = open("Reservas.txt","a")
reserva=[]

IdHab=str(input("Ingresa IdHab de reserva:\n"))
reserva.append(IdHab)
hora=str(input("Ingresa hora(militar) de reserva:\n"))
reserva.append(hora)
dia=str(input("Ingresa dia de reserva:\n"))
reserva.append(dia)
mes=str(input("Ingresa mes de reserva:\n"))
reserva.append(mes)
año=str(input("Ingresa año de reserva:\n"))
reserva.append(año)

archivo.write(str(reserva)+'\n')

archivo.close()
