import json
import random

db = open('codigo_verificacion.json', 'r')
data = json.load(db)

random_index = random.randint(1, 1000)
codigo = data[random_index]['code']


