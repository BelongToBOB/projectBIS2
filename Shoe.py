class Shoe:
    def __init__(self,id,brand,model):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__price = 0.00
        self.__discount = 0.00
        self.__net = 0.00
        self.__setPrice()
        self.__setDiscount()

    def __setPrice(self):
        if self.__brand == "Puma":
            if self.__model == "Batman Suede":
                self.__price = 1350.00
            elif self.__model == "Basket Classic":
                self.__price = 1750.00
            elif self.__model == "Pokemon Rider":
                self.__price = 4300.00
            else : 
                self.__price = 4200.00
        elif self.__brand == "Reebok":
            if self.__model == "Turbo Restyle":
                self.__price = 1400.00
            elif self.__model == "Zig Kinetica":
                self.__price = 2600.00
            elif self.__model == "GL 1000":
                self.__price = 1500.00
            else :
                self.__price = 1200.00
        elif self.__brand == "Converse":
            if self.__model == "Chuck Taylo All Star":
                self.__price = 1400.00
            elif self.__model == "Jack Purcell":
                self.__price = 2400.00
            elif self.__model == "Star Life Clean":
                self.__price = 2600.00
            elif self.__model == "Point Star":
                self.__price = 1900.00
            else:
                self.__price = 1550.00
        elif self.__brand == "Adidas":
            if self.__model == "Neo":
                self.__price = 2350.00
            elif self.__model == "Stan Smith Lux":
                self.__price = 5800.00
            elif self.__model == "Forum Low":
                self.__price = 3600.00
            else:
                self.__price = 2200.00
        else:
            self.__brand == "Nike"
            if self.__model == "Air Force":
                self.__price = 3800.00
            elif self.__model == "Air Max":
                self.__price =3600.00
            elif self.__model == "Retro GTS":
                self.__price = 2100.00
            else:
                self.__price = 3600.00
        self.__setNet()
    
    def __setDiscount(self):
        if self.__brand == "Puma":
            if self.__model == "Batman Suede":
                self.__discount = 0.05 * self.__price
            elif self.__model == "Basket Classic":
                self.__discount = 0.05 * self.__price
            elif self.__model == "Pokemon Rider":
                self.__discount = 0.08 * self.__price
            else:
                self.__discount = 0.08 * self.__price
        elif self.__brand == "Reebok":
            if self.__model == "Turbo Restyle":
                self.__discount = 0.10 * self.__price
            elif self.__model == "Zig Kinetica":
                self.__discount = 0.15 * self.__price
            elif self.__model == "GL 1000":
                self.__discount = 0.10 * self.__price
            else:
                self.__discount = 0.15 * self.__price
        elif self.__brand == "Converse":
            if self.__model == "Chuck Taylo All Star":
                self.__discount = 0.10 * self.__price
            elif self.__model == "Jack Purcell":
                self.__discount = 0.20 * self.__price
            elif self.__model == "Star Life Clean":
                self.__discount = 0.20 * self.__price
            elif self.__model == "Point Star":
                self.__discount = 0.20 * self.__price
            else:
                self.__discount = 0.10 * self.__price
        elif self.__brand == "Adidas":
            if self.__model == "Neo":
                self.__discount = 0.20 * self.__price
            elif self.__model == "Stan Smith Lux":
                self.__discount = 0.30 * self.__price
            elif self.__model == "Forum Low":
                self.__discount = 0.30 * self.__price
            else:
                self.__discount = 0.20 * self.__price
        else:
            if self.__model == "Air Force":
                self.__discount = 0.30 * self.__price
            elif self.__model == "Air Max":
                self.__discount = 0.20 * self.__price
            elif self.__model == "Retro GTS":
                self.__discount = 0.20 * self.__price
            else:
                self.__discount = 0.20 * self.__price
        self.__setNet()

    def __setNet(self):
        self.__net = self.__price - self.__discount

    def getID(self):
        return ("ID: ",self.__id)
    
    def getBrand(self):
        return ("BRAND: ",self.__brand)
    
    def getModel(self):
        return ("MODEL: ",self.__model)
    
    def getPrice(self):
        return self.__price
    
    def getDiscount(self):
        return self.__discount
    
    def getNet(self):
        return self.__net
    
    def __str__(self):
        return "ID:{0:>42s}\nBrand:{1:>35s}\nModel:{2:>38s}\nPrice:{3:>35,.2f}\nDiscount:{4:>35,.2f}\nNet:{5:>40,.2f}".format(self.__id,self.__brand,self.__model,self.__price,self.__discount,self.__net)