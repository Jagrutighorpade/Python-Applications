def revr(no):
    while no!=0:
        remider=no%10
        no=no//10
        print(remider,end="")

def main():
    num=int(input("enter no = "))
    revr(num)
if __name__=="__main__":
    main()