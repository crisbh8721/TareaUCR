import json
DATA_FILE = "biblioteca.json"
def load_libros():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # si el archivo no existe,retorne una lista vacia o data inicial
        return [
            {"Titulo": "La sombra del viento", "Autor": "Carlos Ruiz Zafón", "Año": 2001, "ISBN": "978-84-829975-2"},
            {"Titulo": "Rayuela", "Autor": "Julio Cortázar", "Año": 1963, "ISBN": "978-84-6631905-8"},
            {"Titulo": "Pedro Páramo", "Autor": "Juan Rulfo", "Año": 1955, "ISBN": "978-80-216093-5"},
        ]
    except json.JSONDecodeError:
        # si el archivo no es formato json
        print("Error: No se pudo decodificar la informacion del archivo")
        return [
            {"Titulo": "La sombra del viento", "Autor": "Carlos Ruiz Zafón", "Año": 2001, "ISBN": "978-84-829975-2"},
            {"Titulo": "Rayuela", "Autor": "Julio Cortázar", "Año": 1963, "ISBN": "978-84-6631905-8"},
            {"Titulo": "Pedro Páramo", "Autor": "Juan Rulfo", "Año": 1955, "ISBN": "978-80-216093-5"},
        ]

def save_libros(libros_data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(libros_data, f, indent=4, ensure_ascii=False)

def display_libros(libros_data):
    print("_" * 50)
    if not libros_data:
        print("No hay libros en la  Bibilioteca")
        return
    for i,libro in enumerate(libros_data):
        print(f'{i+1}.Tilulo: {libro['Titulo']}, Autor: {libro['Autor']},Año: {libro['Año']}, ISBN: {libro['ISBN']}')
    print("_"*50)

def add_libro(libros_data):
    print("_" * 50)
    Titulo = input("Ingrese el Titulo del libro: ")
    Autor = input("Ingrese el Autor del libro: ")
    while True:
        try:
            Año = int(input("Ingrese el Año del libro: "))
            break
        except ValueError:
            print("Ingrese un Año en formato numeral")
    ISBN = input("Ingrese el ISBN del libro: ")
    nuevo_libro = {
        "Titulo": Titulo,
        "Autor": Autor,
        "Año": Año,
        "ISBN": ISBN
    }
    libros_data.append(nuevo_libro)
    save_libros(libros_data)
    print(f"'{Titulo}' ha sido añadido a la biblioteca")
    print("_" * 50)

def menu_modify_libro():
    print("_" * 50)
    print("Menu de Modificacion de Datos:")
    print("_" * 50)
    print("Datos disponibles para modificar ")
    print("1. Titulo.")
    print("2. Autor.")
    print("3. Año.")
    print("4. ISBN.")
    print("5. Salir.")
    print("_" * 50)

def modify_libro(libros_data):
    print("_" * 50)
    if not libros_data:
        print("No hay libros disponibles para modificar.")
        return
    display_libros(libros_data)
    try:
        index = int(input("Ingrese el número de libro a modificar: "))-1
        if 0 <= index < len(libros_data):
            libro = libros_data[index]
            print(f"\nModificando el libro número {index + 1}:")
            try:
                while True:
                    print(f"Título: {libro['Titulo']}, Autor: {libro['Autor']}, Año: {libro['Año']}, ISBN: {libro['ISBN']}")
                    menu_modify_libro()
                    seleccion_modify_libro = int(input("selecione una opcion (1-5)\n"))
                    if seleccion_modify_libro == 1:
                        print(f"Título: {libro['Titulo']}")
                        Titulo = input("Ingrese la modificacion al Titulo del libro: ")
                        libros_data[index].update({
                            "Titulo": Titulo,
                        })
                        print(f"Título Actualizado Correctamente")
                    elif seleccion_modify_libro == 2:
                        print(f"Título: {libro['Titulo']},Autor: {libro['Autor']}")
                        Autor = input("Ingrese la modificacion al Autor del libro: ")
                        libros_data[index].update({
                        "Autor": Autor,
                        })
                        print(f"Título Actualizado Correctamente")
                    elif seleccion_modify_libro == 3:
                        while True:
                            try:
                                print(f"Título: {libro['Titulo']},Año: {libro['Año']}")
                                Año = int(input("Ingrese la modificacion al Año del libro: "))
                                libros_data[index].update({
                                    "Año": Año,
                                })
                                print(f"Título Actualizado Correctamente")
                            except ValueError:
                                print("Ingrese un Año en formato numeral")
                    elif seleccion_modify_libro == 4:
                        print(f"Título: {libro['Titulo']},ISBN: {libro['ISBN']}")
                        ISBN = input("Ingrese la modificacion al ISBN del libro: ")
                        libros_data[index].update({
                            "ISBN": ISBN
                        })
                        print(f"Título Actualizado Correctamente")
                    elif seleccion_modify_libro == 5:
                        print("Saliendo del programa")
                        break
                    else:
                        print("Opcion incorrecta")
                    save_libros(libros_data)
                    print("_" * 50)
                else:
                    print("El número ingresado es inválido. Intente de nuevo.")
            except ValueError:
                print("Valor incorrecto, ingrese un número válido.")
    except ValueError:
          print("Valor incorrecto, ingrese un número válido.")
    print(f"'{Titulo}' ha sido actualizado a la biblioteca")
    print(f"Título: {libro['Titulo']}, Autor: {libro['Autor']}, Año: {libro['Año']}, ISBN: {libro['ISBN']}")
    print("_" * 50)

def delete_libro(libros_data):
    print("_" * 50)
    display_libros(libros_data)
    if not libros_data:
        return
    while True:
        try:
            index = int(input("Ingrese el número de libro a eliminar: \n"))
            if 0 <= index < len(libros_data):
                break
            else:
                print("El número es inválido, intente de nuevo")
        except ValueError:
            print("Valor incorrect1o, ingrese un número de la lista de libros")

    libro_eliminado = libros_data.pop(index-1)
    save_libros(libros_data)
    print(f"'{libro_eliminado['Titulo']}' ha sido eliminado de la biblioteca")
    print("_" * 50)

def main():
    libros = load_libros()
    while True:
        print("\n--- Menu de la Biblioteca ---")
        print("1. Ver todos los libros")
        print("2. Añadir un libro ")
        print("3. Modificar un libro")
        print("4. Eliminar un libro")
        print("5. Salir")
        selecion = int(input("selecione una opcion (1-5)\n"))
        try:
            while True:
                if selecion == 1:
                    display_libros(libros)
                    break
                elif selecion == 2:
                    add_libro(libros)
                    break
                elif selecion == 3:
                    modify_libro(libros)
                    break
                elif selecion == 4:
                    delete_libro(libros)
                    break
                elif selecion == 5:
                    print("Saliendo del programa")
                    break
                else:
                    print("Opcion incorrecta")
                    break
        except ValueError:
            print("Opcion incorrecta")

if __name__ == '__main__':
    main()



