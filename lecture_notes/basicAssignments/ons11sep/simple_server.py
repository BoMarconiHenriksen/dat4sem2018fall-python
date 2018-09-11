from flask import Flask


# initieren af en klasse. __name__ er navnet på promgrammet simple_server
my_app = Flask(__name__)

#class Name(_SuperType) # Svarer til extend. _ betyder det er en privat klasse.
#class Ui: # En almindlig klasse
#    def __init__(self): # Konstruktør
#        self.my_info = 5 # Attribut
    #def ui(self): # Self skal altid med svarer til this.
 #       print('ui')

@my_app.route('/')  # Bliver kørt inde eller efter def hello()
def hello():
#    return 'Hello World'
    new_msg_creator = Ui
    #return new_msg_creator.ui()
    return new_msg_creator.my_info = 1000

@my_app.route('/read/<pages>')
def read_books(pages):
    print(pages)
    return pages
    # opg. læse moby og skriv linjer ud fra linje som du skriver 

if __name__ == '__main__':
    my_app.run()  # metode kald da run er en del Flask.
#    main() #funktions kald
