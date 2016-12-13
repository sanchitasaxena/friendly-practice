# remove the repeats of e's in the given string,... 
#don't remove repeats of other letters

def bye_e(s):

    output = []

    i = 0
    while i < len(s):
        if s[i] != 'e':
            output.append(s[i])
        else:
            # if s[i] == 'e'
            i +=1
            while i < len(s):
                output.append(s[i])
                if s[i] == 'e':
                    continue    
                else:
                    output.append(s[i])
                break
                i +=1
           
        i +=1
    print output
    return ''.join(output)


print bye_e('hheed') == 'hhed'
print bye_e('weeeeeeed') == 'wed'

