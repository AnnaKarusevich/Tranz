import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
fig = plt.figure() 
ax = fig.add_subplot(111) 

x=np.array([0,0.1,0.2,0.3,0.36,0.38,0.4,0.42]) 
y=np.array([0,0,4,20,38,64,76,100]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='blue', lw=0.5, mfc='white', ms=3) 


# x=np.array([0,-2,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100]) 
# y=np.array([0,-20,-22,-22,-24,-24,-25,-26,-26,-27,-28,-28]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='black', lw=0.5, mfc='white', ms=3) 


# x=np.array([0,19.8,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27]) 
# y=np.array([0,0.008,0.015,0.022,0.033,0.059,0.071,0.092,0.13,0.17,0.227,0.301,0.375,0.455,0.62,0.74,0.985]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 

# plt.legend(('$\phi_з=40В$','$\phi_з=45В$','$\phi_з=50В$'),loc=(0.1,0.4))

ax.plot(x,y,'ko', color = "crimson", markersize=4) 
plt.title('Прямой ход ВАХ (нагретый диод)')
plt.ylabel('$J$,мА') 
plt.xlabel('$U$,В') 
plt.grid () 
plt.xlim([0,1]) 
plt.ylim([0,102]) 
plt.savefig('31.png',dpi=300)
plt.show()