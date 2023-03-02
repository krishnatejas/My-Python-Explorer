def comput(fun):
    def result(a,b,c):
        if b.lower() in ('add','+','sum'):
            print("The result of {} {} {} : {}".format(a,b,c,a+c))
        elif b.lower() in ('sub','-','minus'):
            print("The result of {} {} {} : {}".format(a,b,c,a-c))
        elif b.lower() in ('mul','*','X','x'):
            print("The result of {} {} {} : {}".format(a,b,c,a*c))
        elif b.lower() in ('div','/'):
            if a == 0.0:
                print("Opertion failes becoz a is 0")
            else:
                print("The result of {} {} {} : {}".format(a,b,c,a/c))
        else:
            print("un-recongnized operator")
    return result

@comput
def oper(a,b,c):
    print("calculation done")

a = int(input("enter first number: "))
b = input("enter operation to : ")
c = int(input("enter second number: "))

oper(a,b,c)








