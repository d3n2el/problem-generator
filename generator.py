import random
print()
def main():
    operation = input("What type of operations do you want to do?")
    operations = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide"
    }
    if operation in operations:
        print(operations[operation])

    error= 0
    err= 0
    attempts= 10
    lvl= get_level()
    for _ in range(10):
        x= generate_integer(lvl)
        y= generate_integer(lvl)
        q= x+y
        for i in range(3):
            print(f"{x} {o} {y} =", end=" ")
            m = int(input())
            if m == x+y:
                break
            if not m == x + y:
                error+= 1
                print("EEE")
        if not m== x o y:
            err+=1
        if error== 3:
            print(f"{x} {o} {y} = {q}")
            error= 0

    f= attempts-err
    print("Score:",f)
def get_level():
    while True:
        lvl= input("Level:")
        if lvl == "1" or lvl== "2" or lvl== "3":
            return int(lvl)
        else:
            continue


def generate_integer(level):
    match level:
        case 1:
            n= random.randint(0,9)
            return n
        case 2:
            n= random.randint(10,99)
            return n
        case 3:
            n= random.randint(100,999)
            return n
        case _:
            raise ValueError

if __name__ == "__main__":
    main()


