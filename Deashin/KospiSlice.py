import json

list = []

with open('c:\\Users\\user\\PycharmProjects\\kospi.csv', 'r') as f:
    for line in f:
        list.append(line.split(','))
print(list)







