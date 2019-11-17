import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import xlrd

plt.rc('text', usetex = True)
plt.rc('font', size=20, family = 'serif')
plt.rc('text.latex',unicode=True)
plt.rc('legend', fontsize=20)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel} \usepackage{amsmath}')

# import data
book = xlrd.open_workbook('data/pole_prot.xlsx','r')
sheet = book.sheet_by_index(0)
# for rownum in range(sheet.nrows):
    # row = sheet.row_values(rownum)
E2 = [float(i) for i in sheet.row_values(36)[1:] if i != '']
u = np.array(E2)/10
t1 = [float(i) for i in sheet.row_values(37)[1:] if i != '']
t2 = [float(i) for i in sheet.row_values(38)[1:] if i != '']

plt.figure(figsize = (10,6))
plt.plot(u,t1,'ro',label='$t_1$')
plt.plot(u,t2,'ks',label='$t_2$')

# plt.xscale('log')
plt.legend()
plt.grid(which = 'both')
# plt.ylim(0,5)
# plt.hlines(y = 4.27/2,xmin = 11.7,xmax = 1.09e6,linestyles='--',lw = 2)
plt.xlabel(r'$U_{\text{з}},\text{ В}$')
plt.ylabel(r'$t,\text{мкс}$')
plt.savefig('fig/task6.png',dpi=500)

plt.show()

