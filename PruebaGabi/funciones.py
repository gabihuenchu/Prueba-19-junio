#registrarPedido():
#ListarPedidos
#Imprimir hoja de ruta
#direccion= input("Ingrese nombre y apellido del cliente: ")
#sector= input("Ingrese secotr del cliente (centro,norte,sur): ")
#detallePed= input("Ingrese detalle del paquete pedido (pequeño/mediano/grande): ")

#datos=[{"Cliente": nombreApellido,
#"Direcciòn": direccion,
#"Sector":sector,
#"Paquetes": detallePed
#}]

sectores=['centro','norte','sur']

def registrarPedido(pedido):
    #servirìa para validar que exista espacio entre ambas palabras.
    while nombreApellido is not "":
        print("ingrese nombre y apellido nuevamente")
    nombreApellido= input("Ingrese nombre y apellido del cliente: ").lower()
    
    direccion=input("Ingrese direccion del cliente: ").lower()
    sector= input("Ingrese secotr del cliente (centro,norte,sur): ").lower()
    detallePed= input("Ingrese detalle del paquete pedido (pequeño/mediano/grande): ").lower()


    


def listarPedido():
    datos=[{
    "Cliente": nombreApellido,
    "Direcciòn": direccion,
    "Sector":sector,
    "Paquetes": detallePed
    }]

def imprimirRuta():
    #aqui habrìa que exportar a txt, pero no me acuerdo del orden sintaxico del formato...
    with open nombreArchivo ("w"):
        nombreArchivo.write(f"sector,{sectores}"\n)



