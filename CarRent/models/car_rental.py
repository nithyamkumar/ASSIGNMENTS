import uuid

class CarRental:
    def __init__(self,car_id,customer_id,rent_from,rent_to,rent_mode,payment_id = 0,is_returned = False):
        self.car_id = car_id
        self.customer_id = customer_id
        self.rent_from = rent_from
        self.rent_to = rent_to
        self.rent_mode = rent_mode
        self.payment_id = payment_id
        self.is_returned = is_returned
        self.id = str(uuid.uuid4())

        