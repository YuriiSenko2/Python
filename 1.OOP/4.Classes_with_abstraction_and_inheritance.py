from abc import ABC, abstractmethod


class Skoda(ABC):
    def __init__(self):
        self.model = None
        self.release_year = None
        self.color = None
        self.price = None

    @abstractmethod
    def from_dollar_converter(self):
        """Calculation formula will be here"""

    @abstractmethod
    def salon_address(self):
        """The address of the salon will be here"""

    @abstractmethod
    def salon_number(self):
        """The number of the salon will be here"""


class Octavia(Skoda):
    def __init__(self):
        super().__init__()
        self.model = 'Octavia'
        self.release_year = 2023
        self.color = 'White'
        self.price = 30000

    def from_dollar_converter(self):
        return self.price * 40

    def salon_address(self):
        print('Address: Klochkivska 188')

    def salon_number(self):
        print('Phone: +380930000004')


class Superb(Skoda):
    def __init__(self):
        super().__init__()
        self.model = 'Superb'
        self.release_year = 2015
        self.color = 'Black'
        self.price = 15000

    def from_dollar_converter(self):
        return self.price * 40

    def salon_address(self):
        print('Adrress: Bilogorska 92B')

    def salon_number(self):
        print('Phone: +380930000005')


class KharkivAddresses(Superb, Octavia):
    def locations(self):
        return Superb.salon_address(self), Superb.salon_number(self), \
               Octavia.salon_address(self), Octavia.salon_number(self)


skoda_map = KharkivAddresses()
skoda_map.locations()








