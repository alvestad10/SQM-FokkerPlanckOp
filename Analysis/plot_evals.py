
############################################
###             IMPORTS                 ####
############################################

###### SYSTEM IMPORTS ######
import os
import argparse

###### LIBRARY IMPORTS #######
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



################################################
###                 CONSTANTS               ####
################################################
###### SETTINGS #######
from analysis_settings import MODEL,\
                              ROOT_DATA_MODEL,\
                              ROOT_FIGURES_MODEL,\
                              COLUMNS,\
                              Test

from analysis_settings import V_MIN,\
                              V_MAX,\
                              V_MIN_MAX,\
                              N

from Tests import Test_vary_N,\
                  Test_sig_im,\
                  Test_sig_unit_circle


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Tests:
    parser.add_argument("-vary_N",
                        help="plot the change in the numbers of discretized points N",
                        action="store_true")
    parser.add_argument("-vary_sig_Im",
                        help="plot the change in the imagenary part of the sigma parameter",
                        action="store_true")
    parser.add_argument("-sig_cos_sin",
                        help="plot the change in sigma over complex unit circle",
                        action="store_true")


    parser.add_argument("-nevals",
                        help="Number of eigenvalues to show in plot",
                        type=int,
                        default=1)
    parser.add_argument("-leval",
                        help="The lowest eigenvalue to show",
                        type=int,
                        default=0)
    parser.add_argument("--kernel", "-K",
                        help="What kernel to use (see convention on datafiles)",
                        default="1")
    parser.add_argument("-F", "--F",
                        help="Eigenvalues from Fokker-Planck operator",
                        action="store_true")
    parser.add_argument("-H", "--H",
                        help="Eigenvalues from MODIFIED Fokker-Planck operator",
                        action="store_true")
    parser.add_argument("--real","-Re",
                        help="Plot real axis",
                        action="store_true",)
    parser.add_argument("--imag","-Im",
                        help="Plot imaginary axis",
                        action="store_true")
    parser.add_argument("--noN","-noN",
                        help="If N is not specified in filename",
                        action="store_true",
                        default=False)

    parser.add_argument("-save",
                        help="Plot the figure",
                        action="store_true",
                        default=False)
    parser.add_argument("-show",
                        help="Show the figure",
                        action="store_true",
                        default=False)

    
    
                    
    args = parser.parse_args()

    # Figure specifics
    SAVE = args.save
    SHOW = args.show

    # Eigenvalues parameters
    NEVALS = args.nevals
    LEVAL = args.leval

    if args.noN:
        N=None

    # Other parameters
    K=args.kernel
    if args.F and not args.H:
        F=True
        H=False
    elif args.H and not args.F:
        F=False
        H=True
    else:
        F=False
        H=False
        #assert False, "Specify either F or H"

    if args.real and not args.imag:
        Re_Im = "Re"
    elif args.imag and not args.real:
        Re_Im = "Im"
    else:
        # Check if the test is relevant for this parameters
        assert not args.vary_N, "Must specify if the real or imagenary eigenvalues should be plotted"

    # Select which type of testing
    if args.sig_cos_sin:
        TEST = Test.SIG_UNIT_CIRCLE
    elif args.vary_sig_Im:
        TEST = Test.SIG_IM
    elif args.vary_N:
        TEST = Test.VARY_N
    else:
        assert False, "Must specify test, see test enum in analysis_settings.py"
    
    if TEST == Test.VARY_N:
        test = Test_vary_N(K,True,False,True,1,0,"PERIODIC",True,"Re",NEVALS,LEVAL,V_MIN,V_MAX)
        test2 = Test_vary_N(K,False,False,False,1,0,"SBP",False, "Re", NEVALS,LEVAL,V_MIN,V_MAX)

        test.loop(100,2000,10)
        test2.loop(100,2000,10)

        test.merge(test2, "PERIODIC_VS_SBP")
        test.plot()
        if SAVE: test.save()
        plt.show()
