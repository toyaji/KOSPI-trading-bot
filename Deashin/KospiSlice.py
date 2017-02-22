import json

list = []
f1 = open('c:\\Users\\user\\PycharmProjects\\kospi1.csv', 'w')

with open('c:\\Users\\user\\PycharmProjects\\kospi.csv', 'r') as f:
    for line in f:
        new = line.split(',')
        print(new.pop(3))
        s = ",".join(new)
        f1.write(s)
    f1.close()
print(list)







