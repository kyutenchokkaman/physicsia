# -*- coding:utf-8 -*-

f1 = open('data_macro.csv', 'r')
f2 = open('data_micro.csv', 'r')

of1 = open('processed_da.csv', 'w')
of2 = open('processed_di.csv', 'w')

of1.write("Induced Current (μA),Frames Taken (1/30 s),Starting Point (cm),Ending Point (cm),0.01*|S-E|/f*30 (m/s) \n")
of2.write("Induced Current (μA),Frames Taken (1/30 s),0.005 / f*30 (m/s) \n")

f1.readline()
f2.readline()

l1 = f1.readlines()
l2 = f2.readlines()

for j in l1:
    j = j.replace("\n", "")
    j = j.split(",")
    u0 = round(10/float(j[0])+2.5, 3)
    u1 = round(2/float(j[1])*100, 3)
    u2 = round(20/float(j[2]), 3)
    u3 = round(20/float(j[3]), 3)
    row = "{},{},{},{},{}\n".format(
        str(round(float(j[0]),3))+"±"+str(u0)+"%",
        str(round(float(j[1]),3))+"±"+str(u1)+"%",
        str(round(float(j[2]),3))+"±"+str(u2)+"%",
        str(round(float(j[3]),3))+"±"+str(u3)+"%",
        str(round(float(j[4]),3))+"±"+str(round(u0+u1+u2+u3, 3))+"%",
        )
    of1.write(row)

for i in l2:
    i = i.replace("\n", "")
    i = i.split(",")

    t0 = round(10/float(i[0])+2.5,3)
    t1 = round(100/float(i[1]),3)
    row = "{},{},{}\n".format(
        str(round(float(i[0]), 3))+"±"+str(t0)+"%",
        str(round(float(i[1]), 3))+"±"+str(t1)+"%",
        str(round(float(i[2]),3))+"±"+str(t1+10)+"%",
        )
    of2.write(row)

f1.close()
of1.close()
f2.close()
of2.close()
