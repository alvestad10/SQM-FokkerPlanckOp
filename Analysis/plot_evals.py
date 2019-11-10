import os
import numpy as numpy
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

MODEL = 'LM_AHO'
ROOT_DATA = os.path.join('../Data/', MODEL)
columns = ["Re","Im"]

N_evals = 10
N = 495


for i in range(10,N,10):
    df = pd.read_csv(os.path.join(ROOT_DATA,"EVal_sig_1_i" + str(0) + '_N_' + str(i)), header=None, names=columns)[0:N_evals].reset_index()
    df['N'] = i
    if (i==240):
        all_ev = df
        print(all_ev.head())
    else:
        all_ev = pd.concat([all_ev,df])

all_ev.Re = all_ev.Re*(-1)
all_ev.Im = all_ev.Im*(-1)

sns.scatterplot(data=all_ev, x="N", y="Re", hue="index")
plt.show()