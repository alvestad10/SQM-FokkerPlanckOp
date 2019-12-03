# Analysing the probablity distribution

Calculations of the eigenvalues have been done one the volume -100 to 100. In this note I will look into if this is to high of a volume or if it should be bigger

## The probability distribution
The Fokker-Planck equation is:
$$
    \frac{d}{dt}\Phi(x;t) = F_{\textrm{FP}} \Phi(x;t) 
$$
where
* $\Phi(x,t)$ is the probability distribution (this is the same as $|\psi(x;t)|^2$ in quantum mechanincs)
* $F_{\textrm{FP}}$ is the Fokker-Planck operator

We can convert this into a time-independent eigenvalue problem by seperation of variable:
$$
    \Phi(x;t) = P(x)\phi(t)
$$

The time-independent Fokker-Planck equation therefor becomes:
$$
    F_{\textrm{FP}} P(x) = \lambda_n P(x)
$$

We have until now only considered the eigenvalues of the problem above. The eigenvectors, which is the probability distribution is also possible to get out of the eigensolvers (Using Eigen at this point)

This means that the corresponding eigenvector for the first eigenvalue should give the greound state probability distribution. 


## Plotting Probability distribution
To ge


## Testing cases where the eigenvalue behaves strange

### High Im($\sigma$)
When we previously varied $\sigma$ in LM_HO model (having the action $S = \frac12 \sigma x^2$) we got:
![Fig:](../Figures/LM_AHO/EVal_sigma_1_i0-20_NEvals_8_on_-100_100.png)

For high values of $Im(\sigma)$ the we clearly get the wrong result.
Plotting the probability distribution for $Im(\sigma)$ we can clearly see why.
.....
Plot above is for N=..., volume=..., ..... (This is for $H_{\textrm{FP}}$)

If we know plot for the old volume: V=-100 to 100, we can see that the answare at high $Im(\sigma)$ does not make sense. 

### When the eigenvalues oscillate in "on the unite circle"
When we analysed that all the eigenvalues of $F_{\textrm{FP}}$ when changing $\sigma$ on the complex unit circle, we got some oscillations when $\sigma$ was close to $Re(\sigma)=0$ and $Im(\sigma) = \pm 1$. Plot below show the eigenvalues for the $H_{\textrm{FP}}$

![](../Figures/LM_HO/EVal_sig_cos_isin_n_48_NEvals_5_K_1_N_-250_on_-100-100.png)