# coding: UTF-8
import matplotlib.pyplot as plt
import numpy as np
#グラフを描く

filename = "data_macro.csv"
raw_data = open(filename, 'r')
data = np.loadtxt(raw_data, delimiter=",")

def errorBar(a, b):
  return a*b

x = []
y = []

for i in data:
 if i[4] < 1.0:
  x.append(i[4])
 else:
  x.append(0)

for i in data:
  y.append(i[3])

func = np.poly1d(np.polyfit(x,y,1))(x)

plt.plot(x,y,'go',label = "points")
plt.plot(x, func, label='Least Squares Method')

err = []
for i in y:
    ev = errorBar(i, 0.025)
    err.append(ev)

r = np.corrcoef(x,y)
plt.errorbar(x,y,yerr=err,fmt='go',ecolor='g')

plt.legend()
plt.title("figure 2.5")
plt.xlabel("Induced Current (μA)")
plt.ylabel("Velocity of Bar Magnet (cm/s)")
plt.axis([0,4,5,30])
plt.show()

#calculated theoretical value
'''x = np.linspace(0.1, 30)
y = -1.502*10**-6/x

plt.plot(x,y)
plt.show()'''
