def frq(no):
    L1=[]
    size=no
    add=0
    for index in range(no):
        L1.insert(index,int(input("enter input=")))
    print(L1)
    chk=int(input("check no="))
    for i in L1:
        if (chk==i):
            add=add+1
    print(add)

def main():
    size=int(input("enter size"))
    frq(size)
if __name__=="__main__":
    main()