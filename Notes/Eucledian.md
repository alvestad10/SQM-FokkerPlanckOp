# Fokker-Planck operator in Eucledian time

## Notation
* Langevin time: $t_5$
* Space cordinate: $x$
  * Space index: $i$, ($j$, $k$)
* Euledian time: $\tau$
  * Eucledian index: $l$


## Model
### Harmonic Oscillator
Action for harmonic oscillator in 1+1 dimension
$$ 
    S = \sum_l \Delta_\tau \left[ \left(\frac{x_{l+1} - x_{l-1}}{2\Delta_\tau}\right)^2 + \frac12 \sigma x_l^2 \right]
$$

Fokker-Planck operator
$$
    F_{\textrm{FP}} = \nabla_x (\nabla_x + (\nabla_xS))
$$
The kinetic term
$$
\begin{aligned}
    \partial_i \sum_l \Delta_\tau \left(\frac{x_{l+1} - x_{l-1}}{2\Delta_\tau}\right)^2 =& \sum_l \frac{1}{4\Delta_\tau} \left[2(x_{l+1} - x_{l-1})(\delta_{i,l+1} - \delta_{i,l-1}) \right]\\
    =& \frac{1}{2\Delta_\tau} \left[(x_i - x_{i-2}) - (x_{i+2} - x_{i}) \right] \\
    =& \frac{1}{2\Delta_\tau} \left[- x_{i-2} + 2x_i - x_{i+2} \right]
\end{aligned}
$$

For the second derivative:
$$
\begin{aligned}
    \partial_j \partial_i \sum_l \Delta_\tau \left(\frac{x_{l+1} - x_{l-1}}{2\Delta_\tau}\right)^2 =& \partial_j \frac{1}{2\Delta_\tau} \left[- x_{i-2} + 2x_i - x_{i+2}\right] \\
    =& \frac{1}{2\Delta_\tau} \left[- \delta_{j,i-2} + 2\delta_{j,i} - \delta_{j,i+2} \right]
\end{aligned}
$$

The potential term
First derivative
$$
\partial_i \sum_l \Delta_\tau \frac12 \sigma x_l^2 = \frac12 \Delta_\tau \sum_l  \sigma 2x_l\delta_{i,l} = \Delta_\tau \sigma x_i 
$$

Second Derivative
$$
\partial_j \partial_i \sum_l \Delta_\tau \frac12 \sigma x_l^2 = \frac12 \Delta_\tau \partial_j \sum_l  \sigma 2x_l\delta_{i,l} = \Delta_\tau \partial_j \sigma x_i = \Delta_\tau \sigma \delta_{i,j}  
$$

Putting in the action:
$$
\begin{aligned}
    F_{\textrm{FP}} = \nabla_x^2 + (\nabla_x^2 S) + (\nabla_x S) \nabla_x
\end{aligned}
$$

$$
\begin{aligned}
    \rightarrow F_{\textrm{FP}}^{ij} =& \nabla_{x}^2 + \frac{- \delta_{j,i-2} + 2\delta_{j,i} - \delta_{j,i+2} }{2\Delta_\tau} + \Delta_\tau \sigma \delta_{i,j} \\
    &+ \left\{ \frac{- x_{i-2} + 2x_{i} - x_{i+2} }{2\Delta_\tau} + \Delta_\tau \sigma x_i \right\} \nabla_{x}
\end{aligned}
$$

Discretizing $x$:
$$
\begin{aligned}
    \rightarrow F_{\textrm{FP}}^{ij,l} =& \frac{P_{j,l+1} -2P_{j,l} + P_{j,l-1}}{a^2}\delta_{ij} \\
    &+ \left(\frac{- \delta_{j,i-2} + 2\delta_{j,i} - \delta_{j,i+2} }{2\Delta_\tau}  + \Delta_\tau \sigma \delta_{i,j}\right) P_{j,l} \\
    &+ \left( \frac{- x_{i-2} + 2x_{i} - x_{i+2} }{2\Delta_\tau} + \Delta_\tau \sigma x_i \right) \frac{P_{j,l+1} - P_{j,l-1}}{2a}
\end{aligned}
$$


* $P(x_0,x_1,...;t_5)$ in fokker-planck equation will be
  * [(l=0,x_min), (l=1,x_min), .... , (l=0,x_1), .... , (l=0,x_max), ...]
  * Try both order (l,x_i) and (x_i,l) 
