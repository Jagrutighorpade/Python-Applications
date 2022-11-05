#patterna
###
###
###

def pat(no):
    for i in range(1,no+1):
        for j in range(1,no+1):
            print("*",end="")
        print()

def main():
    NO=4
    pat(NO)
if __name__=="__main__":
    main()