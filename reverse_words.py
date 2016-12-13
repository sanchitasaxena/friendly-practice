def reverse_sentence(sentence):

    output = []

    i = 0

    while i < len(sentence):
        #finding the start of the words
        if sentence[i] != ' ':
            start = i
            #finding the end of the words
            while i < len(sentence) and sentence[i] != ' ':
                # incrementing until you hit space
                i +=1
            output.append(sentence[start:i])
        #incrementing until you hit space
        i+=1
    # reversing the output
    output = output[::-1]
    # make sure there is a space! joining elements to make strings
    return ' '.join(output)



print reverse_sentence('i like this the best') == 'best the this like i'
print reverse_sentence('i love you') == 'you love i'




