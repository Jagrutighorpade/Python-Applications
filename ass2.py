def ChkNum(m):
    if m%2==0:
        print("even number")
    else:
        print("odd number")
     

def main():
    a=int(input("enter number = "))
    ChkNum(a)

if __name__=="__main__":
    main()