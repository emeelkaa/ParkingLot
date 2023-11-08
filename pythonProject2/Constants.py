from enum import Enum, IntEnum


class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    VAN = 3
    MOTORBIKE = 4

class ParkingSpotType(Enum):
    HANDICAPPED = 1
    COMPACT = 2
    LARGE = 3
    MOTORBIKE = 4


class UserRole(IntEnum):
    ADMIN = 1
    USER = 2
    NULL = 3