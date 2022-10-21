## Big O notation: 
# -- Time Complexity: O(n)
# -- Space Complexity: O(n)

def slidingWindow(list, balance, n):
    total = sum(list[:n])

    max_value = total
    if max_value > balance:
        return []
    else:
        max_list = [list[0],list[1],list[2]]

    for i in range(len(list) - n):
        total = total - list[i] + list[i+n]
        if total <= balance and total > max_value:
            max_value = total
            max_list = [list[i+1],list[n-i+1],list[i+n]]
        elif total > balance:
            break

    return max_list


def findPair(fileName, balance):
    # Use a dictionary to store key(Price) value(Unique Identifies) pairs for each row
    prices_dict = {}
    # Create a list to store each value as well
    price_list = []

    with open(fileName) as file:
        for line in file:
            split = line.split(", ")
            key = int(split[1])
            prices_dict.update({key:split[0]})
            price_list.append(key)
    
    # Check to make sure there are at least 2 items
    if len(price_list) < 3:
        print("Not possible")

    # After we have our value we want to use a sliding window algorithm (Great for finding subarrays on sorted lists)
    # Set n to 2 because this is the size we want our window to be due to getting 2 gifts
    result = slidingWindow(price_list, balance, 3)
    
    if len(result) == 0:
        print("Not possible")
    else:
        # Format return string
        print(f"{prices_dict[result[0]]} {result[0]}, {prices_dict[result[1]]} {result[1]}, {prices_dict[result[2]]} {result[2]}")

## Example
findPair('prices.txt', 10000)
