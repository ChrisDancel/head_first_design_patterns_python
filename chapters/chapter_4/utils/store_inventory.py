from abc import ABC, abstractmethod
from utils import pizza_inventory as pi


class PizzaStore(ABC):

    @abstractmethod
    def createPizza(self, x):
        raise NotImplementedError

    @abstractmethod
    def orderPizza(self, x):
        raise NotImplementedError


class NYStylePizzaStore(PizzaStore):

    def __init__(self):
        self.description = 'NY Pizza Store'

    def createPizza(self, type):
        pizza_selector = {'cheese': pi.NYStyleCheesePizza(),
                          'pepperoni': pi.NYStylePepperoniPizza(),
                          'clam': pi.NYStyleClamPizza(),
                          'veggie': pi.NYStyleVeggiePizza()}
        try:
            return pizza_selector[type]
        except KeyError:
            raise(f'pizza type {type} is invalid')

    def orderPizza(self, type):

        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoStylePizzaStore(PizzaStore):

    def __init__(self):
        self.description = 'Chicago Pizza Store'

    def createPizza(self, type):
        pizza_selector = {'cheese': pi.ChicagoStyleCheesePizza(),
                          'pepperoni': pi.ChicagoStylePepperoniPizza(),
                          'clam': pi.ChicagoStyleClamPizza(),
                          'veggie': pi.ChicagoStyleVeggiePizza()}
        try:
            return pizza_selector[type]
        except KeyError:
            raise(f'pizza type {type} is invalid')

    def orderPizza(self, type):

        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class CaliforniaStylePizzaStore(PizzaStore):

    def __init__(self):
        self.description = 'California Pizza Store'

    def createPizza(self, type):
        pizza_selector = {'cheese': pi.CaliforniaStyleCheesePizza(),
                          'pepperoni': pi.CaliforniaStylePepperoniPizza(),
                          'clam': pi.CaliforniaStyleClamPizza(),
                          'veggie': pi.CaliforniaStyleVeggiePizza()}
        try:
            return pizza_selector[type]
        except KeyError:
            raise(f'pizza type {type} is invalid')

    def orderPizza(self, type):

        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
