
def prim(no):

    if no%1==0 and no%no==0:
        print("it is a prime no")
    else:
        print("its a not prime")


def main():
    num=int(input("enter no from = "))
    prim(num)

if __name__=="__main__":
    main()