def digi(no):
    add=0
    while no!=0:
        remider=no%10
        no=no//10
        add=add+remider
    print(add)



def main():
    num=int(input("enter no = "))
    digi(num)
if __name__=="__main__":
    main()