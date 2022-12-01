import json
import re
import random
import os
import smtplib
from email.message import EmailMessage

if (os.name == 'nt'):
    borrar = 'cls'
else:
    borrar = 'clear'


def es_valido(contenido,username) -> bool:
    count_errors = 0
    caracteres = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM'

    #Si usuario esta en db
    
    db = open('JSON/db.json', 'r')
    data=json.load(db)
    
    if username in data:
        print('El nombre de usuario ya esta en uso, prueba con otro.')
        count_errors += 1
        db.close()
    
    #Validacion contrasenia mayor 8 caracteres
    if len(contenido[username]['password']) < 9:
        print('La contrasenia debe contener mas de 8 caracteres.')
        count_errors += 1
    
    #validacion contrasenia numerica
    for i in (contenido[username]['password']):

        if i not in caracteres:
            if i == len(contenido[username]['password']):
                count_errors += 1
                print('La contrasenia no puede contener solo numeros.')
        else: 
            break

    #Validacion contrasenia contiene mayuscula
    char_password = 0
    for i in contenido[username]['password']:
        char_password += 1
        try:
            i = int(i)
        except:
            pass
        if type(i) == str:
            if i == i.upper():
                break
        else:
            pass
        if char_password == len(contenido[username]['password']):
            count_errors += 1
            print('La contrasenia debe contener al menos una mayuscula.')

    #Validar email
    def es_correo_valido(correo) -> bool:                
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular, correo) is not None

    if es_correo_valido(contenido[username]['email']):
        pass
    else:
        print('Ingrese un formato de email valido.')
        count_errors += 1

    #validar numero tel
    if len(contenido[username]['tel']) == 10 or len(contenido[username]['tel']) == 9:
        try:
            int(contenido[username]['tel'])
        except:
            count_errors += 1
            print('El numero de telefono no es valido.')
    else:
        count_errors += 1
        print('El numero de telefono no es valido.')

    #validar DNI
    if len(contenido[username]['dni']) == 8 or len(contenido[username]['dni']) == 7:
        try:
            int(contenido[username]['dni'])
        except:
            count_errors += 1
            print('El DNI no es valido.')
    else:
        count_errors += 1
        print('El DNI no es valido.')

    if count_errors == 0:
        return True
    else:
        print('\n')
        return False
         
def validar_inicio_sesion(username, password) -> bool:

    db = open('JSON/db.json', 'r')
    contenido=json.load(db)

    if username in contenido and password == contenido[username]['password']:
        db.close()  
        return True
    else:
        db.close()      
        return False

def random_alias(username) -> str:

    with open('JSON/alias.json') as alias:
        data = json.load(alias)

    
        random_index = random.randint(0, 1000-1)
        contenido_random = data[random_index]
        alias_random = contenido_random['first'] + '.' + contenido_random['medium'] + '.' + contenido_random['last'] 

        alias.close()
    
    return alias_random


def random_cvu(username) -> int:
    with open('JSON/cvu.json') as cvu:
        data = json.load(cvu)

    random_index = random.randint(0, 1000-1)
    cvu_random = data[random_index]['cvu']

    cvu.close()

    return cvu_random


def validar_actualizar_datos(user, nom, ape, tel, data) -> None:

        if nom != '':
            data[user]['nombre'] = nom

        if ape != '':
            data[user]['apellido'] = ape

        if tel != '':
            data[user]['tel'] = tel

def validar_monto(para_transferir=False,user=None) -> float:

    while True:
        if para_transferir:
            
            with open('JSON/db.json', 'r') as db:
                data = json.load(db)

            if (data[user]['dinero'] == 0):
                return 'No hay saldo en la cuenta.'

            print(f'Dinero en la cuenta: {data[user]["dinero"]}')
            monto = float(input('Ingrese el monto: '))

            if data[user]['dinero'] >= monto and monto > 0 and monto <= 10000:
                return monto
                break
            else:
                os.system(borrar)
                print('Monto invalido.')

            db.close()

        else:
            monto = float(input())

            if monto and monto > 0 and monto <= 10000:
                return monto
                break
            else:
                print('Monto invalido.')


def validar_cuenta_con_mail(correo) -> bool:
    
    try:
        db = open('JSON/codigo_verificacion.json', 'r')
        data = json.load(db)

        random_index = random.randint(1, 1000)
        codigo = data[random_index]['code']

        message = EmailMessage()
        email_subject = "Codigo de verificacion."
        message.set_content(f"Su codigo de verificacion es: {codigo}")

        sender_email_address = "cuenta.email.billetera@gmail.com"
        email_password = "hqhmxqahdunyuumo"

        receiver_email_address = correo
        email_smtp = "smtp.gmail.com"
        

        message['Subject'] = email_subject
        message['From'] = sender_email_address
        message['To'] = receiver_email_address

        server = smtplib.SMTP(email_smtp, '587')
        server.ehlo()
        server.starttls()

        server.login(sender_email_address, email_password)
        server.send_message(message)

        server.quit()
    
        while True:
            print(
                'Ingrese el codigo de verificacion que le llego a su Email.\n'
                'No introduzca nada para cancelar: '
            )
            verificar_codigo = input()
            if verificar_codigo == codigo:
                input('\nCuenta creada con exito. Pulse ENTER para continuar.')
                return True

            elif verificar_codigo == '':
                input('Operacion cancelada. Pulse ENTER para continuar.')
                os.system(borrar)
                return False

            else:
                os.system(borrar)
                print('Codigo incorrecto. Vuelva a introducirlo\n')

    except:
        print('Correo no valido. Cuenta no creada.')
        return False
