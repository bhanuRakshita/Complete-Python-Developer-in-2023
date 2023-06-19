file=open('08_File\sample.txt')
print(file.read())

file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())

file.seek(0)
print(file.readlines())

file.close()


