number = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)
if number.lower().strip(" ").replace(" ", "").replace("-", "") == "fortytwo":
    print("Yes")
elif number.strip() == "42":
    print("Yes")
else:
    print("No")
