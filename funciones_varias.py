import json
import re
import random
import os
import smtplib
from email.message import EmailMessage

def es_valido(user,username) -> bool:
    c = 0
    caracteres = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM'

    #Si usuario esta en db
    
    db = open('db.json', 'r')
    contenido=json.load(db)
    
    if username in contenido:
        print('El nombre de usuario ya esta en uso, prueba con otro.')
        c += 1
        db.close()
    
    #Validacion contrasenia mayor 8 caracteres
    if len(user[username]['password']) < 9:
        print('La contrasenia debe contener mas de 8 caracteres.')
        c += 1
    
    #validacion contrasenia numerica
    for i in (user[username]['password']):

        if i not in caracteres:
            if i == len(user[username]['password']):
                c += 1
                print('La contrasenia no puede contener solo numeros.')
        else: 
            break

    #Validacion contrasenia contiene mayuscula
    cc = 0
    for i in user[username]['password']:
        cc += 1
        try:
            i = int(i)
        except:
            pass
        if type(i) == str:
            if i == i.upper():
                break
        else:
            pass
        if cc == len(user[username]['password']):
            c += 1
            print('La contrasenia debe contener al menos una mayuscula.')

    #Validar email
    def es_correo_valido(correo):                
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular, correo) is not None



    if es_correo_valido(user[username]['email']):
        pass
    else:
        print('Ingrese un formato de email valido.')
        c += 1


    if c == 0:
        return True
    else:
        return False
         
def validar_inicio_sesion(username, password) -> bool:

    db = open('db.json', 'r')
    contenido=json.load(db)


    if username in contenido and password == contenido[username]['password']:
        db.close()  
        return True
    else:
        db.close()      
        return False

def random_alias(username) -> str:

    with open('alias.json') as alias:
        data = json.load(alias)

    
        random_index = random.randint(0, 1000-1)
        contenido_random = data[random_index]
        alias_random = contenido_random['first'] + '.' + contenido_random['medium'] + '.' + contenido_random['last'] 

        alias.close()
    
    return alias_random


def random_cvu(username) -> int:
    with open('cvu.json') as cvu:
        data = json.load(cvu)

    random_index = random.randint(0, 1000-1)
    cvu_random = data[random_index]['cvu']

    cvu.close()

    return cvu_random


def validar_actualizar_datos(user, nom, ape, tel, data):

        if nom != '':
            data[user]['nombre'] = nom

        if ape != '':
            data[user]['apellido'] = ape

        if tel != '':
            data[user]['tel'] = tel

def validar_monto(para_transferir=False,user=None):

    while True:
        if para_transferir:
            
            with open('db.json', 'r') as db:
                data = json.load(db)

            print(f'Dinero en la cuenta: {data[user]["dinero"]}')
            monto = float(input())

            if data[user]['dinero'] >= monto and monto > 0 and monto <= 10000:
                return monto
                break
            else:
                os.system('clear')
                print('Monto invalido.')

            db.close()

        else:
            monto = float(input())

            if monto and monto > 0 and monto <= 10000:
                return monto
                break
            else:
                print('Monto invalido.')


def validar_cuenta_con_mail(correo):
    try:
        db = open('codigo_verificacion.json', 'r')
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
            verificar_codigo = input('Ingrese el codigo de verificacion que le llego a su Email: ')
            if verificar_codigo == codigo:
                print('Codigo correcto.')
                break
            elif vericar_codigo == '':
                print('Codigo incorrecto. Vuelva a introducirlo')
    except:
        print('Correo no valido. Cuenta no creada.')
"""
cap 5
administracion de la responsabilidad y la etica
responsabilidad social
obligacion sensibilidad y responsabilidad
administracion verde y sustentabilidad
evaluaciones de las administrativas verdes (no)
los gerentes y el comportamiento etico (no)
etica en un contexto internacional (140 libro cuadro) - intensidad del problema etico
principios del pacto mundial de la onu

cap 6 toma de deciones
el proceso de la toma de decisiones - 8 pasos 
la toma de decisiones gerenciales - racionalidad, racionalidad limititada, toma de decisiones intituiva (fasetas intucion)
tipos de decsiones y condiciones para la toma de decsiones
pag 174- cuadro proceso toma de deciones
"""

