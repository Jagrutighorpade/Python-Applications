#pattern
def pat(no):
    for i in range(no):
        for j in range(1,no+1):
            print(j,end="")
        print()


def main():
    no=5
    pat(no)


if __name__=="__main__":
    main()