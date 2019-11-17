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
f = [float(i) for i in sheet.row_values(31)[1:] if i != '']
u = [float(i) for i in sheet.row_values(32)[1:] if i != '']
u = np.array(u)/2 
K = u/0.2

plt.figure(figsize = (10,7))
plt.plot(f,K,'ro')

plt.xscale('log')
plt.grid(which = 'both')
plt.ylim(0,5)
plt.hlines(y = 4.27/2,xmin = 11.7,xmax = 1.09e6,linestyles='--',lw = 2)
plt.xlabel(r'$f, \text{Гц}$')
plt.ylabel(r'$K$')
plt.savefig('fig/task4.png',dpi=500)

plt.show()

