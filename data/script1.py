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
i05 = [float(i) for i in sheet.row_values(2)[1:] if i != '']
u05 = [float(i) for i in sheet.row_values(3)[1:] if i != '']
i2 = [float(i) for i in sheet.row_values(5)[1:] if i != '']
u2 = [float(i) for i in sheet.row_values(6)[1:] if i != '']
i10 = [float(i) for i in sheet.row_values(8)[1:] if i != '']
u10 = [float(i) for i in sheet.row_values(9)[1:] if i != '']


plt.figure(figsize = (10,7))
plt.plot(u05,i05,'r-o',label='$U_c = 0.5$ V')
plt.plot(u2,i2,'k-o',label='$U_c = 2$ V')
plt.plot(u10,i10,'b-o',label='$U_c = 10$ V')

plt.legend()
plt.grid(which = 'both')
plt.xlabel(r'$U_{\text{з}}, V$')
plt.ylabel(r'$I_c, mA$')
plt.savefig('fig/task1.png',dpi=500)

plt.show()

