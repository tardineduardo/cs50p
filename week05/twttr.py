



def main():
    term = input("Input: ")
    print(shorten(term))

def shorten(word):
    output = ""
    for i in range(len(word)):
        if not (word[i].lower() in 'aeiou'):
            output = output + word[i]
    return output

if __name__ == "__main__":
    main()
