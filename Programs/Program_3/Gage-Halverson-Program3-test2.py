def main():
    #reads file
    temp_file = open("weather.csv", "r")
    input_line = temp_file.readline()
    input_line = temp_file.readline()

    i = 0
    while input_line:
        line = input_line.split(",")
        if len(line) != 15:
            i +=1
        input_line = temp_file.readline()

    print(i)

main()
