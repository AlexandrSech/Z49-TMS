class ZeroException(Exception):
    def __init__(self, text):
        print('ZeroException')
        super().__init__(text)



class DigitException(Exception):
    def __init__(self, text):
        print('DigitException')
        super().__init__(text)


class OperationException(Exception):
    def __init__(self, text):
        print('OperationException')
        super().__init__(text)
