# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# March 28, 2019                                      |
# Gage Halverson                                      |
# -----------------------------------------------------

class Queue:
    def __init__(self,name):
        self.list = []

    def __iadd__(self, int_number):
        self.list.append(int_number)
        return "Contents: " + str(self.list)[1:-1].replace(",","")

    def enqueue(self, number):
        self.list.append(number)

    def dequeue(self):
        return self.list.pop(0)

    def is_empty(self):
        return len(self.list) == 0

    def __str__(self):
        return "Contents: " + str(self.list)[1:-1].replace(",","")

# Your solution goes here.  Do not change anything below.

# -----------------------------------------------------
def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
