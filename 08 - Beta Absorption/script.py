import numpy as np
import matplotlib.pyplot as plt
from math import log
from math import sin,sqrt, exp

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

def approx_zero(x,y):
    k, d = regression(x,y)
    return -d/k



N = 1292
Delta_N = sqrt(1292)
hingergrund_strahlung_rate = N/3600


Al_dicke = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
Cu_dicke = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2]

Al_dauer = [2, 4, 4, 5, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 25, 45]
Cu_dauer = [2, 3, 6, 10, 10, 10, 15, 30, 30, 30, 30, 30, 40]

Al_rate = [175641, 253232, 177828, 107797, 256730, 217737, 177992, 159462, 126138, 108890, 94577, 57476, 21771, 7465, 2993, 1824, 1580, 1560, 1419, 2260, 4258]
Cu_rate = [167218, 46370, 50479, 44080, 25153, 10750, 8616, 7863, 4763, 3253, 2648, 2134, 2710]

Al_imp = []
Cu_imp = []

Al_imp_log = []
Cu_imp_log = []

for i in range(len(Al_dauer)):
    Al_imp.append(Al_rate[i]/(60*Al_dauer[i]) - hingergrund_strahlung_rate)
    Al_imp_log.append( log(Al_imp[-1]) )
    
for i in range(len(Cu_dauer)):
    Cu_imp.append(Cu_rate[i]/(60*Cu_dauer[i]) - hingergrund_strahlung_rate)
    Cu_imp_log.append( log(Cu_imp[-1]) )
    
    
    


fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(Al_dicke, Al_imp, 'green')
ax.plot(Al_dicke, Al_imp, 'green', linewidth=0, marker='o')
ax.set_xlabel('Dicke / mm')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("al_imp.png")
plt.close()


fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(Cu_dicke, Cu_imp, 'blue')
ax.plot(Cu_dicke, Cu_imp, 'blue', linewidth=0, marker='o')
ax.set_xlabel('Dicke / mm')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("cu_imp.png")
plt.close()





fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(Al_dicke, Al_imp_log, 'green')
ax.plot(Al_dicke, Al_imp_log, 'green', linewidth=0, marker='o')
ax.set_xlabel('Dicke / mm')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("al_imp_log.png")
plt.close()


fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(Cu_dicke, Cu_imp_log, 'blue')
ax.plot(Cu_dicke, Cu_imp_log, 'blue', linewidth=0, marker='o')
ax.set_xlabel('Dicke / mm')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("cu_imp_log.png")
plt.close()


rho_al = 2.7*100
rho_cu = 8.96*100

for i in range(len(Al_dicke)):
    print(str('%.1f' % Al_dicke[i]) + "\t & \t" +str(round(rho_al*Al_dicke[i])) + "\t & \t" + str(round(Al_imp[i])) + "\t & \t" + str(round(sqrt(Al_imp[i])))  + " \\\\")


print("")

for i in range(len(Cu_dicke)):
    print(str('%.1f' % Cu_dicke[i]) + "\t & \t" +str(round(rho_cu*Cu_dicke[i])) + "\t & \t" + str(round(Cu_imp[i])) + "\t & \t" + str(round(sqrt(Cu_imp[i]))) + " \\\\")




k_Al, d_Al = regression(np.array(Al_dicke[4:-6])*rho_al, Al_imp_log[4:-6])
k_Cu, d_Cu = regression(np.array(Cu_dicke[1:-3])*rho_cu, Cu_imp_log[1:-3])




fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(Al_dicke, Al_imp_log, 'green',alpha=0.3)
ax.plot(Al_dicke[4:-6], Al_imp_log[4:-6], 'green', linewidth=0, marker='o',alpha=.3)

ax.plot(Al_dicke[4:-6], np.array(Al_dicke[4:-6])*k_Al+d_Al, color='green')

ax.set_xlabel('Dicke / mm')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("al_imp_log_regression.png")
plt.close()


fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(Cu_dicke, Cu_imp_log, 'blue', alpha=.3)
ax.plot(Cu_dicke, Cu_imp_log, 'blue', linewidth=0, marker='o',alpha=.3)
ax.plot(Cu_dicke[1:-3], np.array(Cu_dicke[1:-3])*k_Cu+d_Cu, color='blue')

ax.set_xlabel('Dicke / mm')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("cu_imp_log_regression.png")
plt.close()












fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(rho_al*np.array(Al_dicke), Al_imp_log, 'green',alpha=0.3)
ax.plot(rho_al*np.array(Al_dicke[4:-6]), Al_imp_log[4:-6], 'green', linewidth=0, marker='o',alpha=.3)
ax.plot(np.array(Al_dicke[4:-6] + [-d_Al/k_Al]), list(np.array(Al_dicke[4:-6])*k_Al+d_Al) + [0], color='green')

ax.plot([-d_Al/k_Al ],[0], marker='x', color='green') 

ax.set_xlabel('Massendicke / mg/cm²')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("al_imp_log_regression_converted_x.png")
plt.close()


fig, ax = plt.subplots() 
#ax.axis([0, 34, 0, 3500])

ax.plot(rho_cu*np.array(Cu_dicke), Cu_imp_log, 'blue', alpha=.3)
ax.plot(rho_cu*np.array(Cu_dicke), Cu_imp_log, 'blue', linewidth=0, marker='o',alpha=.3)
ax.plot(np.array(Cu_dicke[1:-3] + [-d_Cu/k_Cu]), list(np.array(Cu_dicke[1:-3])*k_Cu+d_Cu) + [0], color='blue')

ax.plot([-d_Cu/k_Cu ],[0], marker='x') 

ax.set_xlabel('Massendicke / mg/cm²')
ax.set_ylabel('Rate / imp/s')
#ax.set_title('')
plt.savefig("cu_imp_log_regression_converted_x.png")
plt.close()







print("mu/rho:")
print(k_Al*1000)
print(k_Cu*1000)


print("E_0 (mu/rho):")
print((-17 / (k_Al*1000))**(1/1.14) )
print((-17 / (k_Cu*1000))**(1/1.14) )


print("\n\n")


print("R_eff, Al: " + str(-d_Al/k_Al ))
print("R_eff, Cu: " + str(-d_Cu/k_Cu ))


print("E_0: R_eff, Al: " + str((-d_Al/k_Al/412)**(1/1.38)))
print("E_0: R_eff, Cu: " + str((-d_Cu/k_Cu/412)**(1/1.38)))



