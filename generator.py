import random
import operator
print()
def main():
    operation = input("What type of operations do you want to do?") 
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    error= 0
    err= 0
    attempts= 10
    lvl= get_level()
    for _ in range(10):
        x= generate_integer(lvl)
        y= generate_integer(lvl)
        func = operations[operation]
        q= func(x, y)
        for i in range(3):
            print(f"{x} {operation} {y} =", end=" ")
            m = int(input())
            if m == q:
                break
            if not m == q:
                error+= 1
                print("EEE")
        if not m== q:
            err+=1
        if error== 3:
            print(f"{x}{operation}{y} = {q}")
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


