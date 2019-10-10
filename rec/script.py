 
from pylab import *
from matplotlib import rc
import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')

rec = path.abspath('rec.xls')

df=read(rec, sheet_name=1,header=[0])
columns = df.columns
colors = ['#1459CC', '#FF006A', '#222222','darkblue']
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
for i in range(4):
    x = array(df.iloc[:,2*i])
    E = array(df.iloc[:,1+2*i])
    ax.plot(x, E,'o-',color = colors[i])
    
ax.set_xlabel(r' $x$, мм',fontsize=22)
ax.set_ylabel(r'$E$, a.u.',fontsize=22)
ax.grid(which='both')
plt.legend([r'$\nu=2634$ ГГц',r'$\nu=3000$ ГГц',r'$\nu=3067$ ГГц',r'$\nu=3075$ ГГц'],fancybox = False,shadow = False, framealpha = 1)
plt.savefig(path.join('task2'+'.pdf'))



df=read(rec, sheet_name=0,header=[0,1])
columns = df.columns
colors = ['#1459CC', '#FF006A', '#222222','darkblue']
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
for i in range(2):
    f = array(df.iloc[:,5*i])
    print(f)
    f=f[~np.isnan(f)]
    h = array(df.iloc[:,1+5*i])
    h=h[~np.isnan(h)]
    ax.plot(f, h,'o-',color = colors[i])
    
ax.set_xlabel(r' $\nu$, ГГц',fontsize=22)
ax.set_ylabel(r'$h,\text{см}^{-1}$ ',fontsize=22)
ax.grid(which='both')
plt.legend([r'$\l_1=22$ мм',r'$\l_2=8$ мм'],fancybox = False,shadow = False, framealpha = 1)
plt.savefig(path.join('task1'+'.pdf'))
plt.show()