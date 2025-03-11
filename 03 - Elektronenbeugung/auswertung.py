import numpy as np
import matplotlib.pyplot as plt
from math import log,sqrt


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



h = 6.62607015 * 10**-34
me = 9.1093837015*10**-31
e = 1.602176634*10**-19

exp1_U = [2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00, 4.25, 4.50, 4.87]
delta1 =   [ 1,  3,  2,  1, 2, 3, 1, 1, 3, 3, 2]
delta2 =   [ 3,  3,  1,  3, 2, 3, 2, 1, 2, 1, 3]
exp1_d1 = [36, 35, 33, 31, 29, 27, 27, 26, 24, 21, 21]
exp1_d2 = [59, 58, 57, 52, 50, 48, 47, 46, 44, 41, 39]



#51.94
exp2_I1 = [25.28, 41.86, 51.94, 60.25, 78.5, 98.4, 120.9, 138.4, 162.5, 182.6, 194.8]
exp2_I2 = [23.95, 50.97, 75.80, 101.9, 128.0, 147.7, 176.1, 202.9, 223.7, 253.1, 272.4]

exp2_d1 = [14, 20, 21, 26, 33, 38, 51, 58, 64, 72, 77]
exp2_d2 = [8, 15, 23, 29, 38, 45, 52, 61, 72, 73, 77]


Delta_U = 0.05
exp1_d1_final = []
exp1_d2_final = []
exp1_gitterabst1 = []
exp1_gitterabst2 = []
lam = []
Delta_lam = []
for i in range(len(delta1)):
    exp1_d1_final.append(exp1_d1[i] - delta1[i]/2.0)
    exp1_d2_final.append(exp1_d2[i] - delta2[i]/2.0)
    
    lam.append( h / sqrt(2 * me * e * (1000*exp1_U[i])))
    Delta_lam.append( lam[i] * Delta_U/(2*(1000*exp1_U[i])))

for i in range(len(delta1)):
    exp1_gitterabst1.append(135*10**-3/(exp1_d1_final[i]/2.0*10**-3)*lam[i])
    exp1_gitterabst2.append(135*10**-3/(exp1_d2_final[i]/2.0*10**-3)*lam[i])


f = open("exp1.tex", "w")
f.write("\\begin{tabular}{r|rr|rr}\n")
f.write("$U$ / kV & $d_{\\text{innen},1}$ / mm & $d_{\\text{aussen},1}$ / mm & $d_{\\text{innen},2}$ / mm & $d_{\\text{aussen},2}$ / mm \\\\\n\hline\n")

for i in range(len(exp1_U)):
    f.write(str('%.2f' % exp1_U[i]) + " & " + str(exp1_d1[i]-delta1[i])  + " & " + str(exp1_d1[i]) + " & " + str(exp1_d2[i]-delta2[i]) + " & " + str(exp1_d2[i]) + "\\\\\n") 

f.write("\\end{tabular}\n")

f.close()


f = open("exp1_auswertung.tex", "w")
f.write("\\begin{tabular}{r|rrr}\n")
f.write("$U$ / kV & $d_1$ / mm & $d_2$ / mm  & $\lambda$ / pm \\\\\n\hline\n")

for i in range(len(exp1_U)):
    f.write(str('%.2f' % exp1_U[i]) + " & " + str('%.1f' % exp1_d1_final[i])  + " & " + str('%.1f' % exp1_d2_final[i]) + " & " + str('%.2f' % (lam[i]*10**12)) + "\\\\\n") 

f.write("\\end{tabular}\n")
f.close()



f = open("exp1_result.tex", "w")
f.write("\\begin{tabular}{r|rr}\n")
f.write("$\lambda$ / pm & $D_1$ / pm & $D_2$ / pm  \\\\\n\hline\n")

for i in range(len(exp1_U)):
    f.write(str('%.2f' % (10**12*lam[i])) + " & " + str('%.1f' % (10**12*exp1_gitterabst1[i]))  + " & " + str('%.1f' % (10**12*exp1_gitterabst2[i])) + "\\\\\n") 

f.write("\\end{tabular}\n")
f.close()


f = open("exp1_gitterabstand.tex", "w")
f.write("\\begin{align}\n")
f.write("D_1 &= \\left(" + str('%.2f' % (10**12*sum(exp1_gitterabst1)/len(exp1_gitterabst1))) + " \pm " + str('%.2f' % (10**12*np.std(np.array(exp1_gitterabst1)))) + "\\right)~\\text{pm}\\\\\n")
f.write("D_2 &= \\left(" + str('%.2f' % (10**12*sum(exp1_gitterabst2)/len(exp1_gitterabst2))) + " \pm " + str('%.2f' % (10**12*np.std(np.array(exp1_gitterabst2)))) + "\\right)~\\text{pm}\n")

f.write("\\label{eq:gitterabst_result}\n\\end{align}\n")
f.close()













f = open("exp2_messung.tex", "w")
f.write("\\begin{tabular}{r|r}\n")
f.write("$I_1$ / mA & $d_1$ / mm \\\\\n\hline\n")

for i in range(len(exp2_I1)):
    f.write(str('%.2f' % exp2_I1[i]) + " & " + str(exp2_d1[i]) + "\\\\\n") 

f.write("\\end{tabular}\\quad\\quad\\quad")

