from Shoe import Shoe

shoeList = []
con = "Y"

while con.upper() == "Y":
    id = input("ID: ")
    brand = int(input("BRAND [1 = Puma  2 = Reebox  3 = Converse  4 = Adidas  5 = Nike]: "))

    if brand == 1:
        brand = "Puma"
        model = int(input("MODEL [1=Batman Suede] [2=Basket Classic] [3=Pokemon Rider] [4=Minecraft]: "))
        if model == 1:
            model = "Batman Suede"
        elif model == 2:
            model = "Basket Classic"
        elif model == 3:
            model = "Pokemon Rider"
        elif model == 4:
            model = "Minecraft"
        else:
            print("ป้อนตัวเลือกไม่ถูก")
            break
    elif brand == 2:
        brand = "Reebok"
        model = int(input("MODEL [1=Turbo Restyle] [2=Zig Kinetica] [3=GL 1000] [4=Flexagon Force]: "))
        if model == 1:
            model = "Turbo Restyle"
        elif model == 2:
            model = "Zig Kinetica"
        elif model == 3:
            model = "GL 1000"
        elif model == 4:
            model = "Flexagon Force"
        else:
            print("ป้อนตัวเลือกไม่ถูก")
            break
    elif brand == 3:
        brand = "Converse"
        model = int(input("MODEL [1=Chuck Taylor All Star] [2=Jack Purcell] [3=Star Life Clean] [4=Point Star] [5=Star in Black Youth]: "))
        if model == 1:
            model = "Chuck Taylor All Star"
        elif model == 2:
            model = "Jack Purcell"
        elif model == 3:
            model = "Star Life Clean"
        elif model == 4:
            model = "Point Star"
        elif model == 5:
            model = "Star in Black Youth"
        else:
            print("ป้อนตัวเลือกไม่ถูก")
            break
    elif brand == 4:
        brand = "Adidas"
        model = int(input("MODEL [1=Neo] [2=Stan Smith Lux] [3=Forum Low] [4=Run Falcon]: "))
        if model == 1:
            model = "Neo"
        elif model == 2:
            model = "Stan Smith Lux"
        elif model == 3:
            model = "Forum Low"
        elif model == 4:
            model = "Run Falcon"
        else:
            print("ป้อนตัวเลือกไม่ถูก")
            break
    elif brand == 5:
        brand = "Nike"
        model = int(input("MODEL [1=Air Force] [2=Air Max] [3=Retro GTS] [4=Free Run]: "))
        if model == 1:
            model = "Air Force"
        elif model == 2:
            model = "Air Max"
        elif model == 3:
            model = "Retro GTS"
        elif model == 4:
            model = "Free Run"
        else:
            print("ป้อนตัวเลือกไม่ถูก")
            break
    else:
        print("ป้อนตัวเลือกไม่ถูก")
        break 
    print("***************************************")    
    print("ID: {0}\nBRAND: {1}\nMODEL: {2}\n".format(id, brand, model))
    shoe_detail = Shoe(id, brand, model)
    price = shoe_detail.getPrice()
    discount = shoe_detail.getDiscount()
    net = shoe_detail.getNet()
    print("ราคา: ",price," บาท")
    print("ส่วนลด: ",discount," บาท")
    print("ราคาสุทธิ: ",net," บาท")
    print("***************************************")
    con = input("ท่านต้องการทำงานต่อหรือไม่? [Y = ใช่ / N = ไม่]: ")

    

