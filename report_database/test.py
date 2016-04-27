



if __name__== "__main__":
    string = "blah, lots  ,  of ,  spaces, here "
    list = [];
    list = [x.strip() for x in string.split(',')]
    print(list)



    #[x.strip() for x in my_string.split(',')]