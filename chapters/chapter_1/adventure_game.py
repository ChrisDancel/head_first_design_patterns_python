from abc import ABC, abstractmethod


# WEAPONS
class WeaponBehaviour(ABC):
    @abstractmethod
    def useWeapon(self):
        raise NotImplementedError


class KnifeBehaiour(WeaponBehaviour):
    def useWeapon(self):
        print('cutting with knife')


class AxeBehaiour(WeaponBehaviour):
    def useWeapon(self):
        print('chopping with an axe')


class SwordBehaiour(WeaponBehaviour):
    def useWeapon(self):
        print('swinging a sword')


class BowAndArrowBehaiour(WeaponBehaviour):
    def useWeapon(self):
        print('shooting an arrow')


# CHARACTER

class Character():

    def __init__(self):
        self.weaponBehaviour = None

    def setWeapon(self, weaponBehaviour):
        self.weaponBehaviour = weaponBehaviour

    def fight(self):
        return self.weaponBehaviour.useWeapon()


class Queen(Character):

    def __init__(self):
        self.weaponBehaviour = None

    def display(self):
        print('I am the queen')


class King(Character):

    def __init__(self):
        self.weaponBehaviour = None

    def display(self):
        print('I am the King')


class Knight(Character):

    def __init__(self):
        self.weaponBehaviour = None

    def display(self):
        print('I am the Knight')


class Troll(Character):

    def __init__(self):
        self.weaponBehaviour = None

    def display(self):
        print('I am the Troll')


if __name__ == '__main__':
    knight = Knight()
    knight.display()
    knight.setWeapon(SwordBehaiour())
    knight.fight()
    knight.setWeapon(AxeBehaiour())
    knight.fight()
    knight.setWeapon(BowAndArrowBehaiour())
    knight.fight()
