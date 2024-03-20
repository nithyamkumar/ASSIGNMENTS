from models.car_model import CarModel

class Car:
    def __init__(self,id:int,name:str,model_id:int,manufacture_year):
        self.id = id
        self.name = name
        self.model = model_id
        self.manufacture_year = manufacture_year