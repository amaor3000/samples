def foo(x: int, y: int) -> int:
    return x + y

def inner_function():
    return

foo(4,5)

class Bar:
    def __init__(self, value: int, DAMN: int):
        self.value = value
        self.member_dummy = 5 + self.get_value()
        Local_dummy = foo(self.value, DAMN)
        print (Local_dummy)

    def get_value(self) -> int:
        def inner_function():
            return foo(4,5)
        
        inner_function()
        return self.value

Bar(2, 5)