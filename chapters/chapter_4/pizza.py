from abc import ABC, abstractmethod
from utils import pizza_inventory as pi


class SimplePizzaFactory:

    def createPizza(self, type):

        pizza_selector = {'cheese': pi.CheesePizza(),
                          'pepperoni': pi.PepperoniPizza(),
                          'clam': pi.ClamPizza(),
                          'veggie': pi.VeggiePizza()}
        # return pizza_selector.get(type)

        try:
            return pizza_selector[type]
        except KeyError:
            raise(f'pizza type {type} is invalid')


class PizzaStore:

    def __init__(self):
        self.pizzaFactory = SimplePizzaFactory()

    def orderPizza(self, type):

        pizza = self.pizzaFactory.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


if __name__ == '__main__':

    # order from factory
    pizzaFactory = SimplePizzaFactory()
    pizza = pizzaFactory.createPizza('cheese')

    # order from store
    pizzaStore = PizzaStore()
    orderedPizza = pizzaStore.orderPizza('cheese')
    print(f'Ordered pizza: {orderedPizza.type}')


