from Account import Account
from Constants import *
from ParkingLot import ParkingLot
from ParkingSpot import ParkingSpot
import datetime

class User:
    def __init__(self,id,password,isDisable,carName,carType):
        self.parkingLot = ParkingLot()
        self.account = Account(id,password,UserRole.USER)
        self.car = Car(carName,carType)
        self.isDiable = isDisable
    
    def ComparePassword(self,password):
        return self.account.ComparePassword(password)

    def ShowUserPage(self):
        while True:
            print("User Menu:")
            print("1. Enter Parking Lot")
            print("2. Exit Parking Lot")
            print("3. Return to Main Menu")

            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                self.EnterParkingLot()
            elif choice == "2":
                self.ExitParkingLot()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def EnterParkingLot(self):
        for floor in self.parkingLot.parkingFloors:
            # Check for empty spots of the specified car type on the current floor
            if self.isDiable == True:
                for spot in floor.handicappedSpots():
                    if floor.handicappedSpots()[spot].isFree():
                        floor.handicappedSpots()[spot].assignVehicle( self.car )
                        self.car.SetEnterTime(datetime.datetime.now())
                        print(f"A { self.car.vehicleType } has entered the parking lot and parked in Compact Spot {spot} on the {floor.floornumber()} floor")
                        self.car.SetSpotInfo(floor.floornumber(),spot,ParkingSpotType.HANDICAPPED)
                        self.car.__isParked = True
                        return

            elif self.car.vehicleType == VehicleType.CAR and len(floor.compactSpots()) > 0:
                # Assign the car to the first available compact spot
                for spot in floor.compactSpots():
                    if floor.compactSpots()[spot].isFree():
                        floor.compactSpots()[spot].assignVehicle( self.car )
                        self.car.SetEnterTime(datetime.datetime.now())
                        print(f"A { self.car.vehicleType } has entered the parking lot and parked in Compact Spot {spot} on the {floor.floornumber()} floor")
                        self.car.SetSpotInfo(floor.floornumber(),spot,ParkingSpotType.COMPACT)
                        self.car.__isParked = True
                        return
                    
            elif self.car.vehicleType  == VehicleType.TRUCK and len(floor.largeSpots()) > 0:
                # Assign the truck to the first available large spot
                for spot in floor.largeSpots():
                    if floor.largeSpots()[spot].isFree():
                        floor.largeSpots()[spot].assignVehicle( self.car )
                        self.car.SetEnterTime(datetime.datetime.now())
                        print(f"A { self.car.vehicleType } has entered the parking lot and parked in Large Spot {spot} on the {floor.floornumber()} floor")
                        self.car.SetSpotInfo(floor.floornumber(),spot,ParkingSpotType.LARGE)
                        self.car.__isParked = True
                        return

            elif self.car.vehicleType  == VehicleType.VAN and len(floor.largeSpots()) > 0:
                # Assign the van to the first available large spot
                for spot in floor.largeSpots():
                    if floor.largeSpots()[spot].isFree():
                        floor.largeSpots()[spot].assignVehicle( self.car )
                        self.car.SetEnterTime(datetime.datetime.now())
                        print(f"A { self.car.vehicleType } has entered the parking lot and parked in Large Spot {spot} on the {floor.floornumber()} floor")
                        self.car.SetSpotInfo(floor.floornumber(),spot,ParkingSpotType.LARGE)
                        self.car.__isParked = True             
                        return

            elif self.car.vehicleType  == VehicleType.MOTORBIKE and len(floor.motorbikeSpots()) > 0:
                # Assign the motorbike to the first available large spot
                for spot in floor.motorbikeSpots():
                    if floor.motorbikeSpots()[spot].isFree():
                        floor.motorbikeSpots()[spot].assignVehicle( self.car.vehicleType )
                        self.car.SetEnterTime(datetime.datetime.now())
                        print(f"A { self.car.vehicleType } has entered the parking lot and parked in Motorbike Spot {spot} on the {floor.floornumber()} floor")
                        self.car.SetSpotInfo(floor.floornumber(),spot,ParkingSpotType.MOTORBIKE)
                        return
                    
    def ExitParkingLot(self):
        # if floorNum == 1 -> that means 0st array
        floor = self.parkingLot.parkingFloors[self.car.floorNum - 1]

        spot = None
        if self.car.spotType == ParkingSpotType.COMPACT:
            spot = floor.compactSpots()[self.car.spotNum]
        elif self.car.spotType == ParkingSpotType.LARGE:
            spot = floor.largeSpots()[self.car.spotNum]
        elif self.car.spotType == ParkingSpotType.MOTORBIKE:
            spot = floor.motorbikeSpots()[self.car.spotNum]
        elif self.car.spotType == ParkingSpotType.HANDICAPPED:
            spot = floor.handicappedSpots()[self.car.spotNum]

        self.car.SetExitTime(datetime.datetime.now())
        spot.removeVehicle()
        self.car.__isParked = False

        self.car.CalculateFee()
    

class Car:
    def __init__(self,name,vehicleType):
        self.__name = name
        self.vehicleType = vehicleType

        self.__enterTime = None
        self.__exitTime = None
        self.__isParked = False

        self.floorNum = None
        self.spotNum = None
        self.spotType = None

    def SetEnterTime(self, enterTime):
        self.__enterTime = enterTime
    
    def SetExitTime(self, exitTime):
        self.__exitTime = exitTime

    def FindMyCar(self):
        if(self.__isParked == False):
            print("Your Car not Parked")
            return
        
        else:
            print("Car Parked {} floor {} spot".format(self.floorNum,self.spotNum))

    def SetSpotInfo(self,floorNum,spotNum,spotType):
        self.floorNum = floorNum
        self.spotNum = spotNum
        self.spotType = spotType

        print("Car Parked {} floor {} spot".format(floorNum,spotNum))

    def CalculateFee(self):
        parking_duration = self.__exitTime - self.__enterTime
        hour_parked = parking_duration.total_seconds() / 3600
        if(self.vehicleType == 1):
            if(hour_parked <= 1):
                parking_fee = 4
            elif(hour_parked <= 3):
                parking_fee = 4 + 3.5*(hour_parked - 1)
            else:
                parking_fee = 4 + 3.5*2 + 2.5*(hour_parked - 3)

        elif(self.vehicleType == 2 or self.vehicleType == 3):
            if(hour_parked <= 1):
                parking_fee = 5
            elif(hour_parked <= 3):
                parking_fee = 5 + 4.5*(hour_parked - 1)
            else:
                parking_fee = 5 + 4.5*2 + 3*(hour_parked - 3)

        else:
            if(hour_parked <= 1):
                parking_fee = 3
            elif(hour_parked <= 3):
                parking_fee = 3 + 2.5*(hour_parked - 1)
            else:
                parking_fee = 3 + 2.5*2 + 2*(hour_parked - 3)

        print(f"You used parking spot for {hour_parked:.3f} hours and the Parking Fee is ${parking_fee}.")