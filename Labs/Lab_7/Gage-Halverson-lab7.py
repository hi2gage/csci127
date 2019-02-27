# --------------------------------------
# CSCI 127, Lab 7                      |
# February 28, 2019                    |
# Gage Halverson                       |
# --------------------------------------

def create_dictionary(input_filename):

    #opens file in read mode
    file = open(input_filename, "r")

    #creates new open dictionary
    dic_temp = {}

    #loops through all the lines in the input_filename
    for line in file:
        #splits file into list
        values = line.split(",")
        #checks to see if the key is a space or comma or normal character
        if values[1] == "space\n":
            dic_temp[" "] = values[0]
        elif values[1] == "comma\n":
            dic_temp[","] = values[0]
        else:
            #sets key as character and value as the ascii value
            dic_temp[values[1][0:-1]] = values[0]
    file.close()
    return dic_temp


def translate(sentence, dictionary, output_file):

    #creates and opens file in Write mode
    output = open(output_file, "w")

    #loops through all the characters in string
    for char in sentence:
        #checks to see if the character is in the dictionary
        if char not in dictionary:
            line = (char + " " + "UNKNOWN" + "\n")
            output.write(line)
        else:
            line = (char + " " + dictionary[char] + "\n")
            #writes line to output_file
            output.write(line)
    output.close()
# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")

    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")
# --------------------------------------

main()
