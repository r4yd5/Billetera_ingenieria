"""
Aplicacion billetera virtual.

Obejtivos principales:
Disenar una aplicacion que siga la logica de una billetera virtual.

Funcioniones principales:
- Registro/Login de usuarios.
- Validacion del correo electronio por medio de un codigo de verificacion.
- Recarga de dinero.
- Transferencias a otros usuarios.
- Pagar por medio de la billetera.

"""

from interfaces import *
from funciones_varias import *
import json
import os


class Aplicacion(IAplicacion):

    def hacer_transferencia(self, user) -> None:

        with open('JSON/db.json', 'r') as db:
            data = json.load(db)

        db.close()
        while True:

            alias_cvu = input('ingrese ALIAS o CVU. No ingrese NADA para cancelar: ')
            os.system('cls')
            if alias_cvu == '':
                return
            for usuario_transferir in data:
                if (data[usuario_transferir]['alias'] == alias_cvu or data[usuario_transferir]['cvu'] == alias_cvu):

                    print(
                        'Le estas a punto de transferir a:\n'
                        '---------------------------------\n'
                        f'ALIAS: {data[usuario_transferir]["alias"]}\n'
                        f'CVU: {data[usuario_transferir]["cvu"]}\n'
                        f'Nombre: {data[usuario_transferir]["nombre"]}\n'
                        f'Apellido: {data[usuario_transferir]["apellido"]}\n'
                        f'DNI: {data[usuario_transferir]["dni"]}\n'
                        '---------------------------------'
                    )

                    while True:
                        decision = input('Seguro que quiere transferir? (s/n): ')
                        if decision == 's':
                            os.system('cls')
                            print('Ingrese el monto a transferir: ')
                            monto = validar_monto(True,user)
                            data[usuario_transferir]['dinero'] += monto
                            data[user]['dinero'] -= monto
                            input('\nTransferencia hecha con exito. Presione ENTER para continuar.')
                            os.system('cls')
                            break

                        elif decision == 'n':
                            return

                        else:
                            print('Ingrese una opcion valida.')

                    with open("JSON/db.json", "w") as db:
                        json.dump(data, db)
                        flag_transferencia = True

                    db.close()

                else:
                    flag_transferencia = False

            if flag_transferencia:
                break

            else:
                print('Ingrese un CVU o ALIAS valido.\n')

    def cargar_dinero(self, user) -> None:

        with open("JSON/db.json", "r") as db:
            data = json.load(db)

        db.close()

        print('Ingrese el monto a cargar (Minimo 1, Maximo 10000):')
        data[user.username]['dinero'] += validar_monto()


        with open("JSON/db.json", "w") as db:
            json.dump(data, db)

        db.close()

        input('\nMonto cargado con exito. Presione ENTER para continuar.')
        os.system('cls')

    def pagar(self, user) -> None:

        with open('JSON/db.json', 'r') as db:
            data = json.load(db)

        print('Ingrese el monto que desea pagar:')
        monto_pagar = validar_monto(True, user)
        data[user]['dinero'] -= monto_pagar
        
        with open('JSON/db.json', 'w') as db:
            json.dump(data, db)

        db.close()

        input('\nMonto cargado con exito. Presione ENTER para continuar.')
        os.system('cls')

class Usuario(IUsuario):

    username = ''
    password = ''

    def crear_usuario(self) -> None:
        while True:

            username = input('Ingrese username: ')
            contenido_db = {
                username: {
                    'dinero': 0,
                    'alias': random_alias(username),
                    'cvu': random_cvu(username),
                    'password': input('Ingrese una contrasenia: '),
                    'nombre': input('Ingrese nombre: '),
                    'apellido': input('Ingrese apellido: '),
                    'email': input('Ingrese email: '),
                    'tel': input('Ingrese tel: '),
                    'dni': input('Ingrese dni: ')
                }
            }

            os.system('cls')
            if es_valido(contenido_db, username):
                if validar_cuenta_con_mail(contenido_db[username]['email']):
                    break
                else:
                    return


        with open('JSON/db.json', 'r+') as archivo:
            data = json.load(archivo)
            data.update(contenido_db)
            archivo.seek(0)
            json.dump(data, archivo)
            archivo.close()

    def iniciar_sesion(self) -> bool:

        self.username = input('Ingrese username: ')
        self.password = input('Ingrese contrasenia: ')

        return validar_inicio_sesion(self.username, self.password)

    def mostrar_datos(self) -> None:

        db = open('JSON/db.json', 'r')
        contenido = json.load(db)

        print(
            f'Dinero: {contenido[self.username]["dinero"]}\n'
            f'ALIAS: {contenido[self.username]["alias"]}\n'
            f'CVU: {contenido[self.username]["cvu"]}\n'
            f'Username: {self.username}\n'
            f'Nombre: {contenido[self.username]["nombre"]}\n'
            f'Apellido: {contenido[self.username]["apellido"]}\n'
            f'Email: {contenido[self.username]["email"]}\n'
            f'Telefeno: {contenido[self.username]["tel"]}\n'
            f'DNI: {contenido[self.username]["dni"]}'
        )

        db.close()

    def actualizar_datos_usuario(self) -> None:

        with open("JSON/db.json", "r") as db:
            contenido = json.load(db)

        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        telefono = input('Telefono: ')

        validar_actualizar_datos(
            self.username, nombre, apellido, telefono, contenido)

        with open("JSON/db.json", "w") as db:
            json.dump(contenido, db)

        db.close()

    def cerrar_sesion(self) -> None:

        self.username = ''
        self.password = ''
