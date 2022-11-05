def concat():
    a1=["Hello","take"]
    a2=["dear","sir"]
    a3= [x+y for x in a1 for y in a2]
    print(a3)


def main():
    concat()

if __name__=="__main__":
    main()