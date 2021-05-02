# the getInstance method is static, meaning that the class does not need to be instantiated
# first before being used. getInstance wraps and returns access to the private inner class _ChcolateBoiler that contains
# all metadata beloning to the state of ChocolateBoiler i.e. empty or boiled.

# In the example below, we explicitly get reference to the getInstance() class twice. After some modification to the
# first chocolate boiler, we can also see that the changes are identical to what the second chocolate boiler has in
# that their ids are completely identical.

# Disclaimer: had to get some help on this exercise by looking at for inspiration
# https://github.com/jtortorelli/head-first-design-patterns-python/blob/master/src/python/chapter_5/chocolate_boiler.py


class ChocolateBoiler:
    instance = None

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if not ChocolateBoiler.instance:
            ChocolateBoiler.instance = ChocolateBoiler._ChocolateBoiler()
        return ChocolateBoiler.instance

    class _ChocolateBoiler:

        def __init__(self):
            self.empty = True
            self.boiled = False

        def fill(self):
            if self.empty:
                self.empty = False
                self.boiled = False

        def drain(self):
            if not self.empty and self.boiled:
                self.empty = True

        def boil(self):
            if not self.empty and not self.boiled:
                self.boiled = True

        def status(self):
            print(f'empty: {self.empty}, boiled: {self.boiled}')


def main():
    cb1 = ChocolateBoiler.getInstance()
    cb2 = ChocolateBoiler.getInstance()

    print(f'id of cb1 {id(cb1)}')
    print('filling boiler...')
    cb1.fill()
    cb1.status()
    print('boiling boiler...')
    cb1.boil()
    cb1.status()
    print(f'id of cb2 {id(cb2)}')
    cb2.status()


if __name__ == '__main__':
    main()
