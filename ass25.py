def ChkPri(no):
    L1=[]
    size=no
    add=0
    for index in range(size):
        L1.insert(index,int(input("enter item in list=")))
    print(L1)
    for i in L1:
        if  i%2!=0:
            print(i,end="")
            #add=add+i
    #print(add)
            


def main():
    size=int(input("enter size = "))
    ChkPri(size)
if __name__=="__main__":
    main()