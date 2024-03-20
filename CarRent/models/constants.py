from enum import Enum

class CarCategory(Enum):
    SUV = 'SUV'
    SEDAN = 'Sedan'
    HATCHBACK = 'Hatch back'

class TransmissionType(Enum):
    Manual = 'Manual'
    AUTO = 'Automatic'
    IMT = 'IMT'

class Make(Enum):
    HYUNDAI='Hyundai'
    MARUTISUZUKI = 'Maruthi Suzuki'
    KIA = 'KIA'

class RENTMODE(Enum):
    HOURLY = 'HOURLY',
    DAY = 'DAY'
    WEEKLY = 'WEEKLY'


