def swap():
    fileReader = open('file1.txt')
    print(fileReader)
    data1 = fileReader.read()
    print(data1)

    fileReader2 = open('file2.txt')
    print(fileReader2)
    data2 = fileReader2.read()
    print(data2)
    fileReader = open('file1.txt', 'w')
    fileReader2 = open('file2.txt', 'w')
    fileReader.write(data2)
    fileReader2.write(data1)

swap()