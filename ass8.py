

def ChkEvn(no):
    no1=no*2
    for i in range(no1):
        if i%2==0:
            print(i,end=" ")


def  main():
    val=int(input("enter no ="))
    ChkEvn(val)
if __name__=="__main__":
    main()