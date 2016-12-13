def sum_pair(l,k):
    end = len(l) - 1
    start = 0

    while start < end:
        if l[start] + l[end] > k:
            end -=1
        elif l[start] + l[end] < k:
            start +=1
        elif l[start] + l[end] == k:
            return True
        else:
            break
    return False



print sum_pair([1,2,3,9], 8) == False
print sum_pair([1,2,4,4], 8) == True

# if numbers are not sorted, then... 

def sum_pair_other(l,k):

    seen = set()

    for num in l:
        if num not in seen:
            seen.add(num)
        else:
            if k - num in seen:
                return True

    return False

print sum_pair_other([1,2,3,9], 8) == False
print sum_pair_other([1,2,4,4], 8) == True