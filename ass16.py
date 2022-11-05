def add(num):
    add=0
    for i in range(1,num):
        if num%i==0:
            add=add+i
    print(add,end="")

def main():
    no=int(input("enter no for factors="))
    add(no)
if __name__=="__main__":
    main()