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



def read_file(name):
    f = open(name, "r")
    data = f.read()
    f.close()

    lines = data.split("\n")
    lines.pop(0)

    UA_list = []
    UB_list = []
    
    for line in lines:
        element = line.split(";")
        if len(element) > 2:
            UA = float(element[1].replace(',', '.'))
            UB = float(element[2].replace(',', '.'))
            UA_list.append(UA)
            UB_list.append(UB)
    return UA_list, UB_list



def umrechnung(UA, UB):
    sigma = []
    rho = []
    T = []
    
    I_q = 3 #mA
    for i in range(len(UA)):
        sigma.append(I_q/UB[i] * 2)
        rho.append( (I_q/UB[i] * 2)**-1 )
        T.append(UA[i]*100+273.15)
    return sigma,rho,T

undotiert_UA, undotiert_UB = read_file("undotiert.csv")
p_dotiert_UA, p_dotiert_UB = read_file("pdotiert.csv")
n_dotiert_UA, n_dotiert_UB = read_file("ndotiert.csv")

undotiert_sigma, undotiert_rho, undotiert_T = umrechnung(undotiert_UA,undotiert_UB)
p_dotiert_sigma, p_dotiert_rho, p_dotiert_T = umrechnung(p_dotiert_UA,p_dotiert_UB)
n_dotiert_sigma, n_dotiert_rho, n_dotiert_T = umrechnung(n_dotiert_UA,n_dotiert_UB)




def transformation(sigma,T):
    logsigma = []
    Tinv = []
    
    for i in range(len(sigma)):
        logsigma.append(log(sigma[i]))
        Tinv.append(1/T[i])
    
    return logsigma, Tinv


fig, ax = plt.subplots()

ax.plot(undotiert_UA, undotiert_UB, 'gray')
ax.plot(p_dotiert_UA, p_dotiert_UB, 'red')
ax.plot(n_dotiert_UA, n_dotiert_UB, 'blue')

ax.legend(['undotiert', 'p-dotiert', 'n-dotiert'])

ax.set_xlabel('UA / V')
ax.set_ylabel('UB / V')
plt.savefig("data_raw.png")
plt.close()




fig, ax = plt.subplots()
plt.xlim(0.9,1.6)
plt.ylim(0,0.4)
ax.plot(undotiert_UA, undotiert_UB, 'gray')
ax.plot(p_dotiert_UA, p_dotiert_UB, 'red')
ax.plot(n_dotiert_UA, n_dotiert_UB, 'blue')

ax.legend(['undotiert', 'p-dotiert', 'n-dotiert'])

ax.set_xlabel('UA / V')
ax.set_ylabel('UB / V')
plt.savefig("data_scaled.png")
plt.close()







fig, ax = plt.subplots()

ax.plot(undotiert_T, undotiert_sigma, 'gray')
ax.plot(p_dotiert_T, p_dotiert_sigma, 'red')
ax.plot(n_dotiert_T, n_dotiert_sigma, 'blue')

ax.legend(['undotiert', 'p-dotiert', 'n-dotiert'])

ax.set_xlabel('T / K')
ax.set_ylabel('sigma / Sm^-1')
plt.savefig("leitfaehigkeit.png")
plt.close()



fig, ax = plt.subplots()

ax.plot(undotiert_T, undotiert_rho, 'gray')
ax.plot(p_dotiert_T, p_dotiert_rho, 'red')
ax.plot(n_dotiert_T, n_dotiert_rho, 'blue')

ax.legend(['undotiert', 'p-dotiert', 'n-dotiert'])

ax.set_xlabel('T / K')
ax.set_ylabel('rho / Ohm m')
plt.savefig("widerstand.png")
plt.close()



logsigma, Tinv = transformation(undotiert_sigma, undotiert_T)

k_B = 1.380649 * 10**-23
e = 1.602176634 * 10**-19
k,d = regression(Tinv, logsigma)
print(k)

E_G = -2*k_B*k

print(E_G)
print(E_G/e)


fig, ax = plt.subplots()

ax.plot([0.0024,0.003], [d+k*0.0024, d+k*0.003])
ax.plot(Tinv, logsigma, 'green')

ax.set_xlabel('1/T / K^-1')
ax.set_ylabel('log(sigma) / 1')
plt.savefig("regression.png")
plt.close()




exit(0)



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
