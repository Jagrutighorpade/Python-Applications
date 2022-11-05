def fact(no):
    mul=1
    for i in range(1,no+1):
        mul=mul*i
    print("factorial=",mul)

def main():
    num=int(input("enter no for factorial="))
    fact(num)
if __name__=="__main__":
    main()