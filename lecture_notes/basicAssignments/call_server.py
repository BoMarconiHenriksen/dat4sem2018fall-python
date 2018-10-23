import requests
from time import sleep
from random import randint

while True:
    response = requests.get('http://10.50.137.11:5000/')
    sleep(randint(1, 4))
