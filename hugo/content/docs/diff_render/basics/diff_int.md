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

Precisely, the second equality in Eq. \eqref{eqn:dI} requires the integrand $f$ to be **continuous** throughout the domain $\Omega$.
When this is the case, the derivative $\D I/\D\theta$ in Eq. \eqref{eqn:dI} can be estimated using *Monte Carlo integration* using a similar process as Eq. \eqref{eqn:I_MC} via

\begin{equation}
  \label{eqn:dI_MC}
  \left\langle \frac{\D I}{\D\theta} \right\rangle = \frac{1}{N} \sum_{i = 1}^N \frac{\D f(\bx_i, \theta)/\D\theta}{p(\bx_i)}.
\end{equation}


### Success Case

We now provide a toy example where Eq. \eqref{eqn:I} holds.
Let $f(x, \theta) := x \\,\theta$. Then,

\\[
  I = \int_0^2 (x \\,\theta) \\,\D x = \left[ \frac{x^2 \\,\theta}{2} \right]_0^2 = 2\theta.
\\]

So we know that

\\[
  \frac{\D I}{\D\theta} = \frac{\D}{\D\theta} (2\theta) = 2.
\\]

We now try calculating the same derivative $\D I/\D\theta$ using Eq. \eqref{eqn:dI}:

\\[
  \frac{\D I}{\D\theta} = \int_0^2 \frac{\D}{\D\theta} (x\\,\theta) \\,\D x = \int_0^2 x \\,\D x = \left[ \frac{x^2}{2} \right]_0^2 = 2,
\\]

matching the result calculated manually above.


### Failure Case


## The General Solution

TBD.