f.write("\\begin{tabular}{r|r}\n")
f.write("$I_2$ / mA & $d_2$ / mm \\\\\n\hline\n")

for i in range(len(exp2_I1)):
    f.write(str('%.2f' % exp2_I2[i]) + " & " + str(exp2_d2[i]) + "\\\\\n") 

f.write("\\end{tabular}\n")


f.close()




esp1 = []
esp2 = []
B1 = [] #T
B2 = []
r1 = [] #m^-1
r2 = []

H_const = 320*0.068**2/(0.068**2 + 0.034**2)**(3/2)
mu_0 = 	1.25663706212*10**-6
d_const = 135*10**-3

f = open("exp2_radius.tex", "w")
f.write("\\begin{tabular}{r|rrr}\n")
f.write("$I_1$ / mA & $s_1$ / mm & $r_1$ / mm & $B_1$ / $\mu$T \\\\\n\hline\n")

for i in range(len(exp2_I1)):
    f.write(str('%.2f' % exp2_I1[i]) + " & " + str('%.1f' % (exp2_d1[i]/2.0)) + " & " + str(round(1000*d_const * sqrt(d_const**2- (10**-3*exp2_d1[i]/2.0)**2)/(10**-3*2*exp2_d1[i]/2.0) )) + " & " + str(round(10**6 * mu_0 * H_const * exp2_I1[i]*10**-3)) + "\\\\\n") 
    B1.append(mu_0 * H_const * exp2_I1[i]*10**-3)
    r1.append( (d_const * sqrt(d_const**2- (10**-3*exp2_d1[i]/2.0)**2)/(10**-3*2*exp2_d1[i]/2.0))**-1 )
    esp1.append( (mu_0 * H_const * exp2_I1[i]*10**-3 * (d_const * sqrt(d_const**2- (10**-3*exp2_d1[i]/2.0)**2)/(10**-3*2*exp2_d1[i]/2.0)))**-2 * 4000)

f.write("\\end{tabular}\\quad\\quad\\quad")

f.write("\\begin{tabular}{r|rrr}\n")
f.write("$I_2$ / mA & $s_2$ / mm & $r_2$ / mm & $B_2$ / $\mu$T \\\\\n\hline\n")

for i in range(len(exp2_I2)):
    f.write(str('%.2f' % exp2_I2[i]) + " & " + str('%.1f' % (exp2_d2[i]/2.0)) + " & " + str(round(1000*d_const * sqrt(d_const**2- (10**-3*exp2_d2[i]/2.0)**2)/(10**-3*2*exp2_d2[i]/2.0) )) + " & " + str(round(10**6 * mu_0 * H_const * exp2_I2[i]*10**-3)) + "\\\\\n") 
    
    B2.append(mu_0 * H_const * exp2_I2[i]*10**-3)
    r2.append( (d_const * sqrt(d_const**2- (10**-3*exp2_d2[i]/2.0)**2)/(10**-3*2*exp2_d2[i]/2.0))**-1 )
    esp2.append( (mu_0 * H_const * exp2_I2[i]*10**-3 * (d_const * sqrt(d_const**2- (10**-3*exp2_d2[i]/2.0)**2)/(10**-3*2*exp2_d2[i]/2.0)))**-2 * 8000)

f.write("\\end{tabular}\n")
f.close()


print(sum(esp1)/len(esp1))
print(sum(esp2)/len(esp2))




k1, d1 = regression(B1, r1)
k2, d2 = regression(B2, r2)


fig, ax = plt.subplots()

ax.plot(np.array(B1)*10**6, r1, 'red', linewidth=0, marker='o')
ax.plot(np.array(B2)*10**6, r2, 'blue', linewidth=0, marker='o')

ax.plot(np.array(B1)*10**6, k1*np.array(B1)+d1, color='red', alpha=0.4)
ax.plot(np.array(B2)*10**6, k2*np.array(B2)+d2, color='blue', alpha=0.4)

ax.legend(['2 kV', '4 kV'])

ax.set_xlabel('B / µT')
ax.set_ylabel('r^-1 / m^-1')
plt.savefig("regression.png")
plt.close()



f = open("exp2_regression.tex", "w")
f.write("\\begin{align*}\n")
f.write("k_1 &= " + str(round(k1)) + "~\\text{m}^{-1}\\cdot \\text{T}^{-1} \\\\\n")
f.write("k_2 &= " + str(round(k2)) + "~\\text{m}^{-1}\\cdot \\text{T}^{-1} \n")

f.write("\\end{align*}\n")
f.close()



f = open("exp2_result.tex", "w")
f.write("\\begin{align*}\n")
f.write("e_{\\text{spez},1} &= (-" + str(round(10**-8*2*2000*k1**2)/1000.0) + "\\pm" + str(round(10**-8*2*2000*k1**2/9.3)/1000.0) + ")\\cdot 10^{11}~\\text{C}\\cdot \\text{kg}^{-1} \\\\\n")
f.write("e_{\\text{spez},2} &= (-" + str(round(10**-8*2*4000*k1**2)/1000.0) + "\\pm" + str(round(10**-8*2*2000*k2**2/8.5)/1000.0) + ")\\cdot 10^{11}~\\text{C}\\cdot \\text{kg}^{-1} \n")

f.write("\\end{align*}\n")
f.close()




exit(0)






