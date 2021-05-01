from abc import ABC, abstractmethod
from utils import pizza_inventory as pi
from utils import ingredients_factory as ifa


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
        self.ingredientsFactory = ifa.NYPizzaIngredientFactory()
        self.pizza = None

    def createPizza(self, type):
        pizza_selector = {'cheese': pi.NYStyleCheesePizza(self.ingredientsFactory),
                          'pepperoni': pi.NYStylePepperoniPizza(self.ingredientsFactory),
                          'clam': pi.NYStyleClamPizza(self.ingredientsFactory),
                          'veggie': pi.NYStyleVeggiePizza(self.ingredientsFactory)}
        try:
            self.pizza = pizza_selector[type]
            self.pizza.setName(f'New York style {type} pizza')
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
        self.ingredientsFactory = ifa.ChicagoPizzaIngredientFactory()
        self.pizza = None

    def createPizza(self, type):
        pizza_selector = {'cheese': pi.ChicagoStyleCheesePizza(self.ingredientsFactory),
                          'pepperoni': pi.ChicagoStylePepperoniPizza(self.ingredientsFactory),
                          'clam': pi.ChicagoStyleClamPizza(self.ingredientsFactory),
                          'veggie': pi.ChicagoStyleVeggiePizza(self.ingredientsFactory)}
        try:
            self.pizza = pizza_selector[type]
            self.pizza.setName(f'Chicago style {type} pizza')
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
        self.ingredientsFactory = ifa.CaliforniaPizzaIngredientFactory()
        self.pizza = None

    def createPizza(self, type):
        pizza_selector = {'cheese': pi.CaliforniaStyleCheesePizza(self.ingredientsFactory),
                          'pepperoni': pi.CaliforniaStylePepperoniPizza(self.ingredientsFactory),
                          'clam': pi.CaliforniaStyleClamPizza(self.ingredientsFactory),
                          'veggie': pi.CaliforniaStyleVeggiePizza(self.ingredientsFactory)}
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
