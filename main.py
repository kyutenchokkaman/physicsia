# coding: UTF-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#グラフを描く

df1 = pd.read_csv('data_macro.csv')[['Induced Current (μA)','0.01*|S-E|/f*30 (m/s)']]
df2 = pd.read_csv('data_micro.csv')[['Induced Current (μA)','0.005 / f*30 (m/s)']]

d1 = df1[df1['Induced Current (μA)'] < 1]
d2 = df2[df2['Induced Current (μA)'] < 1]

print(np.dot(d1,d2))
'''
x = df1['Induced Current (μA)']
y = df1['0.01*|S-E|/f*30 (m/s)']
plt.plot(x,y,'go', label = 'Full Distance of the Magnet (F)')

func = np.poly1d(np.polyfit(x, y,1))(x)
plt.plot(x, func, label='Best Fit Curve for F')


x = df2['Induced Current (μA)']
y = df2['0.005 / f*30 (m/s)']
plt.plot(x,y, 'bo', label = 'Only Around the Coil (O)')

func = np.poly1d(np.polyfit(x, y,1))(x)
plt.plot(x, func, label='Best Fit Curve for O')


f = np.linspace(10000, 0.375)
b = 0.15/f+0.04
a = abs(-1.502/f)
plt.plot(a,b, label = 'Theoretical Value')

plt.xlabel("Induced Current (μA)")
plt.ylabel("Velocity of Bar Magnet (m/s)")

plt.axis([0,4,0,0.35])

plt.title("figure 2.6")

plt.legend()
plt.show()
'''
