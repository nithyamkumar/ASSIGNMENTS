import models.constants as cnst

class CarModel:
    def __init__(self,name:str,make:cnst.Make,category:cnst.CarCategory,
                 transmission_type: cnst.TransmissionType,no_of_seats:int,id:int):
        self.id = id
        self.name = name
        self.category = category
        self.transmission_type = transmission_type
        self.no_of_seats = no_of_seats
        self.make = make