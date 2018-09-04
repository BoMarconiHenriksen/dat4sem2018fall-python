# import modul.
import random_name

# import kun en metode eller liste
from random_name import nouns

# Bruges ved lange filnavne
import random_name as ord
print(ord.nouns)

# Normalt tilgår man ikke de variabler
print(random_name.__file__)
print(random_name.__doc__)
print(random_name.__name__)

# Dokumentation:
# """ Dokumentation
#
# """

# Tilår liste element
random_name.nouns[5]

# Hvor mange elemter er der i listen
print(len(random_name.nouns))

# Giv mig en liste med elementerne fra 10 til 15 (15 er ikke med)
print(random_name.nouns[10:15])

# slice - længde hop
print(random_name.nouns[10:15:2])

# En omvendt liste
print(random_name.nouns[25:10:-1])

# Få sidste element eller -10 og det sidste 10 element
print(random_name.nouns[-1])

# fra start til 10. element
short_nouns = random_name.nouns[:10]
# Ændrer element i liste
short_nouns[0] = "mennesker"
print(short_nouns)

# Tuplets - Brug parentes i stet for  [ ]
my_tuplets = ('a', 1, 5.5)
# my_tuplets[-1] = 'aiaiaai' # Tupler kan ikke ændres.

first_element = my_tuplets[0]
sec_element = my_tuplets[1]
third_ele = my_tuplets[2]

# i stedet i python. Antal a elementer skal passe til elementerne
first_element, sec_element, third_ele = my_tuplets

# Strukturen skal matche. Det man ikke har brug for erstattes med _
first_element, sec_element, _ = my_tuplets

#
short_nouns = random_name.nouns[:10]
# Ændrer element i liste
short_nouns[0] = "mennesker"
short_nouns[-1] = "mennesker"
short_nouns[5] = "mennesker"

short_nouns = set[1, 2, 4]
print(short_nouns)

# dictionary
my_dict = {1: "ai", "two": "ui", 4.4: [1, 2, 3]}

# Hent element fra dict
print(my_dict["two"])

# Se  dictionarys keys - collections a keys
print(my_dict.keys())

# Se dictionarys values
print(my_dict.values())


