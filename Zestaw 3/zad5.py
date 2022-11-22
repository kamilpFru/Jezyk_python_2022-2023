class Bug:

    licznik = 0

    def __init__(self):
        '''Konstruktor zwiekszajacy licznik o 1 i przypisujacy go do id obiektu'''
        Bug.licznik += 1
        self.id = Bug.licznik

    def __del__(self):
        '''Destruktor zmniejszajacy licznik o 1 oraz wypisujacy licznik i id obiektu'''
        print("Koniec licznik: " + self.__str__())
        Bug.licznik -= 1
        del self

    def __str__(self):
        '''Funkcja zwracajaca stan obiektu'''
        return "Licznik: " + str(Bug.licznik) + " ID: " + str(self.id)

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])


