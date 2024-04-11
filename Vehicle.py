class Vehicle():
    def __init__(self, pavadinimas, Rida):
        self.newPavadinimas = pavadinimas
        self.rida = Rida
        

    def getRida(self):
        return self.rida
    
    def getPavadinimas(self,pavadinimas):
        self.newPavadinimas = pavadinimas
        
    
   
    
# z = Vehicle('Mazda', 3500.20)
# print(z.getPavadinimas(), z.getRida())

# #Sukurkite išvestines klases Car, Bus, Train, kurie paveldėtų viską iš Vehicle, 
# ir papildomai būtų galima nurodyti Seats - sėdimų vietų skaičių, 
# ir visi turėtų metoda GetSeats() grąžinantį tekstą: <Pavadinimas> turi <Seats> sėdimų vietų.

class Car(Vehicle):
    def __init__(self, pavadinimas, Rida, seats):
        super().__init__(pavadinimas, Rida,)
        self.NewSeats = int(seats)

    def getSeats(self):
        return print(f'{self.newPavadinimas} turi vietu:' + f' {self.NewSeats}')
    
    def changer(self, pavadinimas, seats):
        self.newPavadinimas = pavadinimas
        self.NewSeats = seats

class Bus(Vehicle):
    def __init__(self, pavadinimas, Rida, seats):
        super().__init__(pavadinimas, Rida)
        self.NewSeats = int(seats)

    def getSeats(self):
        return print(f'{self.newPavadinimas} turi vietu:' + f' {self.NewSeats}')
    
    def changer(self, pavadinimas, seats):
        self.newPavadinimas = pavadinimas
        self.NewSeats = seats

class Train(Vehicle):
    def __init__(self, pavadinimas, Rida, seats):
        super().__init__(pavadinimas, Rida)
        self.NewSeats = seats = int(seats)

    def getSeats(self):
        return f'{self.newPavadinimas} turi vietu:' + f' {self.NewSeats}'
    
    def changer(self, pavadinimas, seats):
        self.newPavadinimas = pavadinimas
        self.NewSeats = seats
    
z = Bus('Mercedez', 35556, 32)
h = Car('Honda', 111110, 5)
t = Car('BulletTrain', 9000, 653)

z.getSeats()
h.getSeats()
t.getSeats()
