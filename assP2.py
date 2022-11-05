#pattern
###
##
#
def pat(no):
    for i in range(1,no+1):
        for j in range(1,no-i+1):
            print("*",end="")
        print()


def main():
    no=4
    pat(no)

if __name__=="__main__":
    main()