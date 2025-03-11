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


def analyze_color(col1, col2, col_name, col_name_eng, regr_num):
    col1 = [-i for i in col1]
    col2 = [-i for i in col2]

    col1_regression = col1[-regr_num:]
    col2_regression = col2[-regr_num:]


    k, d = regression(col1_regression, col2_regression)
    print(col_name)
    print(k)
    print(d)

    nullstelle = (min(col2)-d)/k
    
    fig, ax = plt.subplots() 
    plt.axhline(y=min(col2), color='gray')
    plt.axvline(x=nullstelle, color='gray')

    ax.plot([i for i in np.arange(nullstelle, max(col1), 0.01)], [k*i + d for i in np.arange(nullstelle, max(col1), 0.01)], 'gray')
    ax.plot(col1, col2, col_name_eng, marker='o')


    ax.set_xlabel('Gegenspannung / V')
    ax.set_ylabel('Photospannung ' + col_name + ' / V')
    plt.savefig(col_name_eng + ".png")
    plt.close()
    return -nullstelle


names = []
nst = []
freq = []

purple1 = [1.650, 1.603, 1.578, 1.540, 1.501, 1.478, 1.447, 1.432, 1.431, 1.387, 1.337, 1.293, 1.250, 1.231, 1.194, 1.149]
purple2 = [0.024, 0.023, 0.023, 0.022, 0.019, 0.015, 0.007, -0.001, -0.008, -0.042, -0.112, -0.197, -0.286, -0.323, -0.400, -0.498]

nst.append(analyze_color(purple1, purple2, 'Violett', 'purple', 6))
names.append('Violett')
freq.append(7.41*10**14)


blue1 = [1.445, 1.375, 1.333, 1.304, 1.281, 1.266, 1.244, 1.232, 1.220, 1.214, 1.203, 1.186, 1.165, 1.149, 1.142, 1.123, 1.102, 1.079, 1.060, 1.018]
blue2 = [0.032, 0.028, 0.021, 0.008, -0.010, -0.028, -0.067, -0.097, -0.135, -0.157, -0.200, -0.271, -0.362, -0.440, -0.474, -0.563, -0.666, -0.791, -0.892, -1.101]

nst.append(analyze_color(blue1, blue2, 'Blau', 'blue', 6))
names.append('Blau')
freq.append(6.88*10**14)


bluegreen1 = [1.235, 1.180, 1.124, 1.073, 1.026, 0.986, 0.964, 0.928, 0.884, 0.840, 0.804, 0.772, 0.727, 0.712, 0.687, 0.637, 0.585, 0.569, 0.532, 0.518, 0.498, 0.484]
bluegreen2 = [0.015, 0.016, 0.016, 0.016, 0.006, -0.004, -0.011, -0.023, -0.052, -0.074, -0.110, -0.159, -0.190, -0.216, -0.262, -0.307, -0.363, -0.421, -0.439, -0.466, -0.494, -0.509]

nst.append(analyze_color(bluegreen1, bluegreen2, 'Cyan', 'cyan', 11))
names.append('Cyan')
freq.append(6.08*10**14)



green1 = [0.944,0.872,0.832, 0.813, 0.762, 0.728, 0.686, 0.653, 0.615, 0.579, 0.541, 0.518, 0.485, 0.455, 0.405, 0.390, 0.348, 0.327, 0.311]
green2 = [0.015,0.015,0.015, 0.009, 0.000, -0.008, -0.019, -0.031, -0.059, -0.104, -0.136, -0.145, -0.173, -0.197, -0.245, -0.257, -0.318, -0.334, -0.352]

nst.append(analyze_color(green1, green2, 'Gruen', 'green', 10))
names.append('Gruen')
freq.append(5.49*10**14)

yellow1 = [0.753, 0.706, 0.667, 0.627, 0.598, 0.556, 0.532, 0.513, 0.493, 0.471, 0.461, 0.427]
yellow2 = [0.011, 0.011, 0.010, 0.005, 0.000, -0.010, -0.017, -0.025, -0.033, -0.042, -0.050, -0.075]

nst.append(analyze_color(yellow1, yellow2, 'Gelb', 'orange', 6))
names.append('Gelb')
freq.append(5.19*10**14)


