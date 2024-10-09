import os
os.system("cls")

from funciones_parcial import *

#Gestión de pacientes en una clínica
#En la clínica "La Fuerza" se requiere desarrollar un sistema de gestión de pacientes. El sistema
#debe gestionar la información de los pacientes atendidos en el día. Para cada paciente, se
#almacenará:
#• Número de historia clínica (un número entero).
#• Nombre del paciente (una cadena de texto).
#• Edad del paciente (un número entero).
#• Diagnóstico (una cadena de texto).
#• Cantidad de días de internación (un número entero).
#La información de todos los pacientes debe almacenarse en un array bidimensional, donde
#cada fila representará un paciente, y las columnas contendrán los datos mencionados arriba.
#Recordar que el array debe comenzar vacío.
#Presentamos un ejemplo de cómo debería verse:
#Requerimientos:
#1. Interfaz del programa:
#• El sistema debe mostrar un menú interactivo para que el usuario pueda elegir
#entre las diferentes opciones del sistema (cargar pacientes, buscar paciente
#por Historia Clínica, determinar paciente con más/menos días de internación,
#ordenar pacientes por número de historia clínica, salir del sistema, etc.).
#• El menú debe estar dentro de un bucle que permita al usuario realizar
#múltiples operaciones hasta que decida salir.
#2. Cargar pacientes:
#• Permitir al usuario ingresar los datos de los pacientes, almacenando la
#información en una lista anidada (arreglo bidimensional), como se muestra en
#la imagen de arriba. La cantidad de pacientes a ingresar debe ser determinada
#por el usuario.
#3. Mostrar la lista de pacientes:
#• Imprimir en pantalla todos los datos de los pacientes almacenados en el
#arreglo bidimensional, mostrando cada fila como un paciente.
#4. Búsqueda de pacientes:
#• Implementar una función que, dado el número de historia clínica de un
#paciente, busque en la lista y muestre todos los datos de dicho paciente (o un
#mensaje indicando que no se encontró al paciente).
#5. Ordenamiento de pacientes:
#• Implementar una función que permita ordenar la lista de pacientes por el
#número de Historia Clínica en forma ascendente. Se podrá utilizar cualquier
#algoritmo de ordenamiento.
#6. Determinar el paciente con mayor cantidad de días de internación:
#• Implementar una función que calcule e imprima el paciente con más días de
#internación, mostrando sus datos completos.
#7. Determinar el paciente con menor cantidad de días de internación:
#• Implementar una función que calcule e imprima el paciente con menos días de
#internación, mostrando sus datos completos.
#8. Cantidad de pacientes con días de internación mayor a 5 días.
#• Implementar una función que recorra la lista de pacientes y cuente cuántos
#pacientes tienen más de 5 días de internación.
#9. Promedio de días de internación de todos los pacientes.
#• Implementar una función que calcule el promedio de días de internación de
#todos los pacientes registrados.


#Sugerencias:
#▪ Se recomienda la validación de los datos ingresados por el usuario.
#▪ Organizar el código en funciones y, si es posible, en módulos independientes. Utilizar
#import para incorporar funcionalidades de otros módulos cuando sea necesario.

#▪ Se aconseja incluir documentación de funciones, sugerencia de tipos y comentarios
#explicativos donde lo consideren necesario.
#▪ Utilizar las estructuras que vimos hasta este momento de la cursada.
#▪ Utilizar correctamente arreglos bidimensionales para almacenar la información.
#▪ Proporcionar salidas claras para el usuario. La presentación de los datos debe ser
#comprensible y legible. Se recomienda utilizar f-string.
#Entrega del programa
#▪ La entrega se deberá realizar mediante el link al repositorio de GitHub.

pacientes = []

#• Menú interactivo:
def mostrar_menu ():
    a = input('''
    Menu principal:
    
    1 - Cargar pacientes
    2 - Buscar paciente
    3 - Mostrar paciente con más dias de internacion o paciente menos dias de internacion.
    4 - Ordenar pacientes por historia clinica.
    5 - Mostrar lista de pacientes
    6 - Mostrar paciente con mas de 5 dias de internacion
    7 - Promedio de dias de internacion de pacientes
    8 - Salir del programa
    
    Opcion elegida: ''')
    return a

#• Permite al usuario ingresar nuevos pacientes
#• a = Número de historia clínica (un número entero).
#• b = Nombre del paciente (una cadena de texto).
#• c = Edad del paciente (un número entero).
#• d = Diagnóstico (una cadena de texto).
#• e = Cantidad de días de internación (un número entero).
def agregar_paciente (a, b, c, d, e): 
    pacientes.append([a, b, c, d, e])
    return

#Busqueda de paciente
# a = pacientes (array)
def buscar_paciente(b):
    if pacientes != []:
        for i in range(len(pacientes)):
            if b == pacientes[i][0]:
                print(f"Historia clinica del paciente buscado: {pacientes[i]}")
                return
            else:
                print("El paciente buscado no esta en el sistema.")
    else:
        print("Error. Para elegir esta opcion, perimero debe ingresar pacientes al sistema.")

