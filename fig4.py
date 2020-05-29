import numpy as np
import matplotlib.pyplot as plt
   
#del matplotlib.font_manager.weight_dict['roman']
#matplotlib.font_manager._rebuild()
  
def tanh(x):
    y = (np.exp(x)-np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return y

x = np.linspace(-6, 21, 100)
y = x*x/(1.5*tanh(x-6)+2.5)
#plt.style.use('classic')
#plt.gca().set_aspect('equal', adjustable='box')
fig, ax = plt.subplots(1, 1)

plt.ylim([-3,30])
plt.xlim([-5,12])

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
#ax.set_yticks([1, 4])
#ax.set_yticklabels(['$E_1$','$E_2$'], fontsize=9)
#ax.set_xticks([-0.5])
#ax.set_xticklabels([r'$F_0$''\n$\Delta F$'], fontsize=9)
plt.xlabel('stress $\sigma$', fontsize=13)
plt.ylabel(r'energy', fontsize=13)

ax.plot(x, y, color='black')
plt.show()
fig.savefig("fig4.png",bbox_inches="tight")

