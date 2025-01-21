def main():
    print(parse(input("HTML: ")))


def parse(s):

    try:
        a, b = s.split("http://youtube.com/embed/")
    except ValueError:
        try:
            a, b = s.split("https://youtube.com/embed/")
        except ValueError:
            try:
                a, b = s.split("https://www.youtube.com/embed/")
            except ValueError:
                a = ""
                b = ""

    if ("<iframe" in a) and ("</iframe>" in b):
        code = b.split('"', maxsplit=1)
        return "https://youtu.be/" + code[0]
    else:
        return "None"



if __name__ == "__main__":
    main()

