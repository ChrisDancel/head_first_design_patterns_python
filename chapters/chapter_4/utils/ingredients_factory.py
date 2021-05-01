from abc import ABC, abstractmethod


class PizzaIngredientFactory(ABC):

    def __init__(self):
        self.Dough = None
        self.Sauce = None
        self.Cheese = None
        self.Veggies = []
        self.Pepperoni = None
        self.Clams = None

    @abstractmethod
    def createDough(self):
        raise NotImplementedError

    @abstractmethod
    def createSauce(self):
        raise NotImplementedError

    @abstractmethod
    def createCheese(self):
        raise NotImplementedError

    @abstractmethod
    def createVeggies(self):
        raise NotImplementedError

    @abstractmethod
    def createPepperoni(self):
        raise NotImplementedError

    @abstractmethod
    def createClam(self):
        raise NotImplementedError


class ThinCrustDough(object):
    pass


class MarinaraSauce(object):
    pass


class ReggianoCheese(object):
    pass


class Garlic(object):
    pass


class Onion(object):
    pass


class Mushroom(object):
    pass


class RedPepper(object):
    pass


class SlicedPepperoni(object):
    pass


class FreshClams(object):
    pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super().__init__()

    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return ReggianoCheese()

    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FreshClams()


class ThickCrustDough(object):
    pass


class PlumTomatoSauce(object):
    pass


class MozarellaCheese(object):
    pass


class Spinach(object):
    pass


class Eggplant(object):
    pass


class BlackOlives(object):
    pass


class FrozenClams(object):
    pass


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super().__init__()

    def createDough(self):
        return ThickCrustDough()

    def createSauce(self):
        return PlumTomatoSauce()

    def createCheese(self):
        return MozarellaCheese()

    def createVeggies(self):
        veggies = [Spinach(), Eggplant(), BlackOlives()]
        return veggies

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FrozenClams()


class BBQSauce(object):
    pass


class CaliforniaPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super().__init__()

    def createDough(self):
        return ThickCrustDough()

    def createSauce(self):
        return BBQSauce()

    def createCheese(self):
        return MozarellaCheese()

    def createVeggies(self):
        veggies = [Spinach(), Eggplant(), BlackOlives()]
        return veggies

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FrozenClams()

