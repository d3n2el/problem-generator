import random


def main():
    lvl= get_level()
    x,y = generate_integer(lvl)
    print(f"{x}+{y}")


def get_level():
    while True:
        lvl= input("Level")
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