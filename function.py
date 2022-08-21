 def countWordsFromFile():
    fileName = input("Enter the file name:- ")
    with open(sample1.txt, 'r') as a:
    data_a = a.read()
    with open(sample2.txt, 'r') as a:
    data_b = b.read()
    with open(sample1.txt, 'w') as a:
    a.write(data_b)
    with open(sample2.txt, 'w') as a:
    b.write(data_a)