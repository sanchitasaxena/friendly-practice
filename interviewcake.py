#sum of 4 numbers == k

#max difference

def get_max_difference(l):

    min_num = l[0]
    largest_difference = l[1] - l[0]

    for i, num in enumerate(l):
        if i <= 1:
            continue
        current_difference = num - min_num
        largest_difference = max(current_difference, largest_difference)
        min_num = min(min_num, num)

    return largest_difference



print get_max_difference([10, 7, 5, 8, 11, 9])


# product of every int in a list except that int

def product_excluding_int(l):

    products = []
    product = 1
    for num in l:
        product = float(product * num)

    for num in l:

        products.append(int(product / num))

    return products


print product_excluding_int([1, 7, 3, 4])

        
# highest product of three integers out of a list of integers...

def highest_product(l):
    # two negative numbers multiplied by a third positive gives us a positive 

    # highest_produt_of_three = l[0]*l[1]*l[2]
    # highest_product_two = lowest_product_two = l[0] * l[1]
    # lowest = min(l[0], l[1])
    # highest = max(l[0], l[1])

    # for i range(len(l)):

    # highest product O(n^3):
    if len(l) < 3:
        return 'You need at least 3 numbers to solve this problem'

    highest_product_of_three = l[0]*l[1]*l[2]
    for num1 in l:
        for num2 in l:
            for num3 in l:
                if num1 * num2 * num3 > highest_product_of_three:
                    highest_product_of_three = num1 * num2 * num3
    return highest_product_of_three


print highest_product([-10,-10,1,3,2]) == 300 

# when is everyone available? 
# list_of_meetings - tuples

def merge_ranges(meetings):
    # sorted list of ranges
    meetings = sorted(meetings)
    # list of merged meetings
    merged_meetings = [meetings[0]]



print merge_ranges([(0,1),(3,5),(4,8),(10,12),(9,10)]) #== [(0,1), (3,8), (9,12)]
        






































