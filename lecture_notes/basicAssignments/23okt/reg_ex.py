import re
 
#2018-10-23 - python webscraping:
# https://github.com/datsoftlyngby/dat4sem2018fall-python/blob/master/lecture_notes/18-Web%20Scraping%20Basics.ipynb
# http://kultunaut.dk/
print("hello")
 
myfile = open("addresses.txt", encoding="utf-8").read()
 
phone_num_reg = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
telefon = phone_num_reg.findall(myfile)
# find alle telefonnumre (i en liste)
#print(telefon)
 
navn_reg = re.compile(r"\d{2} \d{2} \d{2} \d{2}\n{2}(.*)\n", re.M)
navne = navn_reg.findall(myfile)
#printer alle navne
#print(navne)
 
#zip codes
zip_reg = re.compile(r"^\d{4}", re.M)
zipcodes = zip_reg.findall(myfile)
#print(zipcodes)
 
#city names with zipcodes
city_reg = re.compile(r"(^\d{4} \w+)", re.M)
cities = city_reg.findall(myfile)
#print(cities)
 
#streetnames
street_reg = re.compile(r"^(\D\S+) \d+", re.M)
streets = street_reg.findall(myfile)
print(streets)
 
 
# fejl:
# street with zipcodes
streetWcodes_reg = re.compile(r"(^\w*).*\n(^\d{4})", re.M)
streetsWzip = streetWcodes_reg.findall(myfile)
#print(streetsWzip)
 
#end