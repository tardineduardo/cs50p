def main():
    quote = input("Greeting: ")
    print(value(quote))


def value(greeting):

    if "hello" in greeting.lower().lstrip():
        return 0
        # print("$0")
    elif greeting[0].lower().lstrip() == "h":
        return 20
        # print("$20")
    else:
        return 100
        # print("$100")






if __name__ == "__main__":
    main()





