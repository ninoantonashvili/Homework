class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand=None, model=None, year=None):
        self._brand = None
        self._model = None
        self._year = None
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def set_brand(self, brand):
        #tu brendi stringi araa, amoagdos error
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError("Brand must be a string")

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        #tu modeli stringi araa amoagdos erori
        if isinstance(model, str):
            self._model = model
        else:
            raise ValueError("Model must be a string")

    def get_model(self):
        return self._model

    def set_year(self, year):
        #tu wli intejeri araa amoagdos erori
        if isinstance(year, int):
            self._year = year
        else:
            raise ValueError("Year must be an integer")

    def get_year(self):
        return self._year