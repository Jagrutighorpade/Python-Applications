def even(val1):
    isum=0
    isum1=0
    for i in range(val1+1):
        if i%2==0:
            isum=isum+i
        else:
            isum1=isum1+i
    return isum-isum1        




def main():
    no1=5
    ans=even(no1)
    print(ans)
if __name__=="__main__":
    main()