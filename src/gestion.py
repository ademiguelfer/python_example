
def anadir_cancion(lista_canciones):
    print("Ha seleccionado Añadir una canción.")
    titulo = input(" Introduce el título de la canción: ")
    interprete = input(" Introduce el interprete de la canción: ")
    duracion_segundos = int(input(" Introduce la duración de la canción en segundos: "))
    estilo_musical = input(" Introduce el estilo musical de la canción: ")
    calificacion = input(" Introduce la calificación de la canción con asteriscos de 1 a 5. Un asterisco es la calificación más baja y 5 asteriscos la más alta: ")
    nueva_cancion = [titulo, interprete, duracion_segundos, estilo_musical, calificacion]
    lista_canciones.append(nueva_cancion)
    print("Canción añadida correctamente. ")
    for cancion in lista_canciones:
        print("titulo: ", cancion[0])
        print("interprete: ", cancion [1])
        print("duracion_segundos: ", cancion [2])
        print("estilo_musical: ", cancion[3])
        print("calificación: ", cancion[4])
        print("--------------------------")

def listar_canciones(lista_canciones):
    listar = 0
    while listar != 4:
        print("OPCIONES")
        print("1. - ESTILOS")
        print("2. - CANCIONES")
        print("3. - TODO")
        print("4. - SALIR")

        listar = int(input("Introduzca la opción que desee: "))
        if listar == 1:
            listar_por_estilo(lista_canciones)
        elif listar == 2:
            listar_por_interprete(lista_canciones)
        elif listar == 3:
            listar_todas(lista_canciones)
        elif listar != 4:
            print("Opción no válida.")

def listar_por_estilo(lista_canciones):
    print("Ha seleccionado Listar por estilos")
    estilo = input("Seleccione un estilo musical: ")
    encontrado_estilo = False
    for cancion in lista_canciones:
        if estilo == cancion[3]:
            print("------------")
            print(cancion[0])
            print(cancion[1])
            encontrado_estilo = True
    if not encontrado_estilo:
        print("No hay más canciones con ese estilo musical.")

def listar_por_interprete(lista_canciones):
    print("Ha seleccionado listar por intérprete")
    cantante = input("Seleccione un intérprete: ")
    print(cantante)
    print("------------------")
    encontrada_cancion = False
    for cancion in lista_canciones:
        if cantante == cancion [1]:
            print(cancion [0])
            print("--------------")
            encontrada_cancion = True
    if not encontrada_cancion:
        print("No hay canciones de ese intérprete.")

def listar_todas(lista_canciones):
    print("LISTAR TODO")
    print("-------------")
    for cancion in lista_canciones:
        print("Canción: ", cancion [0])
        print("Interprete: ", cancion [1])
        # los minutos
        print("Duración: ", cancion [2], "minutos")
        print("Estilo: ", cancion [3])
        print("Calificación: ", cancion [4])
        print("-------------------------")

def eliminar_cancion(lista_canciones):
    print ("Ha seleccionado eliminar canción por título")
    cancion_a_eliminar = input("Introduce el título de la canción que deseas eliminar: ")
    cancion_encontrada = False
    for cancion in lista_canciones:
        if cancion[0] == cancion_a_eliminar:
            lista_canciones.remove(cancion)
            cancion_encontrada = True
            print ("La canción ", cancion_a_eliminar, " ha sido eliminada.")
            break
    if not cancion_encontrada:
        print("La canción", cancion_a_eliminar, "no se encuentra en la lista.")
    print("Lista actualizada de canciones:")
    for cancion in lista_canciones:
        print(cancion)

def modificar_cancion(lista_canciones):
    print ("Ha seleccionado Modificar la información de una canción seleccionada.")
    titulo_a_modificar = input("Introduce el título de la canción que deseas modificar: ")
    cancion_encontrada = None
    for cancion in lista_canciones:
        if cancion[0] == titulo_a_modificar:
            cancion_encontrada = cancion
    if cancion_encontrada:
        print("¿Qué información deseas modificar?")
        print("1. Título")
        print("2. Artista")
        print("3. Duración")
        print("4. Género")
        print("5. Calificación")
        opcion = int(input("Elige una opción (1-5): "))
        if opcion == 1:
            nuevo_titulo = input("Introduce el nuevo título: ")
            cancion_encontrada[0] = nuevo_titulo
        elif opcion == 2:
            nuevo_artista = input("Introduce el nuevo artista: ")
            cancion_encontrada[1] = nuevo_artista
        elif opcion == 3:
            nueva_duracion = int(input("Introduce la nueva duración (en segundos): "))
            cancion_encontrada[2] = nueva_duracion
        elif opcion == 4:
            nuevo_genero = input("Introduce el nuevo género: ")
            cancion_encontrada[3] = nuevo_genero
        elif opcion == 5:
            nueva_calificacion = input("Introduce la nueva calificación: ")
            cancion_encontrada[4] = nueva_calificacion
        else:
            print("Opción no válida.")
        print("Información de la canción actualizada:")
        print(cancion_encontrada)
    else:
        print("La canción", titulo_a_modificar, "no se encuentra en la lista.")
