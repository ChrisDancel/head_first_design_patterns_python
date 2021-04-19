from abc import ABC, abstractmethod

# FLYING BEHAVIOUR

class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print('I can fly')


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print('cannot fly')


class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print('I\'m flying with a rocket!')


# QUACK BEHAVIOUR


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehaviour):
    def quack(self):
        print('quack quack')


class Squeek(QuackBehaviour):
    def quack(self):
        print('squeek squeek')


class MuteQuack(QuackBehaviour):
    def quack(self):
        print('<< silence >>')

# DUCK TYPES


class Duck(ABC):

    def __init__(self):
        self.quackBehaviour = None
        self.flyBehaviour = None

    def setFlyBehaviour(self, flyBehaviour):
        self.flyBehaviour = flyBehaviour

    def setQuackBehaviour(self, quackBehaviour):
        self.quackBehaviour = quackBehaviour

    def performQuack(self):
        return self.quackBehaviour.quack()

    def performFly(self):
        return self.flyBehaviour.fly()


class MallardDuck(Duck):

    def __init__(self):
        self.quackBehaviour = Quack()
        self.flyBehaviour = FlyWithWings()

    @staticmethod
    def display():
        print('I am a Mallard')


class ModelDuck(Duck):
    def __init__(self):
        self.quackBehaviour = None
        self.flyBehaviour = None

    @staticmethod
    def display():
        print('I am a model duck')


class DuckWhistle(QuackBehaviour):

    def __init__(self):
        self.quackBehaviour = Quack()

    def quack(self):
        return self.quackBehaviour.quack()

    def display(self):
        print('Duck Whistle')


if __name__ == '__main__':

    comments = """
    The Strategy Pattern defines a family of algorithms, 
    encapsulates each one, and makes them interchangeable.
    Strategy lets to algorithm vary independently from 
    clients that use it. 
    """
    print(comments + '\n')

    Mallard = MallardDuck()
    Mallard.performQuack()
    Mallard.performFly()
    Mallard.display()

    print('\n ----------- \n')

    model_duck = ModelDuck()
    model_duck.setFlyBehaviour(FlyNoWay())
    model_duck.setQuackBehaviour(Quack())
    model_duck.performQuack()
    model_duck.performFly()
    model_duck.display()

    print('\n ----------- \n')

    model_duck2 = ModelDuck()
    model_duck2.setFlyBehaviour(FlyNoWay())
    model_duck2.performFly()
    model_duck2.setFlyBehaviour(FlyRocketPowered())
    model_duck2.performFly()
    model_duck2.display()

    print('\n ----------- \n')
    duck_whistle = DuckWhistle()
    duck_whistle.display()
    duck_whistle.quack()