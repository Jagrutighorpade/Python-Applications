def max(no):
    L1=[]
    size=no
    max=0
    for index in range(no):
        L1.insert(1,int(input("enter list items = ")))
    print(L1)
    for items in L1:
        if items>max:
            max=items
    print("max no=",max)


def main():
    size=int(input("enter size of list = "))
    max(size)
if __name__=="__main__":
    main()