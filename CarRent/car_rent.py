from tabulate import tabulate
from models.payment_details import PaymentDetails
from models.car_rental import CarRental
from  models.feedback_details import Feedback
from models.customer_credential import CustomerCredential
from datetime import datetime
import data.proj_data as data
import data.session_data as sd
import pandas as pd
import utility
import data.string_constants as s
import models.constants as cst
import uuid


class CarRent:

    #Initiates the car rent process
    def rent_car(_self):
            print(s.WELCOME_MESSAGE)
            _self.__ask_login_credentials__()

    #Method that requests the login credentials
    def __ask_login_credentials__(_self):
        customer = []
        while not customer:
            e_usr_name = input(s.INP_USERNAME)
            e_pwd = input(s.INP_PASSWROD)
            customer = list(filter(lambda x:x.usr_name == e_usr_name and x.pwd == e_pwd, data.customerCredentialList))
        _self.__login__(customer[0].cust_id)

    #Sets the session customer id
    #Checks if the customer has a car to return, if yes then prompts car return message else continu with car rent process    
    def __login__(self,cust_id):
        sd.logged_in_cust_id = cust_id
        rent_car_data = list(filter(lambda x: x.customer_id == sd.logged_in_cust_id and x. is_returned == False , data.carRentalsData))
        if rent_car_data:
            print(s.RETURN_CAR)
            input(s.INP_SELECTION_3)
            self.__return_car__(rent_car_data[0])
        else:
            self.__get_date_preference__()
            self.__list_all_availabe_cars__()

    #Gets the preferred date of car rent
    def __get_date_preference__(self):
        print(s.RENT_DURATION)
        from_date = input(s.INP_DATE_FROM)
        from_date = utility.convert_to_datetime(from_date)
        while  from_date == None or from_date <= datetime.today():
            print(s.INCORRECT_INPUT)
            from_date = input(s.INP_DATE_FROM)
            from_date = utility.convert_to_datetime(from_date)

        to_date = input(s.INP_DATE_TO)
        to_date = utility.convert_to_datetime(to_date)
        while  to_date == None or to_date <= from_date:
            print(s.INCORRECT_INPUT)
            to_date = input(s.INP_DATE_TO)
            to_date = utility.convert_to_datetime(to_date)

        sd.request_from = from_date
        sd.request_to = to_date

    #List all the available cars for the preferred date range. If nothing available then displays message
    def __list_all_availabe_cars__(self):
        if not sd.available_cars:
            unavailable_cars = list(filter(lambda x: (sd.request_from <= utility.convert_to_datetime(x.rent_to,2) 
                                       or sd.request_to >= utility.convert_to_datetime(x.rent_to,2)) and x.is_returned == False,
                                       data.carRentalsData))
            car_ids = [i.car_id for i in unavailable_cars]
            sd.available_cars = list(filter(lambda x: x.id not in car_ids, data.carList))
        if sd.available_cars:
            car_data = [{'Id': x.id, 'Name':x.name} for x in sd.available_cars]    
            print(s.SELECT_CAR)
            print(tabulate(tabular_data= car_data, headers= 'keys',tablefmt="grid"))
            self.__get_car_details__()
        else:
            print(s.NO_CAR_AVAILABLE)
            self.__get_date_preference__()

    #Retrieves the car details for the requested car
    def __get_car_details__(self):
        car_id = input(s.INP_CAR_ID)
        car_details = []
        while not car_id.isdecimal():
            print(s.INCORRECT_INPUT)
            car_id = input(s.INP_CAR_ID)
        car_details = list(filter(lambda x: x.id == int(car_id) ,sd.available_cars))
        while not car_details:
            print(s.INP_CAR_ID)
            car_id = input(s.INP_CAR_ID)
            car_details = list(filter(lambda x: x.id == int(car_id) ,sd.available_cars))
        
        car_details = car_details[0]
        print(s.CAR_DETAILS)
        display_data = []
        display_data.append(['Name',car_details.name])
        display_data.append(['Manufacture Year',car_details.manufacture_year])
        car_model = list(filter(lambda x: x.id == car_details.model, data.carModelList))
        if car_model:
            car_model = car_model[0]
            display_data.append(['Brand',car_model.make.value])
            display_data.append(['Category',car_model.category.value])
            display_data.append(['No of seats',car_model.no_of_seats])
            display_data.append(['Transmission Type',car_model.transmission_type.value])
        car_pricing = list(filter(lambda x: x.car_id == car_details.id, data.carPriceData))
        if car_pricing:
            car_pricing = car_pricing[0]
            display_data.append(['Price/Hr',f'{car_pricing.price_per_hour} {car_pricing.currency}'])
            display_data.append(['Discount for more than 24Hr  booking',f'{car_pricing.discount}%'])
        print(tabulate(tabular_data=display_data,tablefmt='pipe'))
        print('\n')
        selection = input(s.INP_SELECTION)

        while selection.upper() != 'C' and selection.upper() != 'B':
            print(s.INCORRECT_INPUT)
            selection = input(s.INP_SELECTION)
        if(selection.upper() == 'B'):
            self.__list_all_availabe_cars__()
        else:
            self.__view_checkout_details__(int(car_id))  

    def __view_checkout_details__(self, car_id:int):
        print(s.CHECKOUT_DETAILS)
        cart_data = []
        for car in list(filter(lambda x:x.id == car_id ,sd.available_cars)):
            model = [m for m in data.carModelList if m.id == car.model][0]
            cart_data.append([car.id,model.make.value,car.name,car.manufacture_year,self.__get_pricing__(car.id)])
        print(tabulate(tabular_data= cart_data,headers=['Id','Brand','Name','Manufacture Year', 'Total amount'],tablefmt="grid"))
        print('\n')
        selection = input(s.INP_SELECTION)
        while selection.upper() != 'C' and selection.upper() != 'B':
            print(s.INCORRECT_INPUT)
            selection = input(s.INP_SELECTION)
        if(selection.upper() == 'B'):
            self.__list_all_availabe_cars__()
        else:
            self.__check_out_car(cart_data[0])

    def __check_out_car(self,car_data):
       p = self.__add_payment_details__(car_data)
       day_diff, hour_diff = utility.calculate_date_time_difference(sd.request_from,sd.request_to)
       rent_mode = cst.RENTMODE.HOURLY
       if day_diff <= 7 and day_diff > 0:
           rent_mode = cst.RENTMODE.DAY
       else:
           rent_mode = cst.RENTMODE.WEEKLY
       data.carRentalsData.append(CarRental(car_data[0],sd.logged_in_cust_id,str(sd.request_from),str(sd.request_to),rent_mode,p.payment_id))
       print(s.RENT_SUCCESS)
       selection = input(s.INP_SELECTION_1)
       while selection.upper() != 'R' and selection.upper() != 'L' :
            print(s.INCORRECT_INPUT)
            selection = input(s.INP_SELECTION_1)
       if(selection.upper() == 'R'):
            self.__return_car__(data.carRentalsData[-1])
       else:
           self.__logout__()

    def __add_payment_details__(self,car_data):  
        self.__get_payment_info__(car_data[-1])    
        data.paymentData.append(PaymentDetails(car_data[-1]))
        return data.paymentData[-1]
    
    def __return_car__(self,rent_car_data):
        due_amount = round(self.__get_pricing__(rent_car_data.car_id,rent_car_data.rent_to)) * -1
        if due_amount > 0:
            self.__get_payment_info__(due_amount)
            self.__update_payment_details__(rent_car_data.payment_id,due_amount)
            list(filter(lambda x: x.customer_id == sd.logged_in_cust_id and x.is_returned == False , data.carRentalsData))[0].rent_to = datetime.strftime(datetime.today(), '%Y-%m-%d %H:%M:%S')
        list(filter(lambda x: x.customer_id == sd.logged_in_cust_id and x.is_returned == False , data.carRentalsData))[0].is_returned = True
        self.__print_invoice__(rent_car_data)
        self.__addFeedback__(rent_car_data)

    def __update_payment_details__(self,payment_id, total_amount):
        amount = list(filter(lambda x: x.payment_id == payment_id , data.paymentData))[0].total_amount
        list(filter(lambda x: x.payment_id == payment_id , data.paymentData))[0].total_amount = amount + total_amount

    def __addFeedback__(self,rent_car_data):  
        print(s.PROVIDE_FEEDBACK)
        ratings = input(s.INP_FEEDBACK_RATINGS)
        while not ratings.isdecimal():
            print(s.INCORRECT_INPUT)
            ratings = input(s.INP_FEEDBACK_RATINGS)
        while not 1 <= int(ratings) <= 5:
            print(s.INCORRECT_INPUT)
            ratings = input(s.INP_FEEDBACK_RATINGS)
        comments = input (s.INP_COMMENTS)      
        data.feedbackData.append(Feedback(rent_car_data.id,ratings,comments))
        print(s.THANK_YOU)
        selection = input(s.INP_SELECTION_2)
        while selection.upper() != 'L' and selection.upper() != 'B':
            print(s.INCORRECT_INPUT)
            selection = input(s.INP_SELECTION_2)
        if(selection.upper() == 'B'):
            self.__get_date_preference__()
            self.__list_all_availabe_cars__()
        else:
            self.__logout__()

    def __logout__(self):
        sd.logged_in_cust_id = 0
        sd.available_cars = {}
        sd.request_from = ''
        sd. request_to =''
        self.__ask_login_credentials__()

    #Get the pricing details
    def __get_pricing__(self,car_id,rent_to = None):    
        price = [p for p in data.carPriceData if p.car_id == car_id][0]
        if rent_to:
            day_diff, hour_diff = utility.calculate_date_time_difference(datetime.today(),utility.convert_to_datetime(rent_to,2))
        else:
            day_diff, hour_diff = utility.calculate_date_time_difference(sd.request_from,sd.request_to)
        total_amount = (price.price_per_hour * hour_diff) + (price.price_per_hour * (day_diff*24))
        if day_diff > 1:
            #If the car is booked for more than a day. Then discount is applied on the total value
            total_amount = total_amount - (total_amount* (price.discount/100))
        return total_amount
    
    #Gets the payment information
    def __get_payment_info__(self, amount):
        print(s.PAYMENT_DETAILS)
        print(f'Amount To Be Paid: {amount}')
        card_num = input(s.INP_CARD_NUMBER)
        while not utility.check_if_matched(r'\b(?:\d[ -]*?){13,16}\b',card_num):
            print(s.INCORRECT_INPUT)
            card_num = input(s.INP_CARD_NUMBER)
        card_exp = input(s.INP_CARD_EXP)
        while not utility.check_if_matched(r'^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$',card_exp):
            print(s.INCORRECT_INPUT)
            card_exp = input(s.INP_CARD_EXP)
        card_cvv = input(s.INP_CARD_CVV)
        while not utility.check_if_matched(r'\b\d{3,4}\b',card_cvv):
            print(s.INCORRECT_INPUT)
            card_cvv = input(s.INP_CARD_CVV) 
    
    #Prints the invoice
    def __print_invoice__(self,rent_car_data):
        car_details = list(filter(lambda x: x.id == rent_car_data.car_id, data.carList))[0]
        payment = list(filter(lambda x: x.payment_id == rent_car_data.payment_id, data.paymentData))[0]
        print('Return Success!!')
        print('Thank you For Choosing Us\n')
        invoice_data = [['Invoice Number', uuid.uuid4()]]
        invoice_data.append(['Car', f'{car_details.name}'])
        invoice_data.append(['Rent From',datetime.strftime(utility.convert_to_datetime(rent_car_data.rent_from,2), '%d-%m-%Y %I:%M %p')])
        invoice_data.append(['Rent To',datetime.strftime(utility.convert_to_datetime(rent_car_data.rent_to,2), '%d-%m-%Y %I:%M %p')])
        invoice_data.append(['Total Amount',payment.total_amount])
        print(tabulate(tabular_data= invoice_data,tablefmt="simple"))
