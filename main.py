# coding: UTF-8
import matplotlib.pyplot as plt
import numpy as np
#グラフを描く

filename = "hai.csv"
raw_data = open(filename, 'r')
data = np.loadtxt(raw_data, delimiter=",")

def errorBar(a, b):
  return a*b

x = []
y = []

for i in data:
  x.append(i[0])
for i in data:
  y.append(i[1])

plt.plot(x,y,'bo',label = "rand")

err = []
#誤差棒を描く
for i in y:
    ev = errorBar(i, 0.025)
    err.append(ev)

r = np.corrcoef(x,y)[0][1]

plt.errorbar(x,y,yerr=err,fmt='ro',ecolor='g')

plt.legend()
plt.title("figure 1.1")
plt.xlabel("x")
plt.ylabel("Y")
plt.axis([0,1,0,1])
plt.show()
