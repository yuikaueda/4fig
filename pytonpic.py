import numpy as np
import matplotlib.pyplot as plt

#del matplotlib.font_manager.weight_dict['roman']
#matplotlib.font_manager._rebuild()

def tanh(x):
    y = (np.exp(x)-np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return y
x = np.linspace(-7, 13, 100)
y = 1.5*tanh(x/2+0.5)+2.5

#plt.style.use('classic')
#plt.gca().set_aspect('equal', adjustable='box')
fig, ax = plt.subplots(1, 1)
#plt.plot(x, 1.5*tanh(x/2+0.5)+2.5)
plt.ylim([-0,5])
plt.xlim([-6,12])
#plt.plot(x, x*(1-x))
ax.set_yticks([1, 4])
ax.set_yticklabels(['$E_1$','$E_2$'], fontsize=13)
ax.set_xticks([-0.5])
ax.set_xticklabels([r'$F_0$''\n$2\Delta F$'], fontsize=13)
plt.xlabel('force $F$', fontsize=15)
plt.ylabel('Elastic modulus $E$', fontsize=15)

#plt.legend(["r=4", "r=1"])
#ax.grid()
ax.plot(x, y, color='black')
plt.show()
fig.savefig("fig1.png",bbox_inches="tight")
