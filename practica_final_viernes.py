#PRACTICA FINAL
print("MP3")
print("----------------------")
lista_canciones = [
    ["Dance the Night", "Dua Lipa", 180,"Dance","*****"],
    ["Bzrp Music Session Vol 53", "Shakira", 240, "Urban Latino","***"],
    ["Bizcochito", "Rosalia", 200, "Urban Latino","**"],
    ["Nochentera", "Vicco", 200, "Pop","*****"]
]
# print (lista_canciones)


# titulo = input(" Introduce el título de la canción: ")
# interprete = input(" Introduce el interprete de la canción: ")
# duracion_segundos = int (input(" Introduce la duración de la canción en segundos: "))
#estilo_musical = input(" Introduce el estilo musical de la canción en segundos: ")
# calificacion = input(" Introduce la Calificación de la canción con asteriscos de 1 a 5. Un asterisco es la calificación más baja y 5 asteriscos la más alta: ")
# nueva_cancion = [titulo, interprete, duracion_segundos, estilo_musical,calificacion]

# lista_canciones.append(nueva_cancion)
# print (lista_canciones)

opcion = 0
listar = 0

estilo_musical = ""

while opcion != 5:
    print("MENU DE OPCIONES")
    print("1 - Añadir")
    print("2 - Listar")
    print("3 - Eliminar")
    print("4 - Modificar")
    print("5 - Salir")

    opcion = int(input("Introduzca la opción que desee: "))

    if opcion == 1:
        print("Ha seleccionado Añadir una canción.")
        titulo = input(" Introduce el título de la canción: ")
        interprete = input(" Introduce el interprete de la canción: ")
        duracion_segundos = int(input(" Introduce la duración de la canción en segundos: "))
        estilo_musical = input(" Introduce el estilo musical de la canción en segundos: ")
        calificacion = input(" Introduce la calificación de la canción con asteriscos de 1 a 5. Un asterisco es la calificación más baja y 5 asteriscos la más alta: ")
        nueva_cancion = [titulo, interprete, duracion_segundos, estilo_musical, calificacion]
        lista_canciones.append(nueva_cancion)
        print("Canción añadida correctamente.")
        for cancion in lista_canciones:
            print("titulo: ", cancion[0])
            print("interprete: ", cancion [1])
            print("duracion_segundos: ", cancion [2])
            print("estilo_musical: ", cancion[3])
            print("calificación: ", cancion[4])
           # print (nueva_cancion)
            print("--------------------------")

    elif opcion == 2:
        print("Ha seleccionado listar")

        while listar != 4:
            print("OPCIONES")
            print("1. - ESTILOS")
            print("2. - CANCIONES")
            print("3. - TODO")
            print("4. - SALIR")

            listar = int(input("Introduzca la opción que desee: "))
            if listar == 1:
                # Estilos: Se mostrará un listado de las canciones de un estilo seleccionado por el
                # usuario. Se mostrará de esta forma
                print("Ha seleccionado Listar por estilos")
                estilo = (input("Seleccione un estilo musical: "))
                print(estilo)
                encontrado_estilo = False
                for cancion in lista_canciones:
                    if estilo == cancion[3]:
                        print("------------")
                        print(cancion[0])
                        print(cancion[1])

                        encontrado_estilo == True
                if encontrado_estilo == False:
                        print("No hay más canciones con ese estilo musical.")
                        break
            elif listar == 2:
                print("Ha seleccionado listar por intérprete")
                cantante = (input("Seleccione un intérprete: "))
                print(cantante)
                print("------------------")
                encontrada_cancion = False
                for cancion in lista_canciones:
                    if cantante == cancion [1]:
                        print(cancion [0])
                        print("--------------")
                if encontrada_cancion == False:
                        print("No hay canciones de ese intérprete.")
                        break


            elif listar == 3:
                print("LISTAR TODO")
                print("-------------")
                # segundos = 0
                # minutos_enteros = segundos // 60
                # segundos_residuales = segundos % 60


                for cancion in lista_canciones:
                    print("Canción: ", cancion [0])
                    print("Interprete: ", cancion [1])
                    #los minutos
                    print("Duración: ", cancion [2], "minutos")
                    print("Estilo: ", cancion [3])
                    print("Calificación: ", cancion [4])
                    print("-------------------------")


            else:
                 break

    elif opcion == 3:
        print ("Ha seleccionado eliminar canción por título")

        lista_canciones = [
            ["Dance the Night", "Dua Lipa", 180, "Dance", "*****"],
            ["Bzrp Music Session Vol 53", "Shakira", 240, "Urban Latino", "***"],
            ["Bizcochito", "Rosalia", 200, "Urban Latino", "**"],
            ["Nochentera", "Vicco", 200, "Pop", "*****"]
        ]

        # Solicita al usuario el título de la canción a eliminar
        cancion_a_eliminar = input("Introduce el título de la canción que deseas eliminar: ")

        # Busca y elimina la canción de la lista
        cancion_encontrada = False
        for cancion in lista_canciones:
            if cancion[0] == cancion_a_eliminar:
                lista_canciones.remove(cancion)
                cancion_encontrada = True
                print ("La canción ", cancion_a_eliminar, " ha sido eliminada.")
                break

        if not cancion_encontrada:
            print("La canción", cancion_a_eliminar, "no se encuentra en la lista.")

        # Mostrar la lista actualizada
        print("Lista actualizada de canciones:")
        for cancion in lista_canciones:
            print(cancion)

    elif opcion == 4:
        #modificar la informacion de una cancion seleccionada
        print ("Ha seleccionado Modificar la información de una canción seleccionada.")

        lista_canciones = [
        ["Dance the Night", "Dua Lipa", 180, "Dance", "*****"],
        ["Bzrp Music Session Vol 53", "Shakira", 240, "Urban Latino", "***"],
        ["Bizcochito", "Rosalia", 200, "Urban Latino", "**"],
        ["Nochentera", "Vicco", 200, "Pop", "*****"]
    ]

        # Solicita al usuario el título de la canción a modificar
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

        #else:
            #print ("va a salir")

           #break
if opcion ==5:
    print ("Ha seleccionado salir")


if opcion > 5:
    print ("opción no válida. Seleccione otra opción del menu: ")
