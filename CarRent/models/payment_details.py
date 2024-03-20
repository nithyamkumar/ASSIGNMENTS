import uuid 
class PaymentDetails:
    def __init__(self,total_amount,payment_mode='CARD', id = str(uuid.uuid4())):
        self.payment_id = id
        self.payment_mode = payment_mode
        self.total_amount = total_amount