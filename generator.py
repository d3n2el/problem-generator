import random


def main():
    error= 0
    attempts= 10
    lvl= get_level()
    p= 10
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
                print("EEE")
        f= attempts-error
        print(f)
def get_level():
    while True:
        lvl= input("Level:")
        if lvl == "1" or lvl== "2" or lvl== "3":
            return int(lvl)
        else:
            continue