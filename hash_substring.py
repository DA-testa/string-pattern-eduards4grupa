# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()
    if input_type == "f":
        with open("tests/06") as f:
            patt = f.readline().rstrip()
            text = f.readline().rstrip()
            
    else:
        patt = input().rstrip()
        text = input().rstrip()
    return (patt, text)
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
   
    # this is the sample return, notice the rstrip function
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(patt, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    res = []
    if len(patt) > len(text):
        return res
    
    patt_hash=hash(patt)
    text_hash=[hash(text[i:i+len(patt)]) for i in range (len(text) - len(patt)+1)]
    for i in range(len(text_hash)):
        if patt_hash == text_hash[i] and text[i:i+len(patt)] == patt:
            res.append(i)
    return res


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

