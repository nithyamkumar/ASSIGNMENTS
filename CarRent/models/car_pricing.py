class CarPricing:
    def __init__(self,car_id,price_per_hr,discount,currency='₹'):
        self.car_id = car_id
        self.price_per_hour = price_per_hr
        self.discount = discount
        self.currency = currency