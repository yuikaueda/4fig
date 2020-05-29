import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
   
#del matplotlib.font_manager.weight_dict['roman']
#matplotlib.font_manager._rebuild()
  
def tanh(x):
    y = (np.exp(x)-np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return y

x = np.linspace(0, 11, 100)
y = np.linspace(-10, 11, 100)
X, Y = np.meshgrid(x,y)
Z = Y*(X-1)/(X+1)
#plt.style.use('classic')
#plt.gca().set_aspect('equal', adjustable='box')
#fig, ax = plt.subplots(1, 1)

#plt.ylim([-10,10])
#plt.xlim([1,10])

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='gaussian',cmap=cm.Greys,
               origin='lower', extent=[0,10, -10, 10],
               vmax=abs(Z).max(), vmin=-abs(Z).max())
ax.grid(False)
plt.colorbar(im)
plt.xlabel(r'$\alpha$', fontsize=13)
plt.ylabel(r'$F_0$', fontsize=13)

plt.show()
fig.savefig("fig3gray.png", bbox_inches = 'tight')
#ax.axes.yaxis.set_ticks([])
#ax.set_yticks([1, 4])
#ax.set_yticklabels(['$E_1$','$E_2$'], fontsize=9)
#ax.set_xticks([-0.5])
#ax.set_xticklabels([r'$F_0$''\n$\Delta F$'], fontsize=9)
#plt.xlabel(r'$\alpha$', fontsize=13)
#plt.ylabel(r'$F_0$', fontsize=13)

#plt.contourf(xx, yy, z, cmap='gray')
#plt.show()
#fig.savefig("fig2a.png",bbox_inches="tight")

