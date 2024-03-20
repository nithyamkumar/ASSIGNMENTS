from models.customer_model import Customer
from models.customer_credential import CustomerCredential
from models.car_model import CarModel
from models.car import Car
from models.car_pricing import CarPricing
from models.car_rental import CarRental
from models.payment_details import PaymentDetails
import models.constants as cst

#Dummy customer data
customerList = [
    Customer(1,'Demo Customer1'),
    Customer(2,'Demo Customer2')
    ]
#Dummy customer credentials data
customerCredentialList = [CustomerCredential(1,'demo1','demo1'),
                          CustomerCredential(2,'demo2','demo2'),
                        ]

#Dummy car models data                        
carModelList = [
    CarModel('i20',cst.Make.HYUNDAI,cst.CarCategory.HATCHBACK,cst.TransmissionType.AUTO,4,1),
    CarModel('i20',cst.Make.HYUNDAI,cst.CarCategory.HATCHBACK,cst.TransmissionType.Manual,4,2),
    CarModel('i20',cst.Make.HYUNDAI,cst.CarCategory.HATCHBACK,cst.TransmissionType.IMT,4,3),
    CarModel('Creta',cst.Make.HYUNDAI,cst.CarCategory.SUV,cst.TransmissionType.AUTO,5,4),
    CarModel('Creta',cst.Make.HYUNDAI,cst.CarCategory.SUV,cst.TransmissionType.Manual,5,5),
    CarModel('Verna',cst.Make.HYUNDAI,cst.CarCategory.SEDAN,cst.TransmissionType.Manual,4,6),
    CarModel('Seltos',cst.Make.KIA,cst.CarCategory.SUV,cst.TransmissionType.AUTO,5,7),
    CarModel('Seltos',cst.Make.KIA,cst.CarCategory.HATCHBACK,cst.TransmissionType.Manual,4,8),
    CarModel('Baleno',cst.Make.MARUTISUZUKI,cst.CarCategory.HATCHBACK,cst.TransmissionType.AUTO,4,9),
    CarModel('Vittara',cst.Make.MARUTISUZUKI,cst.CarCategory.SUV,cst.TransmissionType.AUTO,5,10)
]

#Dummy Available cars data
carList = [
    Car(1,'i20-Blue',1,'2018'),
    Car(2,'i20-Black',1,'2020'),
    Car(3,'i20-Blue',2,'2018'),
    Car(4,'i20-Black',2,'2020'),
    Car(5,'Creta-White',4,'2018'),
    Car(6,'Crete-Black',5,'2020'),
    Car(7,'Verna-White',6,'2018'),
    Car(8,'Seltos-Black',7,'2021'),
    Car(9,'Seltos-White',8,'2021'),
    Car(10,'Baleno-Black',9,'2021'),
    Car(11,'Baleno-White',10,'2021')
]

#Dummy Car Pricing data
carPriceData=[
    CarPricing(1,100,25),
    CarPricing(2,100,25),
    CarPricing(3,100,25),
    CarPricing(4,100,25),
    CarPricing(5,200,25),
    CarPricing(6,200,25),
    CarPricing(7,150,25),
    CarPricing(8,200,25),
    CarPricing(9,200,25),
    CarPricing(10,100,25),
    CarPricing(11,100,25)
]

#Dummy Car Rental Information
carRentalsData = [
    #CarRental(10,1,'2024-04-01 17:00:00','2024-04-01 22:00:00',cst.RENTMODE.HOURLY,'1')
]

#Dummy Payment Information
paymentData = [
    PaymentDetails(500,'CARD','1')
]

feedbackData = []