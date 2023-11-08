from ParkingSpot import *
from Constants import *


class ParkingFloor():
    def __init__(self, floorNumber):
        self.__spotCount = 0
        self.__floorNumber = floorNumber
        self.__handicappedSpots = {}
        self.__compactSpots = {}
        self.__largeSpots = {}
        self.__motorbikeSpots = {}


    def floornumber(self):
        return self.__floorNumber

    def handicappedSpots(self):
        return self.__handicappedSpots

    def compactSpots(self):
        return self.__compactSpots

    def largeSpots(self):
        return self.__largeSpots

    def motorbikeSpots(self):
        return self.__motorbikeSpots

    def AddParkingSpot(self, spotType: ParkingSpotType):
        self.__spotCount += 1
        # Determine the next spot number for the given spot type
        if spotType == ParkingSpotType.HANDICAPPED:
            next_spot_number = len(self.__handicappedSpots) + 1
            parkingSpot = HandicappedSpot(next_spot_number,self.__floorNumber)
            self.__handicappedSpots[next_spot_number] = parkingSpot
        elif spotType == ParkingSpotType.COMPACT:
            next_spot_number = len(self.__compactSpots) + 1
            parkingSpot = CompactSpot(next_spot_number,self.__floorNumber)
            self.__compactSpots[next_spot_number] = parkingSpot
        elif spotType == ParkingSpotType.LARGE:
            next_spot_number = len(self.__largeSpots) + 1
            parkingSpot = LargeSpot(next_spot_number,self.__floorNumber)
            self.__largeSpots[next_spot_number] = parkingSpot
        elif spotType == ParkingSpotType.MOTORBIKE:
            next_spot_number = len(self.__motorbikeSpots) + 1
            parkingSpot = MotorbikeSpot(next_spot_number,self.__floorNumber)
            self.__motorbikeSpots[next_spot_number] = parkingSpot


    def ShowAllParkingFloor(self):
        print(f"Floor {self.__floorNumber} - Parking Spots:")
        print(f"Total Spots: {self.__spotCount}")
        print(f"Handicapped Spots: {len(self.__handicappedSpots)}")
        for spot_number, spot in self.__handicappedSpots.items():
            print(f"  - Spot {spot_number}: {spot.isFree()}")

        print(f"Compact Spots: {len(self.__compactSpots)}")
        for spot_number, spot in self.__compactSpots.items():
            print(f"  - Spot {spot_number}: {spot.isFree()}")

        print(f"Large Spots: {len(self.__largeSpots)}")
        for spot_number, spot in self.__largeSpots.items():
            print(f"  - Spot {spot_number}: {spot.isFree()}")

        print(f"Motorbike Spots: {len(self.__motorbikeSpots)}")
        for spot_number, spot in self.__motorbikeSpots.items():
            print(f"  - Spot {spot_number}: {spot.isFree()}")

        print()