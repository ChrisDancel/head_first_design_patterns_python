from utils import pizza_inventory as pi
from utils import store_inventory as si

print(' ----- The Factor Method Pattern ----- \n')


# for previous reference
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
            raise (f'pizza type {type} is invalid')


def main():
    nyStore = si.NYStylePizzaStore()
    chicagoStore = si.ChicagoStylePizzaStore()
    californiaStore = si.CaliforniaStylePizzaStore()

    pizza = nyStore.orderPizza('cheese')
    print(f'Ethan ordered a {pizza.getName()}\n')

    pizza = chicagoStore.orderPizza('cheese')
    print(f'Joel ordered a {pizza.getName()}\n')

    pizza = californiaStore.orderPizza('cheese')
    print(f'Chris ordered a {pizza.getName()}\n')


if __name__ == '__main__':
    main()
