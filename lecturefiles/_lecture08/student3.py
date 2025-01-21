# Returns student as tuple, without unpacking it


def main():
    student = get_student()
    if student[0] == 'Padma':
        student[1] = 'Ravenclaw'
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    age = int(input("Age: "))
    return [name, age]


if __name__ == "__main__":
    main()
