import funciones as fn

pedido=[]

while True:
    try:
   
        print("BIENVENIDO A --PaquExpress--")
        print("1. Registrar pedidos: ")
        print("2. Listar los todos los pedidos: ")
        print("3. Imprimir hoja de ruta: ")
        print("4. Salir del programa: ")

        opcion=int(input("Seleccione una opcion (1-4): "))

        if opcion == 1:
            fn.registrarPedido(pedido)
        elif opcion ==2:
            fn.listarPedido()
        elif opcion ==3:
            fn.imprimirRuta()
        elif opcion ==4:
            print("Salir")
            break
    except:
        print("ingrese opcion vàlida 1-4 ")   