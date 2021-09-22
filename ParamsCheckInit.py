#Find number in random list#

import random
def find():
    a = int(input("Select Number"))
    b = False
    l = []
    for i in range(5000):
        l.append(random.randint(0,10000))

    for k in l:
        if (k == a):
            b = True
            break
        else :
            b = False
    print(b)
    return(b)

find()

#######################################################################################

list1 = [1234567890B, 0987654321A, 2345678765C]

def search():
    
    a = hex(input("Select"))
    b = False
    l = []
    val = a in list1
    if val == False :
        print("not")
        
    return a= False :
        print("not")
        
    return a

