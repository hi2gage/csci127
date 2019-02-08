import random

def main():
    rows = int(input("how many rows would you like?"))
    columns = int(input("How many columns would you like?"))

    for i in range(rows):
        for j in range(columns):
            x = random.randint(1,2)
            y = random.randint(1,2)
            if ( x == y):
                print("*", end="")
            else:
                print("-", end="")
        print("")
        


main()
