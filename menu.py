from clases import *
import os

if (os.name == 'nt'):
    borrar = 'cls'
else:
    borrar = 'clear'

usuario_iniciado = Usuario()
billetera = Aplicacion()

flag_aplicacion_iniciada = True
while flag_aplicacion_iniciada:
    os.system(borrar)
    
    print(
        '---------------------------------------'
        '\nBienvenid@! Inicie sesion o registrese.'
        '\n1.Iniciar sesion.'
        '\n2.Registrarse.'
        '\n3.Salir.'
        '\n---------------------------------------'
    )
    opc = int(input('Ingrese una opcion: '))
    os.system(borrar)

    if opc == 1:
        while True:

            if usuario_iniciado.iniciar_sesion():
                os.system(borrar)
                input(
                    'Inicio de sesion correcto.\n '
                    'Presione ENTER para continuar.'
                )

                flag_usuario_inciado = True

                while flag_usuario_inciado:
                    os.system(borrar)
                    print(
                        '--------------------------'
                        '\n1.Cargar dinero.'
                        '\n2.Hacer transferencia.'
                        '\n3.Pagar.'
                        '\n4.Ver datos.'
                        '\n5.Actualizar datos.'
                        '\n6.Cerrar sesion.'
                        '\n7.Cerrar aplicacion.'
                        '\n--------------------------'
                    )

                    opc = int(input('Ingrese una opcion: '))

                    if opc == 1:
                        os.system(borrar)
                        billetera.cargar_dinero(usuario_iniciado)

                    elif opc == 2:
                        os.system(borrar)
                        billetera.hacer_transferencia(usuario_iniciado.username)

                    elif opc == 3:
                        os.system(borrar)
                        billetera.pagar(usuario_iniciado.username)

                    elif opc == 4:
                        os.system(borrar)
                        usuario_iniciado.mostrar_datos()
                        input('\nPresione ENTER para continuar.')

                    elif opc == 5:
                        os.system(borrar)
                        usuario_iniciado.actualizar_datos_usuario()

                    elif opc == 6:
                        usuario_iniciado.cerrar_sesion()
                        flag_usuario_inciado = False
                        continue

                    elif opc == 7:
                        flag_aplicacion_iniciada = False
                        break

            else:
                os.system(borrar)
                print('Usuario/contrasenia incorrectos.\n')
                continue

            break

    elif opc == 2:
        usuario_iniciado.crear_usuario()
        os.system(borrar)

    elif opc == 3:
        break

    else:
        print('Ingrese una opcion correcta.')


#dmatiaszurita@gmail.com