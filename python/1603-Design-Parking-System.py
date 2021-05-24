class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big < 1:
                return False
            else:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium < 1:
                return False
            else:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small < 1:
                return False
            else:
                self.small -= 1
                return True

        # Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(1)
param_2 = obj.addCar(2)
param_3 = obj.addCar(3)
param_4 = obj.addCar(1)

print(param_1, param_2, param_3, param_4)
