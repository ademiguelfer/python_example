#PRACTICA FINAL
from gestion import anadir_cancion, listar_canciones, eliminar_cancion, modificar_cancion

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
        anadir_cancion(lista_canciones)
    elif opcion == 2:
        listar_canciones(lista_canciones)
    elif opcion == 3:
        eliminar_cancion(lista_canciones)
    elif opcion == 4:
        modificar_cancion(lista_canciones)
    elif opcion == 5:
        print("Ha seleccionado salir")
    else:
        print("Opción no válida.")

