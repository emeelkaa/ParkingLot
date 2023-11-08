from Constants import *
from Admin import *
from ParkingLot import *
from User import *

def PrintSelectMode():
    print("------------------------------------------")
    print(" Select Your Mode     ")
    print("------------------------------------------")
    print(" 1. Admin ")
    print(" 2. Customer ")
    print(" 3. Quit ")
    print("------------------------------------------")

parkingLot = ParkingLot()
UserDict = {}
def main():
    admin = Admin("Admin", "123")

    while True:
        PrintSelectMode()
        role = int(input("Input : "))

        if role == int(UserRole.ADMIN):
            if admin.checkAccount():
                admin.viewAdminPage()

        elif role == int(UserRole.USER):
            ShowUserLoginPage()

        else:
            print("Quit Parking Lot System")
            break

def ShowUserLoginPage():
        while True:
            print("User Account Menu:")
            print("1. Make ID")
            print("2. Log in")
            print("3. Quit")
            
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                MakeUserID()
            elif choice == "2":
                UserLogin()
            elif choice == "3":
                break
            else:
                print("oops")

def MakeUserID():
    id = input("User ID: ")
    password = input("User Password: ")
    isDisable = input("Are you didable(y/n): ")
    if isDisable == 'y':
        isDisable = True
    else:
        isDisable = False

    carType = input("Choose your car type(1.Car/2.Truck/3.Van/4.Motorbike): ")
    if carType == "1":
        carType = VehicleType.CAR
    elif carType == "2":
        carType = VehicleType.TRUCK
    elif carType == "3":
        carType = VehicleType.VAN
    elif carType == "4":
        carType = VehicleType.MOTORBIKE
    
    carName = input("Write your car name: ")

    if id in UserDict:
        print("ID is already exist")
        return

    else: # make new id
        user = User(id,password,isDisable,carName,carType)
        UserDict[id] = user

def UserLogin():
    id = input("User ID: ")
    password = input("User Password: ")
    if id in UserDict:
        if(UserDict[id].ComparePassword(password)):
            print("Success to Login")
            UserDict[id].ShowUserPage()
        else:
            print("Wrong Password")
            return

    else : # no id
        print("Wrong ID")

if __name__ == "__main__":
    main()
