import string, random
# Se crea lista con 10 futuros usuarios
usuarios = ['Administrador', 'Empresa Te Lo Vendo', 'Empresa Fenix', 'Francisco', 'Felipe', 'Nombre3', 'Nombre4', 'Nombre5', 'Nombre6', 'Nombre7']

# Se recorre la lista
for usuario in usuarios:
    print(usuario)


def generar_cuenta():
    """Función para generar cuenta de los usuarios"""
    for idx, usuario in enumerate(usuarios):
        usuarios[idx] = {'username': usuario, 'contraseña': generar_contraseña(), 'telefono': solicitar_telefono(usuario)}

def generar_contraseña():
    """Función para generar contraseña para usuarios"""
    caracteres = string.ascii_letters + string.digits

    while True:
        contraseña = ''
        for i in range(12):
            contraseña += ''.join(random.choice(caracteres))
        
        if not any(caracter.isupper() for caracter in contraseña): continue
        if not any(caracter.islower() for caracter in contraseña): continue
        if not any(caracter.isdigit() for caracter in contraseña): continue

        break

    return contraseña

def solicitar_telefono(nombre_usuario):
    while True:
        telefono = input(f"\nIngresar número de teléfono del usuario {nombre_usuario}: ")
        if sum(c.isdigit() for c in telefono) >= 8: break
        print("El número debe contener al menos 8 dígitos")
    return telefono

generar_cuenta()

for usuario in usuarios:
    print(f"usuario: {usuario['username']}, contraseña: {usuario['contraseña']}, teléfono: {usuario['telefono']}")
