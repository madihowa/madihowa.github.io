class Mobile:
    def __init__(self, brand, color, serviceProvider):
        self.brand = brand
        self.color = color
        self.serviceProvider = serviceProvider

    def makeAPhoneCall(self, number):
        print("Brr brrr brr calling {}".format(number))
