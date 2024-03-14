class Shoes:
    def __init__(self, id, brand, model, price, discount):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__discount = discount
        self.__net = 0.00
        self.__setNet()

    def __setPrice(self):
        if self.__brand == 1:
            if self.__model == 1:
                self.__price = 1350.00
            elif self.__model == 2:
                self.__price = 1750.00
            elif self.__model == 3:
                self.__price = 4300.00
            elif self.__model == 4:
                self.__price = 4200.00
        elif self.__brand == 2:
            if self.__model == 1:
                self.__price = 1400.00
            elif self.__model == 2:
                self.__price = 2600.00
            elif self.__model == 3:
                self.__price = 1500.00
            elif self.__model == 4:
                self.__price = 1200.00
        elif self.__brand == 3:
            if self.__model == 1:
                self.__price = 1400.00
            elif self.__model == 2:
                self.__price = 2400.00
            elif self.__model == 3:
                self.__price = 2600.00
            elif self.__model == 4:
                self.__price = 1900.00
            elif self.__model == 5:
                self.__price = 1550.00
        elif self.__brand == 4:
            if self.__model == 1:
                self.__price = 2350.00
            elif self.__model == 2:
                self.__price = 5800.00
            elif self.__model == 3:
                self.__price = 3600.00
            elif self.__model == 4:
                self.__price = 1550.00
        elif self.__brand == 5:
            if self.__model == 1:
                self.__price = 3800.00
            elif self.__model == 2:
                self.__price = 3600.00
            elif self.__model == 3:
                self.__price = 2100.00
            elif self.__model == 4:
                self.__price = 3600.00
        else:
            print("ป้อนตัวเลือกยี่ห้อไม่ถูกต้อง")

    def __setDiscount(self):
        if self.__brand == 1:
            if self.__model == 1 or self.__model == 2:
                self.__discount = 0.05
            elif self.__model == 3 or self.__model == 4:
                self.__discount = 0.08
        elif self.__brand == 2:
            if self.__model == 1 or self.__model == 3:
                self.__discount = 0.1
            elif self.__model == 2 or self.__model == 4:
                self.__discount = 0.15
        elif self.__brand == 3:
            if self.__model == 1 or self.__model == 5:
                self.__discount = 0.1
            elif self.__model == 2 or self.__model == 3 or self.__model == 4:
                self.__discount = 0.2
        elif self.__brand == 4:
            if self.__model == 1 or self.__model == 4:
                self.__discount = 0.2
            elif self.__model == 2 or self.__model == 3:
                self.__discount = 0.3
        elif self.__brand == 5:
            if self.__model == 1 or self.__model == 4:
                self.__discount = 0.3
            elif self.__model == 2 or self.__model == 3:
                self.__discount = 0.2
        else:
            print("ป้อนตัวเลือกยี่ห้อไม่ถูกต้อง")

    def __setNet(self):
        self.__net = self.__price - (self.__price * self.__discount)

    def get_id(self):
        return self.__id

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_discount(self):
        return self.__discount

    def get_net(self):
        return self.__net
    
    def __str__(self):
        return f"{self.__id} - {self.__brand} - {self.__model} - {self.__price:.2f} - {self.__discount * 100}% - {self.__net:.2f}"

    def set_price(self, price):
        self.__price = price
        self.__setNet()

    def set_discount(self, discount):
        self.__discount = discount
        self.__setNet()
