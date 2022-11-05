def ChkNum(m):
    if m==0:
        print("zero")
    elif m<0:
        print("number is negative")
    else:
        print("num is positive")

def main():
    a=int(input("enter number = "))
    ChkNum(a)
if __name__=="__main__":
    main()