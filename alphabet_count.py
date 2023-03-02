import string
value = input("enter name: ")
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
#alpha = enumerate(string.ascii_lowercase,1)
#for i,j in alpha:
#    dic[j] = i

def outer(x):
    def inner(value):
        count,new = 0,0
        for k in value.lower():
            if k != " ":
                #print(dic[k])
                count += dic[k]
            else:
                count += 0
        for val in str(count):
            new += int(val)
        print("string total count: ", count)
        print("Numerology count of provided string: ", new)
    return inner

@outer
def numer(value):
    print("computation")

numer(value)
      
    
    
    
