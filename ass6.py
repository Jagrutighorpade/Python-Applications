def fun(val):
    if val%5==0:
        print("TRUE")
    else:
        print("FALSE")



def main():
    val=int(input("enter number ="))
    fun(val)
if __name__=="__main__":
    main()