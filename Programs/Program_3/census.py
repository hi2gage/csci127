census_file = open("census.txt", "r")

for one_line in census_file:
    values = one_line.split()
    print("State: " + values[0] + ", Population: " +  values[1])

census_file.close()
