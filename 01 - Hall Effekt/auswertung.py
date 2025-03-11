import numpy as np
import matplotlib.pyplot as plt
from math import log

def regression(x,y):
    if len(x) != len(y):
        print("Fehler bei Regression")
        exit()
    
    xm = sum(x)/len(x)
    ym = sum(y)/len(y)
    
    d1 = 0
    d2 = 0
    for i in range(len(x)):
        d1 += (x[i] - xm)*(y[i] - ym)
        d2 += (x[i] - xm)**2
        
    return d1/d2, ym - d1/d2 * xm 









daten = [[-2.3, -1.6, -1.1, -0.5, 0.1, 0.8, 1.4, 1.9, 2.6,3.2,3.8],[-7.6, -5.8, -3.8, -2.0, 0, 1.8, 3.7,5.5, 7.4, 9.3, 11.2],[-13.4, -10.2, -6.9, -3.6, -0.3, 3.0, 6.2, 9.4, 12.8, 16.0, 19.2],[-19.2, -14.6, -9.9, -5.2, -0.6, 3, 8.7, 13.3, 18.1,22.7, 27.3],[-25.4, -19.3, -13.2, -7.0, -1.0, 5.2, 11.3, 17.6,23.7, 29.8, 35.8],[-30.6, -23.5, -16.0, -8.6, -1.3, 6.2, 13.7, 21.1, 28.5, 35.9, 43.2],[-36, -27.5, -18.9, -10.1, -1.6, 7.2, 16.0, 24.6, 33.3, 42.0, 50.6]]


I = [2,7,12,17,22,27,32]
B = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
f = open("messungen.tex", "w")

f.write("I")
for value in B:
    f.write( " & $U_{" + str(value) + "}$")

f.write("\\\\\n\hline")

for i in range(len(daten)):
    line = str(I[i]) + " "
    for j in range(len(daten[i])):
        line += " & " + str('{:0.1f}'.format(daten[i][j]))
    line += "\\\\ \n" 
    f.write(line)
f.close()
    


daten_t = []
for i in range(len(daten[0])): #assume all rows with equal length
    col = []
    for row in daten:
        col.append(row[i])
    daten_t.append(col)
    
print(daten_t)




fig, ax = plt.subplots()
for i in range(len(daten_t)):
    ax.plot(I, daten_t[i], color=[i/11.0,0, (1-i/11.0)])

ax.legend(["-250 mT", "-200 mT", "-150 mT", "-100 mT", "-50 mT", "0 mT", "50 mT", "100 mT", "150 mT", "200 mT", "250 mT" ], loc='lower left', ncol=2, prop={'size': 8})
#ax.plot(freq[4], e*nst[4], color='orange', marker='o', linewidth=0)

ax.set_xlabel('Querstrom I / mA')
ax.set_ylabel('Hallspannung / mV')
plt.savefig("regression_I.png")
plt.close()






fig, ax = plt.subplots()
for i in range(len(daten)):
    ax.plot(B, daten[i], color=[(7-i)/7, (165 + 90/7*i)/255.0, 0 ])

ax.legend(["2 mA", "7 mA", "12 mA", "17 mA", "22 mA", "27 mA", "32 mA"], loc='lower right', ncol=2, prop={'size': 10})
#ax.plot(freq[4], e*nst[4], color='orange', marker='o', linewidth=0)

ax.set_xlabel('Magnetische Flussdichte / mT')
ax.set_ylabel('Hallspannung / mV')
plt.savefig("regression_B.png")
plt.close()




e = 1.602176634*10**-19
d = 1 #mm

hall_const = []
ladungstr = []
f = open("auswertung_B_U.tex", "w")
for i in range(len(daten)):
    k, d = regression(B, daten[i])
    f.write(str(I[i]) + " & " + str('{:0.0f}'.format(k*10**3)) + " & " +  str('{:0.2f}'.format(k*10**3/I[i])) + " $\\cdot 10^{-3}$ & " + str('{:0.0f}'.format( 10**-19 *(e*k/I[i])**-1 )) + "$\\cdot 10^{19}$ \\\\")
    hall_const.append(k*10**3/I[i])
    ladungstr.append((e*k/I[i])**-1)

f.close()
hall_const = hall_const[1:]
ladungstr = ladungstr[1:]

f = open("ergebnis.tex", "w")
f.write("\\begin{align*}\n")
f.write("R_H &= (" + str('{:0.2f}'.format(sum(hall_const)/len(hall_const))) + " \pm " + str('{:0.2f}'.format(np.array(hall_const).std())) + ")\\cdot 10^{-3} ~\\text{m}^3/\\text{C} \\\\\n")
f.write("p &= (" + str('{:0.0f}'.format(10**-19*sum(ladungstr)/len(ladungstr))) + "\\pm" + str('{:0.0f}'.format(10**-19*np.array(ladungstr).std())) +  ") \\cdot 10^{19} ~\\text{m}^{-3}")
f.write("\n\\end{align*}")
f.close()
