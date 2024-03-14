def fCalTax(memberStatus, total):
    discount = 0.00 
    if memberStatus == 1: 
        if total <= 1000: 
            discount = 0.00 
        elif total <= 5000: 
            discount = total * 0.05 
        elif total <= 10000: 
            discount = total * 0.10 
        else: 
            discount = total * 0.15
    return discount 

def fCalScore(memberStatus, total):
    if memberStatus != 0: 
        if total <= 500: 
            score = 0 
        elif total <= 1000: 
            score = 5 
        elif total <= 5000: 
            score = 10 
        else:
            score = 15 
    return score

print("* Welcome to user-define function program *")
memberType = int(input("Enter member status [0=none/1=member]: "))
price = float(input("Enter product price: "))
amount = int(input("Enter product amount: "))
myScore = int(input("Enter your score: "))

total = price * amount
myDiscount = fCalTax(memberType, total)
myScore = myScore + fCalScore(memberType, total)
if memberType==0:
    strMemberType="None member"
else:
    strMemberType="Member"

print("************* Result ************** ")
print("Member type: " + strMemberType)
print("{0:<23s} {1:>15,.2f} ".format("Product price",price))
print("{0:<23s} {1:>15,.2f} ".format("Product amount",amount))
print("{0:<23s} {1:>15,.2f} ".format("Total", total))
print("{0:<23s} {1:>15,.2f} ".format("Discount",myDiscount))
print("{0:<23s} {1:>15,.2f} ".format("Your score point",myScore))
print("************* Good bye ************ ")
