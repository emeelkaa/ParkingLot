from Constants import *
from ParkingFloor import *
from Account import *
from ParkingLot import *


class Admin:
    _instance = None

    def __new__(cls, id, password):
        if cls._instance is None:
            cls._instance = super(Admin, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, id, password):
        if not self.initialized:
            self.__Account = Account(id, password, UserRole.ADMIN)
            self.initialized = True
            self.parkingLot = ParkingLot()

    def viewAdminPage(self):
        while True:
            print("Admin Menu:")
            print("1. Add Parking Floor")
            print("2. Display Parking Lot")
            print("3. Return to Main Menu")

            choice = input("Enter your choice (1/2/3): ")

            print("------------------------------------------")

            if choice == "1":
                self.addParkingFloor()
            elif choice == "2":
                self.displayParkingFloors()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def checkAccount(self):
        print("------------------------------------------")
        inputId = input("Admin ID: ")
        inputPassword = input("Admin Password: ")
        print("------------------------------------------")

        if inputId == self.__Account.id and inputPassword == self.__Account.password:
            print("Successfully Logged In")
            return True
        else:
            return False

    def displayParkingFloors(self):
        if not self.parkingLot.parkingFloors:
            print("No parking floors available.")
        else:
            print("Parking Floors and Spots:")
            for floor_number, floor in enumerate(self.parkingLot.parkingFloors, start=1):
                floor.ShowAllParkingFloor()
                print()

    def addParkingFloor(self):
        try:
            spotCounts = {}
            spotCounts[ParkingSpotType.HANDICAPPED] = int(input("Enter the number of handicapped spots: "))
            spotCounts[ParkingSpotType.COMPACT] = int(input("Enter the number of compact spots: "))
            spotCounts[ParkingSpotType.LARGE] = int(input("Enter the number of large spots: "))
            spotCounts[ParkingSpotType.MOTORBIKE] = int(input("Enter the number of motorbike spots: "))

            if any(count < 0 for count in spotCounts.values()):
                print("Spot counts cannot be negative.")
                return

            floorNumber = len(self.parkingLot.parkingFloors) + 1
            floor = ParkingFloor(floorNumber)

            for spot_type, count in spotCounts.items():
                for _ in range(count):
                    floor.AddParkingSpot(spot_type)

            self.parkingLot.parkingFloors.append(floor)
            print(f"Added a new floor (Floor {floorNumber}) with the specified parking spots.")
        except ValueError:
            print("Invalid input. Please enter valid spot counts.")