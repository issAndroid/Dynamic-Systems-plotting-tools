import matplotlib.pyplot as plt
import numpy as np

n, primeList = 900, []

## returns numbers in one line of 100000.text
def getNumbersInLine(line):
    primeList, cursor = [], 0
    for i in range(len(line)):
        if ((line[i].isdigit()) and line[i-1]==' '):
            cursor = i
            while(line[i]!=' '):
                i += 1
            primeList.append(int(line[cursor: i]))
    return primeList


## read 100000.txt and cut prime numbers
nc = 1
with open('100000.txt','r') as file:
    for line in file:
        if(line[0] != '#'):
            primeList += (getNumbersInLine(line))
            nc += 1
            if (nc > n):
                break
file.close()

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='polar')
ax.plot(primeList, primeList, '.', color='black')
ax.set_yticklabels([])
plt.show()
