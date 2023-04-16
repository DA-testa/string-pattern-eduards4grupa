# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    patt = input().rstrip()
    text = input().rstrip()
    # return both lines in one return
   
    # this is the sample return, notice the rstrip function
    return patt, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    n = len(text)
    m=len(patt)
    p=31
    m_mod = 10**9+9
    p_pow=[1]
    for i in range(1,m):
        p_pow.append((p_pow[-1]*p)%m_mod)
        
    h=[0]*(n+1)
    for i in range(1,n+1):
        h[i] = (h[h-1] + (ord(tex[i-1]) - ord('a')+1)*p_pow[i-1])% m_mod
        
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

