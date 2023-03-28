class Person_name:
    def __init__(self, Name, Age, Height):
        self.Name = Name
        self.Age = Age
        self.Height = Height

    def person_intro(self):
        print(f'His/Her name is {self.Name}, he/she is {self.Age} years old and he/she is {self.Height} tall')

    def person(self):
        return self.Name

for_Satya = Person_name('Satya','23',"5'6")
for_Sush = Person_name('Sushma','24',"5'2")

for_Satya.person_intro()
for_Sush.person_intro()