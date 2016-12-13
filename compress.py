def compress(s):

    output = ''
    count = 1

    i = 1

    while i < len(s):

        if s[i] == s[i-1]:
            count +=1
        
        else:
            output = output + s[i-1] + str(count)
            count = 1
        i +=1

    output = output + s[i-1] + str(count)



    return output


print compress('aabcccccaaa') == 'a2b1c5a3'