def min(no):
    L1=[]
    size=no
    min=0
    for index in range(no):
        L1.insert(index,int(input("enter list item in L1 =")))
    print(L1)
    for item in L1:
        if item < min:
            min=item
    print(min)


def main():
    size= int(input("enter size of list ="))
    min(size)
if __name__=="__main__":
    main()