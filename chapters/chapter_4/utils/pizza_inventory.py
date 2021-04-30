from abc import ABC, abstractmethod

# NOTE - not making Pizza class as an ABC as we want subclasses to inherent current print messages that are linked
# to each method


class Pizza:

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f'Preparing {self.name}')
        print(f'Tossing dough......')
        print(f'Adding sauce')
        print(f'Adding toppings {str(self.toppings)}...')

    def bake(self):
        print('Bake for 25 min at 350C')

    def cut(self):
        print('Cutting the pizza into diagonol slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def getName(self):
        return self.name


class CheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'cheese'


class PepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'pepperoni'


class ClamPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'clam'


class VeggiePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'veggie'


class NYStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.type = 'NYStyleCheesePizza'
        self.name = 'NY style sauce and cheese pizza'
        self.dough = 'thin crust dough'
        self.sauce = 'marina sauce'
        self.toppings = ['grated regiano cheese']


class NYStylePepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'NYStylePepperoni'


class NYStyleClamPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'NYStyleClamPizza'


class NYStyleVeggiePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'NYStyleVeggie'


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'chiciago style deep dish cheese pizza'
        self.dough = 'extra thick crust dough'
        self.sauce = 'plum tomato sauce'
        self.toppings = ['shredded mozzarella cheese']


class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'ChicagoStylePepperoni'


class ChicagoStyleClamPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'ChicagoStyleClamPizza'


class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'ChicagoStyleVeggie'


class CaliforniaStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'CaliforniaStyleCheesePizza'
        self.dough = 'extra thick crust dough'
        self.sauce = 'plum tomato sauce'
        self.toppings = ['pieapples']

class CaliforniaStylePepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'CaliforniaStylePepperoni'


class CaliforniaStyleClamPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'CaliforniaStyleClamPizza'


class CaliforniaStyleVeggiePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'CaliforniaStyleVeggie'

