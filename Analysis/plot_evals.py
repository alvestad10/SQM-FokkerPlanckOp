import os
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

MODEL = 'LM_AHO'
ROOT_DATA = os.path.join('../Data/', MODEL)
ROOT_FIGURES = os.path.join('../Figures/', MODEL)
columns = ["Re","Im"]

# Testing specifics
N_evals = 1
N_lowest_eval = 0
i_min = 10
i_max = 4100
steps = 10

# Lattice parameters
#N = 250
x_min = -100
x_max = 100
x_min_max = False

# Other parameters
K="1"
F=False
H=False
Re_Im = "Re"

# Select which type of testing
sig_cos_sin = False
vary_sig_Im = False
vary_N = True

for i in range(i_min,i_max,steps):

    if (i == 800):
        x_min_max = True
        H = True
    
    if (i>800):
        if i%100 != 0: continue

    if vary_N:
        N = i

    # Construct filename
    filename = "EVal"
    if F:
        filename += '_F'
    elif H:
        filename += '_H'

    if sig_cos_sin:
        filename += "_sig_cos("+ str(i) + "pi_" + str(24) +")_isin("+ str(i) + "pi_"+ str(24) +")"
    elif vary_sig_Im:
        filename += "_sig_" + str(1) + "_i" + str(i)
    elif vary_N:
        filename += "_sig_" + str(1) + "_i" + str(0)    
    
    if N:
        filename += "_N_" + str(N)

    if K != "1":
        filename += "_K_" + K
    
    if x_min_max:
        filename += "_on_" + str(x_min) + "-" + str(x_max)

    df = pd.read_csv(os.path.join(ROOT_DATA,filename),
                     header=None,
                     names=columns).sort_values(by=['Re'], ascending = False)\
                                   .reset_index(drop=True)[N_lowest_eval:N_lowest_eval + N_evals]\
                                   .reset_index()

    if sig_cos_sin:
        df['N'] = i/(48)
    elif vary_sig_Im or vary_N:
        df['N'] = N

    if (i==i_min):
        all_ev = df
    else:
        all_ev = pd.concat([all_ev,df])

all_ev.Re = all_ev.Re*(-1)
all_ev.Im = all_ev.Im*(-1)

#sns.scatterplot(data=all_ev, x="N", y="Re")#, hue="index")
#sns.lineplot(data=all_ev, x="N", y="Re", hue="index")
#all_ev.plot.scatter(x="Re", y="Im", c="N")
#
if sig_cos_sin:
    sns.lineplot(data=all_ev, x="N", y="Re", hue="index")
    plt.title("Vary sigma on unit circle")
elif vary_sig_Im:
    sns.scatterplot(data=all_ev, x="Re", y="Im", hue="index")
    plt.title("Varying Complex part of sigma")
elif vary_N:
    sns.scatterplot(data=all_ev, x="N", y="Re")#, hue="index")
    #plt.title("The eigenvalues for varying N")
    plt.title("Lowest eigenvalue for given N")


plot_filename = "EVal"
if F:
    plot_filename += '_F'
elif H:
    plot_filename += '_H'

plot_filename += "_" + Re_Im

if vary_N: 
    plot_filename += "_EvalNr_" + str(N_lowest_eval) + "-" + str(N_lowest_eval + N_evals-1)

if sig_cos_sin:
    plot_filename += "_sig_cos_isin_n_" + str(48)
elif vary_sig_Im:
    plot_filename += "_sig_" + str(1) + "_i" + str(0) + "-" + str(20)
elif vary_N:
    plot_filename += "_sig_" + str(1) + "_i" + str(0)

if sig_cos_sin or vary_sig_Im:
    plot_filename += "_NEvals_" + str(N_evals)
    plot_filename += "_N_" + str(N)
elif vary_N:
    plot_filename += "_N_" + str(i_min) + "-" + str(i_max)

plot_filename += "_K_" + K

plot_filename += "_on_"+ str(x_min) +'-'+ str(x_max)

plt.ylim([-0.001,0.0001])

#plt.savefig(os.path.join(ROOT_FIGURES, 'EVal_sigma_1_i0-20_NEvals_8_on_-100_100'))
plt.savefig(os.path.join(ROOT_FIGURES, plot_filename))
plt.show()