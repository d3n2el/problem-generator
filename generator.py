import random


def main():
    error= 0
    attempts= 10
    lvl= get_level()
    p= 10
    w=3
    while p> 0:
        x,y = generate_integer(lvl)
        i=3
        while i >0:
            print(f"{x}+{y}=", end=" ")
            m = int(input())
            i= i-1
            p= p-1
            if m == x+y:
                break
            if not m == x + y:
                error+= 1
                print("EEE")`
            print(x+y)

    f= attempts-error
    print("Score:",f)
def get_level():
    while True:
        lvl= input("Level:")
        if lvl == "1" or lvl== "2" or lvl== "3":
            return int(lvl)
        else:
            continue




def generate_integer(level):
    if level == 1:
        x = random.randrange(10)
        y = random.randrange(10)
    if level == 2:
        x = random.randrange(100)
        y = random.randrange(100)
    if level == 3:
        x = random.randrange(1000)
        y = random.randrange(1000)
    return x, y

if __name__ == "__main__":
    main()
