class PartyAnimal:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name,'Constructor')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count',self.x)

class footballfan(PartyAnimal):
    points = 0
    def goal(self):
        self.points = self.points + 5
        self.party()
        print(self.name,'points',self.points)

s = PartyAnimal('Abc')
s.party()

j = footballfan('Def')
j.party()
j.goal()