def make_greeter(phrase):
    prefix = phrase + ', '
    def greeter(name):
        return prefix + name
    return greeter()
casual_greeter = make_greeter('Hello')