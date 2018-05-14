from datetime import *

def Crear_reserva(hora,dia,mes,anio,IdHab):
    """
    Creamos una funcion donde nos valide una reserva para guardar en un txt

    :param hora: ingresa hora reserva
    :param dia: ingresa dia reserva
    :param mes: ingresa mes reserva
    :param año: ingresa año reserva
    :param IdHab: ingresa identificacion de la reserva
    :return: Crear una reserva validada
    """

 """Creamos un archivos txt para enviar informacion allí"""

archivo = open("Reservas.txt","a")
reserva=[]

nombre=input("Buen dia, por favor ingresa tu nombre, gracias\n")
print("Estimado usuario "+nombre+" Para realizar una reserva ingresa correctamente los suiguientes datos por favor\n")

"""Creamos los campos para llenar en el archivo txt"""

IdHab=str(input("Ingresa IdHab de reserva:\n"))
reserva.append(IdHab)
hora=str(input("Ingresa hora de reserva:\n"))
reserva.append(hora)
dia=int(input("Ingresa dia de reserva (DD):\n"))
reserva.append(dia)
mes=int(input("Ingresa mes de reserva(MM):\n"))
reserva.append(mes)
anio=int(input("Ingresa año de reserva (YYYY):\n"))
reserva.append(anio)
fecha_reserva = date(anio, mes, dia)


print("----------------------------------***-Los datos de la reserva son los siguientes: -***----------------------------------\n"+"IdHab: "
        +IdHab+"\nFECHA: "+fecha_reserva.strftime('%d,%b,%Y')+"HORA: \n"+hora)

Verificacion = input("***SI LA SUIGUIENTE INFORMACION ES CORRECTA INGRESE EL NUMERO 1 PARA CONFIRMAR DE LO CONTRARIO INGRESE 2\n")

if Verificacion=="1":
    hoy = datetime.now().date()
    reserva.append(hoy)
    print("***RESERVA REALIZADA CON ÉXITO QUE TENGA EXCELENTE DIA***")

    archivo.write(str(reserva)+'\n')

    archivo.close()
else:
    print("***LA INFORMACION SE HA ELIMINADO, INTENTE DE NUEVO POR FAVOR***")

