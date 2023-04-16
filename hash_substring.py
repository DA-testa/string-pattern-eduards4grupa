# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()
    if input_type == "f":
        with open("tests/06") as f:
            patt = f.readline().rstrip()
            text = f.readline().rstrip()
            return patt, text
    else:
        patt = input().rstrip()
        text = input().rstrip()
        return patt, text
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
    n = len(text)
    m=len(patt)
    p=31
    m_mod = 10**9+9
    p_pow=[1]
    for i in range(1,m):
        p_pow.append((p_pow[-1]*p)%m_mod)
        
    h=[0] * (n  + 2)
    for i in range(1,n+1):
        h[i] = (h[i-1] + (ord(text[i-1]) - ord('a')+1)*p_pow[i-1])% m_mod
        
    patt_hash=0
    for i in range(m):
        patt_hash=(patt_hash+(ord(patt[i])-ord('a')+1)*p_pow[i]) % m_mod
   
    occurrences=[]
    for i in range(n-m+1):
        current_hash = (h[i+m]-h[i]+m_mod)% m_mod
        if current_hash == patt_hash:
            if text[i:i+m] == patt:
                occurrences.append(i)
                          
        
                   
                   
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

