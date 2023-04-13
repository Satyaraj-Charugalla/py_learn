# We are creating a clas named foodie
class foodie:
    # A constructor (__init__) is used to assign the values
    def __init__(self,colur,fruitname):
        self.colur = colur
        self.fruitname= fruitname
    # A function that is defined in a class is called a method
    # The method here will print out the name and colour of the fruit
    def show(self):
    # The word self is an instance to access all the attributes in the class
        print(f'Fruit name is "{self.fruitname}" and its colur is "{self.colur.lower()}"')

fru_mango = foodie('Yellow','Mango')
fru_avacado = foodie('Green','Avacado')

fru_mango.show()
fru_avacado.show()