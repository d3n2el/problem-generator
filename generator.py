import random

def main():
    error= 0
    err= 0
    attempts= 10
    lvl= get_level()
    p= 10
    while p> 0:
        x= generate_integer(lvl)
        y= generate_integer(lvl)
        i=3
        q= x+y
        while i >0:
            print(f"{x} + {y} =", end=" ")
            m = int(input())
            i= i-1
            p= p-1
            if m == x+y:
                break
            if not m == x + y:
                error+= 1
                print("EEE")
        if not m== x+y:
            err+=1
        if error== 3:
            print(f"{x} + {y} = {q}")
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
            n= random.randint(0,99)
            return n
        case 3:
            n= random.randint(0,999)
            return n
        case _:
            raise ValueError

if __name__ == "__main__":
    main()


