# Schwinger-Keldysh Contour

From [arXiv:hep-lat/0609059](https://arxiv.org/pdf/hep-lat/0609058.pdf), we have the action on the Schwinger-Keldysh contour
$$ 
\begin{aligned}
    S =& \frac12 \sum_t \int d^3 x \left\{ \frac{(\phi_{t+1}(\bf{x}) - \phi_t(\bf{x}))^2}{\Delta_t} \right. \\
    &+ \frac{\Delta_t}{2}\left[ \phi_{t+1}(\textbf{x}) \nabla^2 \phi_{t+1}(\textbf{x}) + \phi_{t}(\textbf{x}) \nabla^2 \phi_{t}(\textbf{x}) \right] \\
    &\left. - \Delta_t\left[ V(\phi_{t+1}(x)) + V(\phi_t(x)) \right] \phantom{\rlap{$\int \frac{(\phi(\bf{x}))^2}{D}$}}\right\}
\end{aligned}
$$

Where we have both $t+1$ and $t$ since we have split these into two $\frac12$'s.

Comes from discretizing the general action:
$$ 
\begin{aligned}
    S =& -\int d^4 x \left\{ \frac12 \phi(x) \Box \phi(x)  + V(\phi(x)) \right\}
\end{aligned}
$$

where
$$
\Box = \partial_t^2 - \nabla^2
$$

Discretizing time:
$$
    \int dt \rightarrow \sum_t \Delta_t
$$

$$
    S =  \sum_t \Delta_t \int d^3 x \left\{ \frac12 \frac{(\phi_{t+1}(\textbf{x}) - \phi_t(\textbf{x}))^2}{\Delta_t^2} + \frac12 \phi_{t}(\textbf{x}) \nabla^2 \phi_{t}(\textbf{x}) - V(\phi_t(\textbf{x})) \right\}
$$

### Fokker-Planck Operator
$$
    F_{\textrm{FP}} [\phi] = \int d^4 x \frac{\delta}{\delta \phi(x)} \left( \frac{\delta}{\delta \phi(x)} - i\frac{\delta S_M[\phi]}{\delta \phi(x)} \right) 
$$