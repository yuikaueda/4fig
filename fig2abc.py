import numpy as np
import matplotlib.pyplot as plt
   
#del matplotlib.font_manager.weight_dict['roman']
#matplotlib.font_manager._rebuild()
  
def tanh(x):
    y = (np.exp(x)-np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return y

x = np.linspace(-1, 21, 100)
y1 = x/(0.5*tanh(x/2-3)+1.5)
y2 = x/(0.25*tanh(x/2-3)+1.25)
y3 = x/(1.5*tanh(x/2-3)+2.5)

c1,c2,c3 = "blue","green","red"
l1,l2,l3 = r"$\Delta F=\frac{\alpha - 1}{\alpha + 1}F_0$",r"$\Delta F>\frac{\alpha - 1}{\alpha + 1}F_0$",r"$\Delta F<\frac{\alpha - 1}{\alpha + 1}F_0$"
#plt.style.use('classic')
#plt.gca().set_aspect('equal', adjustable='box')
fig, ax = plt.subplots(1, 1)

plt.ylim([0,9])
plt.xlim([0,12])

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
#ax.set_yticks([1, 4])
#ax.set_yticklabels(['$E_1$','$E_2$'], fontsize=9)
#ax.set_xticks([-0.5])
#ax.set_xticklabels([r'$F_0$''\n$\Delta F$'], fontsize=9)
plt.xlabel('stress $\sigma$', fontsize=15)
plt.ylabel(r'strain $\varepsilon$', fontsize=15)

ax.plot(x, y1, color=c1, label=l1)
ax.plot(x, y2, color=c2, label=l2)
ax.plot(x, y3, color=c3, label=l3)
ax.legend(loc=0)
plt.show()
fig.savefig("fig2abc.png",bbox_inches="tight")

