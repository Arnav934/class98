def readFromFile():
    fileReader = open('text.txt')
    totalWords = 0
    print(fileReader) 
    for eachLine in fileReader:
        print(eachLine)
        words = eachLine.split()
        print(words)
        print(len(words))
        totalWords = totalWords + len(words)
    print(totalWords)

readFromFile()
