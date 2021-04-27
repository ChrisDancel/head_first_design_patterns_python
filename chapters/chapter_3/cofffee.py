from abc import ABC, abstractmethod


class Beverage(ABC):

    def __init__(self):
        self.description = 'unknown beverage'
        self.size = 'TALL'

    @abstractmethod
    def getDescription(self):
        raise NotImplementedError

    @abstractmethod
    def cost(self):
        raise NotImplementedError

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size


class CondimentDecorator(Beverage):

    def getDescription(self):
        raise NotImplementedError

    def cost(self):
        raise NotImplementedError

    def getSize(self):
        raise NotImplementedError


class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self.description = 'Espresso'

    def getDescription(self):
        return self.description

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        super().__init__()
        self.description = 'House Blend Coffee'

    def getDescription(self):
        return self.description

    def cost(self):
        return 0.89


class DarkRoast(Beverage):

    def __init__(self):
        super().__init__()
        self.description = 'Dark Roast'

    def getDescription(self):
        return self.description

    def cost(self):
        return 0.99


class Decaf(Beverage):

    def __init__(self):
        super().__init__()
        self.description = 'Decaf'

    def getDescription(self):
        return self.description

    def cost(self):
        return 1.05


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Mocha'

    def cost(self):
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Soy'

    def cost(self):

        size_mapper = {'TALL': 0.10,
                       'GRANDE': 0.15,
                       'VENTI': 0.20}

        return self.beverage.cost() + size_mapper[self.beverage.getSize()]


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Whip'

    def cost(self):
        return self.beverage.cost() + 0.10


if __name__ == '__main__':
    beverage = Espresso()
    print(beverage.getDescription() + ' $' + str(beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.getDescription() + ' $' + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3.setSize('TALL')
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.getDescription() + ' $' + str(beverage3.cost()))


