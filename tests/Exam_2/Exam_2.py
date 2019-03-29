
def retain_every_other_line(input_file, output_file):
    input = open(input_file, "r")
    output = open(output_file, "w")
    odd = True
    for line in input:
        if odd == True:
            output.write(line)
            odd = not odd
        else:
            odd = True









retain_every_other_line("input.txt", "output.txt")
