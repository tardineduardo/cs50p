def convert(x):
    return x.replace(':)', '🙂').replace(':(', '🙁')


def main():
    sentence = input("say something: ")
    sentence = convert(sentence)
    print(sentence)

main()