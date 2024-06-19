with open("DAY26/file1.txt")as file1:
    data1=file1.readlines()

with open("DAY26/file2.txt")as file2:
    data2=file2.readlines()

result=[int(item) for item in data1 if item in data2]
print(result)