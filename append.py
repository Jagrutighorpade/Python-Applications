def appd():
    list1=[10,20,[300,400,[5000,7000]]]
    list1[2][2].insert(1,6000)
    print(list1)
def main():
    appd()
if __name__=="__main__":
    main()