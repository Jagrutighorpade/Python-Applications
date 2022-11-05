def add(no):
    L1=[]
    size=no
    add=0
    for index in range(no):
        L1.insert(index,int(input("enter list items=")))
    print(L1)

    for item in L1:
        add=add+item
    print(add)
        


def main():
    size=int(input("enter size of list = "))
    add(size)
if __name__=="__main__":
    main()