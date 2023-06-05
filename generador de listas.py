import os
import time
import ipaddress # Para intrducior direcciones IP

listas = []# Crear una lista vacía para almacenar las listas de elementos
#matriz = ["ZONA","\t","DISPOSITIVO","\t","INTERFAZ","\t","IP","\t","\t","MASCARA","\t","\t","DESTINO","\t","\t","CAPA JERÁRQUICA","\t","PROTOCOLOS DE RED","\t","SERVICIOS DE RED","\n"]#encabezado de la documentacion
#listas.append(matriz)


def leer_documento_txt():
    nombre_archivo = 'planilla5.txt'
    filas = [] # Lista para almacenar las filas del documento
    try:
        with open(nombre_archivo, 'r') as archivo: # Abrir el archivo en modo lectura
            contents = archivo.read() 
            print(contents)
            for linea in archivo: # Leer cada línea del archivo
                fila = linea.strip("\n") # Eliminar el salto de línea al final de cada línea
                filas.append(fila) # Agregar la fila a la lista
        return filas
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None

def validador_IP(direccion_ip):
    try:
        ipaddress.ip_address(direccion_ip)
        return True
    except ValueError:
        return False

def generador_lista():# Solicitar al usuario que ingrese elementos
    while True:
        lista = []  # Crear una nueva lista vacía para cada iteración
        while True:
            i = 0
            zona = input("Ingrese nombre de la zona en que operan los dispositivos: "); i = i +1 #zona en la que trabajan los equipos
            dispositivo = input("Ingrese dispositivo que pertenece a la zona: "); i = i +1 #nombre del dispositivo
            interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X): "); i = i +1 #numero de interfaz
            while True:
                direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: "); #direccion ip de la interfaz
                if validador_IP(direccion_ip):
                    i = i +1
                    break
                else:
                    print("direccion ip invalida. Favor de ingresar un direccion ip valida.")
            while True:
                mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: "))#Mascara de red de la interfaz
                if mascara > 0 and mascara <= 32:
                    mascara = str(mascara)
                    i = i + 1 #Mascara de red de la interfaz 
                    break
                elif mascara <= 0 or mascara > 30:
                    print("La mascara de red ha sido ingresada erroneamente.")
            destino = input("Ingrese nombre del dispositvo de destino: "); i = i + 1 #destino de la interfaz o hacia donde llegará esa interfaz
            capa_jerarquica = input("Ingrese la capa jerarquica perteneciente al equipo: "); i = i +1 #jerarquia perteneciente al equipo
            servicio_adheridos = input("Ingrese los servicios que estan disponibles en el dispositivo: "); i = i +1 #servicios que estan configurados en el equipo
            protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: "); i = i +1 #protocolos de red que tiene configurado el equipo
            lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+"/"+mascara+"\t"+"\t"+destino+"\t"+capa_jerarquica+"\t"+"\t"+protocolos_de_red+"\t"+"\t"+servicio_adheridos+"\n"); i = i +1 #se agrega las variables a una lista
            if i == 10:
                break
        listas.append(lista)  # Agregar la lista actual a la matriz lista
        os.system("clear")
        while True:
            agregar = input("Desea agregar una nueva interfaz? (S/N) ") #se agrega interfaces adicionales del equipo en caso de tenerlas
            if agregar == "Si" or agregar == "si" or agregar == "SI" or agregar == "S" or agregar == "s":
                zona = ""
                dispositivo = "\t"
                interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X): "); i = i +1 #numero de interfaz
                while True:
                    direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: "); #direccion ip de la interfaz
                    if validador_IP(direccion_ip):
                        i = i +1
                        break
                    else:
                        print("direccion ip invalida. Favor de ingresar un direccion ip valida.")
                while True:
                    mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: "))#Mascara de red de la interfaz
                    if mascara >= 0 and mascara <= 32:
                        mascara = str(mascara)
                        break
                    elif mascara < 0 or mascara > 32:
                        print("La mascara de red ha sido ingresada erroneamente.")
                destino = input("Ingrese nombre del dispositvo de destino: ")
                capa_jerarquica ="\t"
                servicio_adheridos = "\t"
                protocolos_de_red = "\t"
                lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+"/"+mascara+"\t"+"\t"+destino+"\t"+capa_jerarquica+"\t"+"\t"+protocolos_de_red+"\t"+"\t"+servicio_adheridos+"\n") #agrega una lista de la interfaz configurada 
            elif agregar == "N" or agregar == "n" or agregar == "no" or agregar == "NO" or agregar == "No":
                break
        os.system("clear")
        continuar = input("¿Deseas crear otra lista? (s/n): ") #creamos otra lista para otro dispositivo.
        if continuar.lower() != "s":
            break

