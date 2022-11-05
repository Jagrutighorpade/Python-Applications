def fact(no):
    mul=1 
    for i in range(1,no+1):
        mul*=i
    print(mul)

def main():
    no=int(input("enetr no ="))
    fact(no)

if __name__=="__main__":
    main()