f = open("null.tex", "w")
for i in range(5):
    print(names[i] + "      \t" + str(nst[i]) + "      \t" + str(freq[i]*10**-14))
    f.write(str(names[i]) + " & " + str(freq[i]*10**-14)  + " & " + str('{:.3f}'.format(round(nst[i], 3))))
    f.write("\\\\\n")
f.close()

e = 1.60217733 * 10**-19
k, d = regression(freq,[i*e for i in nst])

print("h= " + str(k) + "Js")
print("W= " + str(d) + " J")


fig, ax = plt.subplots() 
#plt.axhline(y=min(col2), color='gray')
#plt.axvline(x=nullstelle, color='gray')

#ax.plot([i for i in np.arange(nullstelle, max(col1), 0.01)], [k*i + d for i in np.arange(nullstelle, max(col1), 0.01)], 'gray')
ax.plot([-i for i in purple1], [-i for i in purple2], 'purple', marker='o', markersize=3)
ax.plot([-i for i in blue1], [-i for i in blue2], 'blue', marker='o', markersize=3)
ax.plot([-i for i in bluegreen1], [-i for i in bluegreen2], 'cyan', marker='o', markersize=3)
ax.plot([-i for i in green1], [-i for i in green2], 'green', marker='o', markersize=3)
ax.plot([-i for i in yellow1], [-i for i in yellow2], 'orange', marker='o', markersize=3)


ax.set_xlabel('Gegenspannung / V')
ax.set_ylabel('Photostrom (als Spannung gemessen) / V')
plt.savefig("alle.png")
plt.close()






Delta_nst = 0.100
Delta_freq = 0.1*10**14

fig, ax = plt.subplots() 
ax.plot([i for i in [min(freq), max(freq)]],[k*i+d for i in [min(freq), max(freq)]], color='gray')

ax.plot(freq[0], e*nst[0], color='purple', marker='o', linewidth=0)
ax.plot(freq[1], e*nst[1], color='blue', marker='o', linewidth=0)
ax.plot(freq[2], e*nst[2], color='cyan', marker='o', linewidth=0)
ax.plot(freq[3], e*nst[3], color='green', marker='o', linewidth=0)
ax.plot(freq[4], e*nst[4], color='orange', marker='o', linewidth=0)


ax.plot([freq[0]+Delta_freq, freq[4]-Delta_freq],[e*(nst[0]-Delta_nst), e*(nst[4]+Delta_nst)], marker='o', markersize=2, linewidth=0.5,color='gray')

ax.plot([freq[0]-Delta_freq, freq[4]+Delta_freq],[e*(nst[0]+Delta_nst), e*(nst[4]-Delta_nst)], marker='o', markersize=2, linewidth=0.5,color='gray')



ax.set_xlabel('Frequenz / 10^14 Hz')
ax.set_ylabel('Stopspannung / eV')
plt.savefig("regression.png")
plt.close()


k1 =  ( e*(nst[4]+Delta_nst) - e*(nst[0]-Delta_nst) ) / ( freq[4]-Delta_freq - freq[0]+Delta_freq) 
k2 = ( e*(nst[4]-Delta_nst) - e*(nst[0]+Delta_nst) ) / ( freq[4]+Delta_freq - freq[0]-Delta_freq)
Delta_k = (k2-k1)/2 
Delta_d = Delta_k* ( sum(freq)/len(freq))

f = open("regressionsgerade.tex", "w")
f.write("\\begin{align*}\\\\\nk &= " + str('{:.3f}'.format(round(k*10**34,3))) + "\\cdot 10^{-34}~\\text{Js}\\\\\nd &= " + str('{:.3f}'.format(round(d*10**19,3))) + "\\cdot 10^{-19}~\\text{J}\n\\\\\end{align*}")
f.close()
f = open("ergebnis.tex", "w")
f.write("\\begin{align*}\\\\\nh &= (" + str('{:.3f}'.format(round(k*10**34,3))) + " \pm " + str('{:.3f}'.format(round(Delta_k*10**34,3))) + ") \\cdot 10^{-34}~\\text{Js}\\\\\nW &= (" + str('{:.3f}'.format(round(abs(d)*10**19,3))) + "\pm " + str('{:.3f}'.format(round(abs(Delta_d)*10**19,3)))+ ") \\cdot 10^{-19}~\\text{J}\n\\\\\end{align*}")
f.close()

