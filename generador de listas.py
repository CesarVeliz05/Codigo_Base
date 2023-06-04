# Crear una lista vacía para almacenar las listas de elementos
listas = []
matriz = ["Zona","\t","Dispositivo","\t","Interfaz","\t","IP","\t","\t","Capa Jerarquica","\t","Servicios de RED","\n"]#encabezado de la documentacion
listas.append(matriz)
# Solicitar al usuario que ingrese elementos
while True:
    lista = []  # Crear una nueva lista vacía para cada iteración
    while True:
        i = 0
        zona = input("Ingrese nombre de la zona en que operan los dispositivos: "); i = i +1 #zona en la que trabajan los equipos
        dispositivo = input("Ingrese dispositivo que pertenece a la zona: "); i = i +1 #nombre del dispositivo
        interfaz = input("Ingrese la interfaz conectada: "); i = i +1 #numero de interfaz
        direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: "); i = i +1 #direccion ip de la interfaz
        capa_jerarquica = input("Ingrese la capa jerarquica perteneciente al equipo: "); i = i +1 #jerarquia perteneciente al equipo
        servicio_adheridos = input("Ingrese los servicios que estan disponibles en el dispositivo: "); i = i +1 #servicios que estan configurados en el equipo
        lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+capa_jerarquica+"\t"+servicio_adheridos+"\n"); i = i +1 #se agrega las variables a una lista
        if i == 7:
            break
        dispositivo_aux = dispositivo
    listas.append(lista)  # Agregar la lista actual a la matriz lista
    while True:
        agregar = input("Desea agregar una nueva interfaz?: ") #se agrega interfaces adicionales del equipo en caso de tenerlas
        if agregar == "Si" or agregar == "si" or agregar == "SI":
            zona = ""
            dispositivo = "\t"
            interfaz = input("Ingrese la interfaz conectada: ") #se ingresa la otra interfaz configurada con direccion ip
            direccion_ip = input("Ingrese la direccion ip de la interfaz antes mencionada: ") #la direccion ip de la interfaz configurada
            capa_jerarquica ="\t"
            servicio_adheridos = "\t"
            lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+capa_jerarquica+"\t"+servicio_adheridos+"\n") #agrega una lista de la interfaz configurada 
        elif agregar == "no" or agregar == "NO" or agregar == "No":
            break
    continuar = input("¿Deseas crear otra lista? (s/n): ") #creamos otra lista para otro dispositivo.
    if continuar.lower() != "s":
        break

for i, lista in enumerate(listas): # Imprimir todas las listas creadas
    print("Lista", i + 1, ":", lista)

with open('planilla5.txt', 'w') as archivo: #Guarda las listas en un archivo de texto.
    for fila in listas:
        for elements in fila:
            archivo.write(elements)