#Determina el paciente con mayor cantidad de días de internación
def paciente_mas_dias()-> list: 
    if pacientes != []:
        e = 0
        for i in range(len(pacientes)):
            if e < pacientes[i][4]:
                e = pacientes[i][4]
                nombre_paciente = pacientes[i][1]
        print(f"El paciente {nombre_paciente} tiene el mayor numero de dias de internacion: {e} dias.")
    else:
        print("Error. Para elegir esta opcion, perimero debe ingresar pacientes al sistema.")

#Determina el paciente con menor cantidad de días de internación
def paciente_menos_dias()-> list:#
    if pacientes != []:
        e = pacientes[0][4]
        for i in range(len(pacientes)):
            if e > pacientes[i][4]:
                e = pacientes[i][4]
                nombre_paciente = pacientes[i][1]
        print(f"El paciente {nombre_paciente} tiene el menor numero de dias de internacion: {e} dias.")
    else:
        print("Error. Para elegir esta opcion, perimero debe ingresar pacientes al sistema.")

#ordenar pacientes por número de historia clínica
def ordenar_pacientes(a)-> list: #Ordenamiento de pacientes
    if pacientes != []:
        n = len(pacientes)
        for i in range(n-1):
            for j in range(n-1-i): 
                if pacientes[j][4] > pacientes[j+1][4]:
                    aux = pacientes[j+1]
                    pacientes[j+1] = pacientes[j]
                    pacientes[j] = aux
    else:
        print("Error. Para elegir esta opcion, perimero debe ingresar pacientes al sistema.")

def burcar_paciente_mas5(): #Busca cantidad de pacientes con mas de 5 días de internación.
    if pacientes != []:
        paciente_encontrado = False
        pacientes_mas5_dias = []
        for i in range(len(pacientes)):
            if pacientes[i][4] > 5:
                pacientes_mas5_dias.append(pacientes[i])
                paciente_encontrado = True
        if not paciente_encontrado:
            mensaje = "No hay pacientes con mas de 5 dias de internacion"
            return mensaje
        return pacientes_mas5_dias
    else:
        print("Error, prinero debe ingresar productor al inventario.") 

def promediar_dias_internacion(): #Promedia todos los dias de internacion de los pacientes
    dias = 0
    for i in range(len(pacientes)):
        dias += pacientes[i][4]
    promedio_dias = dias / i
    return promedio_dias

eleccion = "laLala"
while eleccion != "8":
    eleccion = mostrar_menu() #• El menú debe estar dentro de un bucle que permita al usuario realizar múltiples operaciones hasta que decida salir.
    match eleccion:
        case "1":
            a = input("Ingrese un numero de historia clinica: ")
            while not a.isdigit() or int(a) < 0:
                a = input("Debe ingresar un caracter numerico: ")
            a = int(a)              
            b = input("Ingrese el nombre del paciente: ")
            c = input("Ingrese la edad del paciente: ")
            while not c.isdigit() or int(c) < 0:
                c = input("Debe ingresar un caracter numerico: ")
            c = int(c)
            d = input("Ingrese el diagnostico del paciente: ")
            e = input("Ingrese la cantidad de dias de internacion: ")
            while not e.isdigit() or int(e) < 0:
                e = input("Debe ingresar un caracter numerico: ")
            e = int(e)
            agregar_paciente(a, b, c, d, e)
        case "2":
            num_historia_clin = input("Ingrese el numero de historia clinica del paciente que dese buscar: ")
            while not num_historia_clin.isdigit() or int(num_historia_clin) < 0:
                num_historia_clin = input("Debe ingresar un caracter numerico: ")
            num_historia_clin = int(num_historia_clin)
            buscar_paciente(num_historia_clin)
        case "3":
            mas_o_menos = input("Si desea buscar el paciente con mas dias de internacion ingrese 1, si desea buscar el paciente con menos dias de internacion ingrese 2:  ")
            if mas_o_menos == "1":
                paciente_mas_dias()
            elif mas_o_menos == "2":
                paciente_menos_dias()
        case "4":
            ordenar_pacientes(pacientes)
        case "5":
            if pacientes != []:
                for i in range(len(pacientes)): #Muestra lista de pacientes
                    print(f'''
        Historia clinica: {pacientes[i][0]}, Nombre del paciente: {pacientes[i][1]}, Edad: {pacientes[i][2]}, Diagnostico: {pacientes[i][3]}, Dias de internacion: {pacientes[i][4]}''')
            else: 
                print("Error, debe ingresar al menos un paciente para elegir esta opcion.")
        case "6": #Mostrar pacientes con mas de 5 dias de internacion
            print(f"Los pacientes con mas de 5 dias de internacion son: {burcar_paciente_mas5()}")
        case "7": #Promedio dias de internacion
            print(f"EL promedio de dias de internacion de todos los pacientes es {promediar_dias_internacion()}")
        case "8":
            print("Usted a salido del programa, adios.")
        case _ :
            print("Error, ingrese otra opcion: ")
