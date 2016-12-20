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
        
        


# when is everyone available... meeting time finder - time given in blocks of 30

#(2, 3)  meeting from 10:00 – 10:30 am
#(6, 9)  meeting from 12:00 – 1:30 pm































