## Big O notation: 
# -- Time Complexity: O(N^2)
# -- Space Complexity: O(n)


def combo(option_count, options):
    #Use backtracking to find the possible combinations given the amount of X in a string
    if option_count == 1:
        return options
    else:
        return [ 
            y + x
            for y in combo(1, options)
            for x in combo(option_count - 1, options)
        ]

def combinations(string, options):
    # Count to store the number of times x shows up. 
    # combo list to store all available combinations of 0, 1
    count = 0
    combo_list = []
    result = []
    for i in string:
        if i == 'X':
            count += 1
    

    combo_list = combo(count, options)

    # Loop through the each combo list and string at the same time swap the X out for each posible option.
    for i in range(len(combo_list)):
        entry = combo_list[i]
        print(entry)
        new_string = ""
        x = 0
        for j in range(len(string)):
            if string[j] == 'X':
                new_string += entry[x]
                x+=1
            else:
                new_string += string[j]
        result.append(new_string)

    print(result)

# Example
combinations('10X10X0X',['0','1'])