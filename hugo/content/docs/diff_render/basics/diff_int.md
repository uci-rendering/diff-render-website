---
title: "Differentiating Integrals"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Differentiating Integrals

{{< latex_macros_basic >}}

Since **forward rendering** largely amounts to computing (high-dimensional) integrals, physics-based **differentiable rendering** requires estimating derivatives of forward-rendering integrals (with respect to arbitrary parameters of a virtual scene).

In what follows, we discuss the differentiation of a general Lebesgue integral $I(\theta)$ over some domain $\Omega$ associated with measure $\mu$:

\begin{equation}
  \label{eqn:I}
  I(\theta) = \int_{\Omega} f(\bx, \theta) \\,\D\mu(\bx).
\end{equation}

When applied to rendering, the domain $\Omega$ in Eq. \eqref{eqn:I} can be:

- The surface of the unit sphere $\sph := \\{ \bx \in \real^3 : \| \bx \| = 1 \\}$;

- The surface $\calM$ of objects in the scene;

- The path space under Veach's path-integral formulation.

In practice, the integral in Eq. \eqref{eqn:I} can be estimated numerically using *Monte Carlo integration* via

\begin{equation}
  \label{eqn:I_MC}
  \langle I(\theta) \rangle = \frac{1}{N} \sum_{i = 1}^N \frac{f(\bx_i, \theta)}{p(\bx_i)},
\end{equation}

where $\bx_1, \bx_2, \ldots, \bx_N \in \Omega$ are $N$ random samples drawn from some probability density distribution $p$.



## The Incomplete Solution

The derivative of the integral in Eq. \eqref{eqn:I} with respect to $\theta$ can *sometimes* be obtained by exchanging the ordering of differentiation and integration:

\begin{equation}
  \label{eqn:dI}
  \frac{\D}{\D\theta} I = \frac{\D}{\D\theta} \left( \int_{\Omega} f(\bx, \theta) \\,\D\mu(\bx) \right)
  \stackrel{\Large ?}{=} \int_{\Omega} \left( \frac{\D}{\D\theta} f(\bx, \theta) \right) \D\mu(\bx).
\end{equation}

Precisely, 

## The General Solution
