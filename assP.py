
#pattern 
###
##
#

def pat(no):
    for i in range(no):
        for j in range(no-i):
            print("*",end="$")


def main():
    no=4
    pat(no)
if __name__=="__main__":
    main()