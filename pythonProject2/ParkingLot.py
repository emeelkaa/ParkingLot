from ParkingFloor import ParkingFloor
from Constants import *

class ParkingLot:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            self.parkingFloors = []

    