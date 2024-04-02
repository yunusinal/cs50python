"""
implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Users can only insert 5,10,25 cents.
"""
totalbalance=0
while True:
    balance=int(input("Insert a coin:"))
    if balance not in [5,10,25] :
        print("Amount Due: 50")

    else:
        totalbalance+=balance
        if totalbalance<50:
            print("Amount Due: {}".format(50-totalbalance))
                
        else: 
            print("Change Owed: {}".format(totalbalance-50)) 
            break