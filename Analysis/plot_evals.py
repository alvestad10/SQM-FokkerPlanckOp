import os
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

MODEL = 'LM_HO'
ROOT_DATA = os.path.join('../Data/', MODEL)
ROOT_FIGURES = os.path.join('../Figures/', MODEL)
columns = ["Re","Im"]

N_evals = 50
N = 250
i_0 = 0
steps = 1
x_min = -100
x_max = 100
K="sig*"
F=True
Re_Im = "Re"

sig_cos_sin = True

for i in range(i_0,48,steps):

    # Construct filename
    filename = "EVal"
    if F:
        filename += '_F'

    if sig_cos_sin:
        filename += "_sig_cos("+ str(i) + "pi_" + str(24) +")_isin("+ str(i) + "pi_"+ str(24) +")"
    else:
        filename += "_sig_" + str(1) + "_i" + str(i)
    
    if N:
        filename += "_N_" + str(N)

    if K != "1":
        filename += "_K_" + K

    #df = pd.read_csv(os.path.join(ROOT_DATA,"EVal_sig_1_i" + str(0) + '_N_' + str(i)), header=None, names=columns).sort_values(by=['Re'], ascending = False)[0:N_evals].reset_index()
    df = pd.read_csv(os.path.join(ROOT_DATA,filename), header=None, names=columns)[0:N_evals].reset_index()

    df['N'] = i/(48) #np.cos(i*np.pi/24)
    if (i==i_0):
        all_ev = df
        print(all_ev.head())
    else:
        all_ev = pd.concat([all_ev,df])

all_ev.Re = all_ev.Re*(-1)
all_ev.Im = all_ev.Im*(-1)

#sns.scatterplot(data=all_ev, x="N", y="Re")#, hue="index")
sns.lineplot(data=all_ev, x="N", y="Re", hue="index")
#all_ev.plot.scatter(x="Re", y="Im", c="N")
#plt.title("Lowest eigenvalue for given N")
#plt.title("Varying Complex part of sigma")
plt.title("Vary sigma on unit circle")


plot_filename = "EVal"
if F:
    plot_filename += '_F'

plot_filename += "_" + Re_Im

if sig_cos_sin:
    plot_filename += "_sig_cos_isin_n_" + str(48)
else:
    plot_filename += "_sig_" + str(1) + "_i" + str(0) + "-" + str(20)

plot_filename += "_NEvals_" + str(N_evals)

if N:
    plot_filename += "_N_" + str(N)

plot_filename += "_K_" + K

plot_filename += "_on_"+ str(x_min) +'-'+ str(x_max)

#plt.savefig(os.path.join(ROOT_FIGURES, 'EVal_sigma_1_i0-20_NEvals_8_on_-100_100'))
plt.savefig(os.path.join(ROOT_FIGURES, plot_filename))
plt.show()