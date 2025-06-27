usuarios = {}

def validar_nombre(nombre):
    return nombre not in usuarios

def validar_sexo(sexo):
    return sexo.upper() in ['F', 'M']

def validar_contraseña(contraseña):
    tiene_letra = any(c.isalpha() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    sin_espacios = ' ' not in contraseña
    return len(contraseña) >= 8 and tiene_letra and tiene_numero and sin_espacios

def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    if not validar_nombre(nombre):
        print("El nombre de usuario ya existe!")
        return

    sexo = input("Ingrese sexo (F/M): ").upper()
    if not validar_sexo(sexo):
        print("Sexo inválido! Solo se permite F o M.")
        return

    contraseña = input("Ingrese contraseña: ")
    if not validar_contraseña(contraseña):
        print("Contraseña inválida!!! Debe tener al menos 8 caracteres, una letra, un número y sin espacios.")
        return

    usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}
    print("¡Usuario ingresado exitosamente!")

def buscar_usuario():
    nombre = input("Ingrese el nombre de usuario a buscar: ")
    if nombre in usuarios:
        print(f"Sexo: {usuarios[nombre]['sexo']}")
        print(f"Contraseña: {usuarios[nombre]['contraseña']}")
    else:
        print("Usuario no se encuentra.")

def eliminar_usuario():
    nombre = input("Ingrese el nombre de usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado!")
    else:
        print("No se pudo eliminar usuario!")

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ingresar_usuario()
        elif opcion == '2':
            buscar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            print("Programa terminado.")
            break
        else:
            print("Debe seleccionar una opción válida.")

if __name__ == "__main__":
    main()
    