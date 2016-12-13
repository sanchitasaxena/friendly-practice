def one_away(s1,s2):

    s1 = sorted(s1)
    s2 = sorted(s2)

    count = 0

    p1 = 0
    p2 = 0

    # if the lengths of both strings are equal, check for replacement
    if len(s1) == len(s2):
        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                count +=1
            else: 
                i+=1
                print str(i) + 'after else'
            i+=1
            print str(i) + 'after conditions'
    # if length of s1 > s2
    if len(s1) > len(s2):
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 +=1
                p2 +=1
            else:
                p1 +=1
                count +=1
    # if length of s2 < s1
    if len(s2) > len(s1):
        while p2 < len(s2) and p1 < len(s1):
            if s1[p1] == s2[p2]:
                p1 +=1
                p2 +=1
            else:
                p2 +=1
                count +=1
# check if count/ one away is true
    if count > 1:
        return False

    return True


#test cases
print one_away('happy','happyy') == True # True
print one_away('happy','happi') == True # True
print one_away('pale', 'ple') == True # True
print one_away('pale','bake') == True # False