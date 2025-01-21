def main():
    price = 50
    paid = 0
    while paid < price:
        print(f"Amount Due: {price - paid}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            paid += coin
    print(f"Change Owed: {(paid - price)}")


main()
