
def name():
    name=input("enter your 1st name = ")
    surname=input("enter your surname = ")
    return name + surname
def main():
    full_name=name()
    print(full_name)

if __name__=="__main__":
    main()