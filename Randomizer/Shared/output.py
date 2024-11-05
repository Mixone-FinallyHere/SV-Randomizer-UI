chosen_starters = []

def fetch_devname(index: int, csvdata):
    return str.strip(csvdata[index])

def output_starters():
    names_file = open('Randomizer/Shared/english_names.txt', 'r')
    names = []
    for x in names_file:
        names.append(x)
    names_file.close()
    index_line = 1
    with open('output_starter.txt', 'w') as output_starter:
        for i in range(0, len(chosen_starters), 3):
            output_starter.write('Rando '+ str(index_line) + '\n')
            chunk = chosen_starters[i:i+3]
            for index in chunk:
                name = fetch_devname(index, names)
                output_starter.write(name + '\n')
            output_starter.write('\n')
            index_line = index_line + 1