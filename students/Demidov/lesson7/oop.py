class House():
    length: int
    width: int
    height: int

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return self.length

    def __str__(self) -> str:
        return f'width - {self.width}, length - {self.length}, height - {self.height}'


office = House(100, 40, 76)

print(office.__str__())

