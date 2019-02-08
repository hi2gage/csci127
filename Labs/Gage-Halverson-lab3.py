# --------------------------------------
# CSCI 127, Lab 3                      |
# January 31, 2019                     |
# Your Name                            |
# -------------------------------------- 
# Calculate how many z's are in a      |
# sentence using three techniques.     |
# --------------------------------------

def count_built_in(sentence):
    return sentence.count("z", 0, len(sentence))

def count_iterative(sentence):
    i = 0
    z = 0
    while i < len(sentence):
        if sentence[i] == "z":
            z += 1
        i += 1
    return z
def count_recursive(sentence):
    if sentence == "":
        return 0
    else:
        if sentence[0] == "z":
            return 1 + count_recursive(sentence[1:])
        else:
            return count_recursive(sentence[1:])

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of z's using ...")
        print("---------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
