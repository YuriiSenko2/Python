class Train:
    def __init__(self, train_type, route):
        self.type = train_type
        self.route = route
        self.wagons = dict()

    def __len__(self):
        return len(self.wagons)

    def __setitem__(self, key, value):
        self.wagons[key] = value

    def __getitem__(self, item):
        return self.wagons[item]


class Wagon:
    def __init__(self, wagon_type, accommodation):
        self.type = wagon_type
        self.accommodation = accommodation
        self.passengers = dict()

    def __len__(self):
        return len(self.passengers)

    def __setitem__(self, key, value):
        self.passengers[key] = value

    def __getitem__(self, item):
        return self.passengers[item]


class Passengers:
    def __init__(self, place, name, terminal):
        self.place = place
        self.name = name
        self.terminal = terminal

    def __str__(self):
        return f'place: {self.place},\nname: {self.name},\ndestination: {self.terminal}\n'


train = Train('Express', 'Kharkiv - Lviv')

wagon1 = Wagon('Luxury', 20)
pass1 = Passengers(1, 'Andrii', 'Cherkassy')
wagon1[1] = pass1
pass2 = Passengers(5, 'Taras', 'Dnipro')
wagon1[5] = pass2
train[1] = wagon1

wagon2 = Wagon('Mid-range', 50)
pass3 = Passengers(25, 'Anatoliy', 'Kyiv')
wagon2[25] = pass3
pass4 = Passengers(6, 'Ihor', 'Lviv')
wagon2[6] = pass4
pass5 = Passengers(38, 'Nazar', 'Lviv')
wagon2[38] = pass5
train[2] = wagon2

wagon3 = Wagon('Economy', 100)
pass6 = Passengers(77, 'Fedir', 'Poltava')
wagon3[77] = pass6
train[3] = wagon3

print(wagon1[1])
print(wagon2[6])
print(wagon3[77])
print(len(wagon1))
print(len(wagon2))
print(len(wagon3))
print(len(train))



