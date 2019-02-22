earthquake = open("earthquakes.csv", "r")
input_line = earthquake.readline()
locations = []
while input_line:
    value_1 = input_line.split(",")
    if locations.count(value_1[-5]) == 0:
        locations.append(value_1[-5])
    input_line = earthquake.readline()

locations.sort()
print(locations)
