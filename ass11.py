import module1 as m
def even(a):
    if a%2==0:
        return 1
    else:
        return 0  

def main():
    no1=int(input("enter 1st value="))
    no2=int(input("enter 1st value="))
    m.add(no1,no2)
    m.sub(no1,no2)
    m.mult(no1,no2)
    m.div(no1,no2)
    val=even(no1)
    if val:
        print("even")
    else:
        print("odd")




if __name__=="__main__":
    main()
