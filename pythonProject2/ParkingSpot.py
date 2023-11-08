from Constants import *
import datetime

class ParkingSpot:
    def __init__(self, spotNumber, parkingSpotType,floorNum):
        self.__free = True
        self.__vehicle = None
        self.__parkingSpotType = parkingSpotType
        self.floorNum = floorNum
        self.spotNum = spotNumber

    def isFree(self):
        return self.__free

    def assignVehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False
        self.__vehicle.parkedSpot = self
        self.__vehicle.enterTime = datetime.datetime.now()


    def removeVehicle(self):
        self.__vehicle.exitTime = datetime.datetime.now()
        self.__vehicle.parkedSpot = None
        self.__vehicle = None
        self.__free = True

    def ShowSpotInfo(self):
        print("Floor : {self.floorNum}, spotType = {self.__parkingSpotType}, spotNum : {self.spotNum}")

class HandicappedSpot(ParkingSpot):
    def __init__(self, number,floorNum):
        super().__init__(number, ParkingSpotType.HANDICAPPED,floorNum)

class CompactSpot(ParkingSpot):
    def __init__(self, number,floorNum):
        super().__init__(number, ParkingSpotType.COMPACT,floorNum)

class LargeSpot(ParkingSpot):
    def __init__(self, number,floorNum):
        super().__init__(number, ParkingSpotType.LARGE,floorNum)

class MotorbikeSpot(ParkingSpot):
    def __init__(self, number,floorNum):
        super().__init__(number, ParkingSpotType.MOTORBIKE,floorNum)
