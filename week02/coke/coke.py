amountDue = 50

while(amountDue > 0):
    print(f"Amount Due: {amountDue}")
    coin = int(input("Insert Coin: "))
    if((coin == 25) or (coin == 10) or (coin == 5)):
        amountDue = amountDue - coin

changeOwed = abs(amountDue)
print(f"Change Owed: {changeOwed}")