def reemplazar(nombre_archivo):
    def leer_documento_txt(nombre_archivo):
        filas = []  # Lista para almacenar las filas del documento
        try:
            with open(nombre_archivo, 'r') as archivo:  # Abrir el archivo en modo lectura
                for linea in archivo:  # Leer cada línea del archivo
                    fila = linea.strip("\n")  # Eliminar el salto de línea al final de cada línea
                    filas.append(fila)  # Agregar la fila a la lista
            return filas
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no existe.")
            return None
    def reemplazar_texto(filas, num_fila, texto_reemplazar):
        if num_fila < 1 or num_fila > len(filas):  # Verificar si el número de fila es válido
            print("Número de fila inválido.")
            return filas
        fila_actualizada = filas[num_fila - 1].replace(texto_buscar, texto_reemplazar)  # Realizar el reemplazo de texto en la fila seleccionada
        filas_actualizadas = filas.copy()  # Actualizar la lista de filas
        filas_actualizadas[num_fila - 1] = fila_actualizada
        return filas_actualizadas
    def guardar_documento_txt(nombre_archivo, filas):
        try:
            with open(nombre_archivo, 'w') as archivo:  # Abrir el archivo en modo escritura
                for fila in filas:  # Escribir cada fila en el archivo
                    archivo.write(fila + '\n')
            print(f"El documento se ha guardado en '{nombre_archivo}'.")
        except:
            print(f"No se pudo guardar el documento en '{nombre_archivo}'.")
    # Leer el documento y guardar las filas en una lista
    filas_documento = leer_documento_txt(nombre_archivo)
    if filas_documento:
        print("Contenido del documento:")  # Imprimir las filas del documento
        for i, fila in enumerate(filas_documento):
            print(f"{i+1}. {fila}")
        texto_buscar = str(input("Ingrese el parámetro a cambiar: "))
        num_fila = int(input("Ingrese el número de fila en el que desea realizar el reemplazo: "))  # Pedir al usuario el número de fila para reemplazar el texto
        if num_fila < 1 or num_fila > len(filas_documento):  # Verificar si el número de fila es válido
            print("Número de fila inválido.")
        else:
            texto_reemplazar = input("Ingrese el texto con el que desea reemplazar: ")  # Pedir al usuario el texto con el que desea reemplazar
            filas_actualizadas = reemplazar_texto(filas_documento, num_fila, texto_reemplazar)  # Realizar el reemplazo de texto en la fila seleccionada
            print("\nContenido del documento actualizado:")  # Imprimir las filas actualizadas
            for i, fila in enumerate(filas_actualizadas):
                print(f"{i+1}. {fila}")
            guardar_documento_txt(nombre_archivo, filas_actualizadas)  # Guardar el documento actualizado

nombre_archivo = 'BACKBONE.txt'
                
def menu():
    os.system("clear")
    print("--------------MENU-------------------")
    print("1. leer archivo backbone.txt")
    print("2. Agregar al archivo backbone.txt")
    print("3. Reemplazar Texto en archivo backbone.txt")
    print("4. Salir.")
    print("\n\n---------------------------------")

while True:
    menu()
    opc = int(input("Ingrese la opcion que desea realizar."))
    if opc == 1:
        leer_documento_txt()
    elif opc == 2:
        generador_lista()
        for i, lista in enumerate(listas): # Imprimir todas las listas creadas
            print("Lista", i + 1, ":", lista)
        with open(nombre_archivo, 'a') as archivo: #Guarda las listas en un archivo de texto.
            for fila in listas:
                for elements in fila:
                    archivo.write(elements)
    elif opc == 3:
        reemplazar(nombre_archivo)
    elif opc == 4:
        break