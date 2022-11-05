def digi(no):
    #print(len(str(num)))
    len=0
    while no!=0:
        #reminder=no%10
        no=no//10
        len=len+1
        
    print(len)


def main():
    num=int(input("enter no = "))
    digi(num)
if __name__=="__main__":
    main()