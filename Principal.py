"""
Importamos los archivos de las clases "Objetos" y les asignamos una variable
"""
import Clases as Cl
import ClaseHabitaciones as Habi


"""
Llamamos el documento de texto de donde vamos a extraer los datos, y damos instrucciones sobre este
"""
filename = 'Hoteles.txt'
Hoteles =[]
a = 0

nombre=input("Buen Dia, ingrese su nombre por favor\n")
print("Buen dia " + nombre)
user = input("Si quieres ver los hoteles disponibles ingresa el numero 1\nSi quieres ver las habitaciones disponibles ingresa 2\nSi quieres ver tus reservas, ingresa 3\n")

if user == "1":

    with open (filename) as file_Object:
        lines = file_Object.readlines(a)
        for line in lines:
            temporal = (line.strip().replace('\n','').split(','))

            Hotel_1 = temporal[0]
            Hotel_2 = temporal[1]
            Hotel_3 = temporal[2]
            Hotel_4 = temporal[3]
            Hotel_5 = temporal[4]
            Hoteles.append(Cl.Hotel(Hotel_1,Hotel_2,Hotel_3,Hotel_4,Hotel_5))
            print(temporal)
            a =+ 1
    print("Gracias "+nombre+" que tenga buen día")

if user == "2":
    """
    Llamamos nuestro segundo archivo para extraer los datos
    """
    filename2 = 'Habitaciones.txt'
    Habitaciones = []
    h = 0
    with open(filename2) as file_Object:
        lines2 = file_Object.readlines(h)
        for linez in lines2:
            temporal2 = (linez.strip().replace('\n','').split(','))

            Hab_1 = temporal2[0]
            Hab_2 = temporal2[1]
            Hab_3 = temporal2[2]
            Hab_4 = temporal2[3]

            Habitaciones.append(Habi.Habitaciones(Hab_1,Hab_2,Hab_3,Hab_4))
            print(temporal2)
            a =+ 1
    print("Gracias "+nombre+" que tenga buen día")

if user == "3":
    filename3 = 'Reservas.txt'
    reserva = []
    h = 0
    with open(filename3) as file_Object:
        lines3 = file_Object.readlines(h)
        for linex in lines3:
            temporal3 = (linex.strip().replace('\n','').split(','))

            res_1 = temporal3[0]
            res_2 = temporal3[1]
            res_3 = temporal3[2]
            res_4 = temporal3[3]
            print(temporal3)
            reserva.append(Habi.Habitaciones(res_1,res_2,res_3,res_4))

            a =+ 1

    print("Gracias "+nombre+" que tenga buen día")



