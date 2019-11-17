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
i0 = [float(i) for i in sheet.row_values(13)[1:] if i != '']
u0 = [float(i) for i in sheet.row_values(14)[1:] if i != '']
i05 = [float(i) for i in sheet.row_values(16)[1:] if i != '']
u05 = [float(i) for i in sheet.row_values(17)[1:] if i != '']
i15 = [float(i) for i in sheet.row_values(19)[1:] if i != '']
u15 = [float(i) for i in sheet.row_values(20)[1:] if i != '']
i1 = [float(i) for i in sheet.row_values(22)[1:] if i != '']
u1 = [float(i) for i in sheet.row_values(23)[1:] if i != '']


plt.figure(figsize = (10,7))
plt.plot(u0,i0,'k-s',label=r'$U_{\text{з}} = 0$ V')
plt.plot(u05,i05,'r-o',label=r'$U_{\text{з}} = 0.5$ V')
plt.plot(u1,i1,'b-o',label=r'$U_{\text{з}} = 1$ V')
plt.plot(u15,i15,'g-o',label=r'$U_{\text{з}} = 1.5$ V')

plt.legend()
plt.grid(which = 'both')
plt.xlabel(r'$U_c, V$')
plt.ylabel(r'$I_c, mA$')
plt.savefig('fig/task2.png',dpi=500)

plt.show()

