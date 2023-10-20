
value = 0
cash = 0
count = 0
value = int(input("enter your amount - "))



def coins (value):
    if value >= 5000:
        afordable = int(input("enter your afordable 5000 - "))
        cash = value // 5000
        if afordable < cash:
            cash = afordable 
        value = value - (5000 * cash)
        print("5000 = ",cash)
        print()

    if value >= 1000:
        afordable = int(input("enter your afordable 1000 - "))
        cash  = value // 1000
        if afordable < cash:
            cash = afordable 
        print("1000 = ",cash)
        value = value - (1000 * cash)
        print()

    if value >= 500:
        afordable = int(input("enter your afordable 500 - "))
        cash = value // 500
        if afordable < cash:
            cash = afordable
        print("500 = ",cash)
        value = value - (500 * cash)
        print()

    if value >= 100:
        afordable = int(input("enter your afordable 100 - "))
        cash = value // 100
        if afordable < cash:
            cash = afordable
        print ("100 = ",cash)
        value = value - (100 * cash)
        print()

    if value >= 50:
        afordable = int(input("enter your afordable 50 - "))
        cash = value // 50
        if afordable < cash:
            cash = afordable
        print ("50 = ",cash)
        value = value - (50 * cash)
        print()

    if value >= 20:
        afordable = int(input("enter your afordable 20 - "))
        cash = value // 20
        if afordable < cash:
            cash = afordable
        print ("20 = ",cash)
        value = value - (20 * cash)
        print()

    if value >= 10:
        afordable = int(input("enter your afordable 10 - "))
        cash = value // 10
        if afordable < cash:
            cash = afordable
        print ("10 = ",cash)
        value = value - (10 * cash)
        print()

    if value >= 5:
        afordable = int(input("enter your afordable 5 - "))
        cash = value // 5
        if afordable < cash:
            cash = afordable
        print ("5 = ",cash)
        value = value - (5 * cash)
        print()
        
    if value >= 2:
        afordable = int(input("enter your afordable 2 - "))
        cash = value // 2
        if afordable < cash:
            cash = afordable
        print ("2 = ",cash)
        value = value - (2 * cash)
        print()
    
    if value >= 1:
        afordable = int(input("enter your afordable 1 - "))
        cash = value // 1
        if afordable < cash:
            cash = afordable
        print ("1 = ",cash)
        value = value - (1 * cash)
        print()

    if value != 0:
        print ('''oops! I'm sorry, we can't afordable your amount
                        thank you!

    ''')
    else:
        print("thank you!----- come again...")




    


coins(value)


    
    

    

