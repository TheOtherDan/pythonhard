def get_num(text="Enter a number: "):
    return int(input(text))

def adder(x,y):
    return x+y

if __name__=="__main__":
    a = get_num()
    b = get_num("Enter another one: ")
    print "the number %i and %i add up to " % (a,b) + str(adder(a,b))
