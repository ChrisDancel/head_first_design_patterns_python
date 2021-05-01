from abc import ABC, abstractmethod


# NOTE - not making Pizza class as an ABC as we want subclasses to inherent current print messages that are linked
# to each method


class Pizza:

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None
        self.toppings = []
        self.ingredientsFactory = None

    @abstractmethod
    def prepare(self):
        raise NotImplementedError
        # print(f'Preparing {self.name}')
        # print(f'Tossing dough......')
        # print(f'Adding sauce')
        # print(f'Adding toppings {str(self.toppings)}...')

    def bake(self):
        print('Bake for 25 min at 350C')

    def cut(self):
        print('Cutting the pizza into diagonol slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredientsFactory.createDough()
        self.sauce = self.ingredientsFactory.createSauce()
        self.cheese = self.ingredientsFactory.createCheese()


class CheesePizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'cheese'
        self.ingredientsFactory = ingredientsFactory


class PepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'pepperoni'


class ClamPizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'clam'
        self.ingredientsFactory = ingredientsFactory


class VeggiePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'veggie'


class NYStyleCheesePizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.type = 'NYStyleCheesePizza'
        self.name = 'NY style sauce and cheese pizza'
        self.dough = 'thin crust dough'
        self.sauce = 'marina sauce'
        self.toppings = ['grated regiano cheese']
        self.ingredientsFactory = ingredientsFactory


class NYStylePepperoniPizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'NYStylePepperoni'
        self.ingredientsFactory = ingredientsFactory


class NYStyleClamPizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'NYStyleClamPizza'
        self.ingredientsFactory = ingredientsFactory



class NYStyleVeggiePizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'NYStyleVeggie'
        self.ingredientsFactory = ingredientsFactory


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'chiciago style deep dish cheese pizza'
        self.dough = 'extra thick crust dough'
        self.sauce = 'plum tomato sauce'
        self.toppings = ['shredded mozzarella cheese']
        self.ingredientsFactory = ingredientsFactory


class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'ChicagoStylePepperoni'
        self.ingredientsFactory = ingredientsFactory


class ChicagoStyleClamPizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'ChicagoStyleClamPizza'
        self.ingredientsFactory = ingredientsFactory


class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'ChicagoStyleVeggie'
        self.ingredientsFactory = ingredientsFactory


class CaliforniaStyleCheesePizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'CaliforniaStyleCheesePizza'
        self.dough = 'extra thick crust dough'
        self.sauce = 'plum tomato sauce'
        self.toppings = ['pieapples']
        self.ingredientsFactory = ingredientsFactory


class CaliforniaStylePepperoniPizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'CaliforniaStylePepperoni'
        self.ingredientsFactory = ingredientsFactory


class CaliforniaStyleClamPizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'CaliforniaStyleClamPizza'
        self.ingredientsFactory = ingredientsFactory


class CaliforniaStyleVeggiePizza(Pizza):

    def __init__(self, ingredientsFactory):
        super().__init__()
        self.name = 'CaliforniaStyleVeggie'
        self.ingredientsFactory = ingredientsFactory
