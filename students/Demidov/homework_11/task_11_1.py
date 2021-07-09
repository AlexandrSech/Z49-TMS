class Car:
    from accessify import protected

    brand: str
    series: str
    car_id: int
    model: str
    year: int
    power: int
    price: int
    mileage: int

    def __init__(self, brand, series, car_id, model, year, power, price, mileage):
        
        self.brand = brand
        self.__series = series
        self.__car_id = car_id
        self.model = model
        self.year = year
        self.power = power
        self.price = price
        self.mileage = mileage

    @protected # import protected class from accessify
    def get_brand_model(self):
        return f'Company: {self.brand}; Model - {self.year}'

    def get_model_year_mileage(self): # get ordinary values
        return f'Model: {self.model}; Created in {self.year}; Mileage: {self.mileage}'

    def setter_series(self, series, car_id): # set protected values
        if (isinstance(series, str)) and (isinstance(car_id, int) or isinstance(car_id, float)):
            self.__series = series
            self.__car_id = car_id
        else:
            print("series must be string and id must be an integer")

    def getter_series(self): # get protected values
        return f'Series: {self.__series}, ID: {self.__car_id}'

    def setter_model(self, model): # set ordinary values
        self.model = model

    def getter_model(self): # get ordinary values
        return f'Model name is {self.model}'


x5 = Car('BMW', 'X-series', 4, 'X5', 2013, 330, 19000, 70000)


print(x5.get_model_year_mileage())

# setters initializing
x5.setter_series("X", 10)
x5.setter_model("X7")


# call getter methods
print(x5.getter_series())
print(x5.getter_model())


class Animal:

  domen: str
  kingdom: str
  type: str
  classs: str
  order: str
  family: str
  view: str

  def init(self, name, domen, kingdom, type, classs, order, family, view):
    self.name = name
    self.domen = domen
    self.kingdom = kingdom
    self.type = type
    self.classs = classs
    self.order = order
    self.family = family
    self.view = view

  def get_name(self):
    return f'Name is {self.name}'

  def get_domen(self): # simple getter
    return f'Domen is: {self.domen}'

  def get_kingdom(self): # simple getter
    return f'Kingdom is: {self.kingdom}'


  def get_type(self): # simple getter
    return f'Type is: {self.type}'


  def get_classs(self): # simple getter
    return f'Class is: {self.classs}'


  def get_order(self): # simple getter
    return f'Order is: {self.order}'


  def get_family(self): # simple getter
    return f'Family is: {self.family}'


  def get_view(self): # simple getter
    return f'View is: {self.view}'


lion = Animal("Lion", "Eukaryotes", "Animalia", "Chordal", "Mammals", "Predatory", "Feline", "Lion")

print(lion.dict)