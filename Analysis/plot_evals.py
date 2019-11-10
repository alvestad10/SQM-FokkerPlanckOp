import os
import numpy as numpy
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

MODEL = 'LM_AHO'
ROOT_DATA = os.path.join('../Data/', MODEL)
ROOT_FIGURES = os.path.join('../Figures/', MODEL)
columns = ["Re","Im"]

N_evals = 1
N = 500

i_0 = 10
steps = 10
for i in range(i_0,N,steps):
    df = pd.read_csv(os.path.join(ROOT_DATA,"EVal_sig_1_i" + str(0) + '_N_' + str(i)), header=None, names=columns).sort_values(by=['Re'], ascending = False)[0:N_evals].reset_index()
    df['N'] = i
    if (i==i_0):
        all_ev = df
        print(all_ev.head())
    else:
        all_ev = pd.concat([all_ev,df])

all_ev.Re = all_ev.Re*(-1)
all_ev.Im = all_ev.Im*(-1)

sns.scatterplot(data=all_ev, x="N", y="Re")#, hue="index")
plt.title("Lowest eigenvalue for given N")
plt.savefig(os.path.join(ROOT_FIGURES, 'EVal_gs_varyN_-100_100'))
plt.show()