class PartyAnimal:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name,'Constructor')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count',self.x)


s = PartyAnimal('Abc')
s.party()

j = PartyAnimal('Def')
j.party()
s.party()