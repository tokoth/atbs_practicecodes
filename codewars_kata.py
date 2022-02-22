# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive.
# The string can contain any char.

# My Solution

def xo(s):
    num_x = 0
    num_o = 0
    if 'x' or 'o' not in s:
        return True
    elif 'x' or 'o' in s:
        return False    
    elif 'x' or 'X' in s:
        num_x += 1
    elif 'o' or 'O' in s:
        num_o += 1
    elif num_x == num_o:
        return True
    elif num_x != num_o :
        return False

# Copied Long Solution
#def xo(s):
    #countX = 0
    #countO = 0
    #for i in s:
        #if (i == 'X') | (i == 'x'):
            #countX = countX + 1
        #elif (i == 'O') | (i == 'o'):
            #countO = countO + 1
    #if countX == countO:     
        #return True
    #else:
        #return False

# Copied short solution

#def xo(s):
    #s = s.lower()
    #return s.count('x') == s.count('o')

#def xo(s):
    #return s.lower().count('x') == s.lower().count('o')
    
# Test        
print(xo('xo'))
print(xo('xo0'))
print(xo('xxxoo'))