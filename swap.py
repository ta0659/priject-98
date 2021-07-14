def swap():
    file1 = input("What is the name of file one?")
    file2 = input("What is the name of file two?")

    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a) 
        print("Completed! The content in ", file1, "was successfully switched with the content in ",file2,"." )
swap()