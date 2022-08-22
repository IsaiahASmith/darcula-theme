# pylint: disable-all

def decorator():
    pass


def argued_decorator(arg):
    pass


class A:
    @decorator
    def meth(self):
        pass

    @argued_decorator(int, 100, 'test', enumerate)
    def meth2(cls, test=5):
        pass

    @staticmethod
    def test():
        pass

    @classmethod
    def test(cls):
        meth2(test=5)


@decorator
@argued_decorator(int, 100, 'test', enumerate)
def function():
    pass
