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

## 1. The Incomplete Solution

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


### 1.1 Success Example

We now provide a toy example where Eq. \eqref{eqn:I} holds.
Let $f(x, \theta) := x \\,\theta$. Consider the simple Riemann integral:

\\[
  I = \int_0^2 (x \\,\theta) \\,\D x = \left[ \frac{x^2 \\,\theta}{2} \right]_0^2 = 2\theta.
\\]

So we know that

\\[
  \frac{\D I}{\D\theta} = \frac{\D}{\D\theta} (2\theta) = \boxed{2}.
\\]

We now try calculating the same derivative $\D I/\D\theta$ using Eq. \eqref{eqn:dI}:

\\[
  \frac{\D I}{\D\theta} = \int_0^2 \frac{\D}{\D\theta} (x\\,\theta) \\,\D x = \int_0^2 x \\,\D x = \left[ \frac{x^2}{2} \right]_0^2 = \boxed{2},
\\]

which matches the manually calculated result above.


### 1.2 Failure Example

We now show another toy example for which simply exchanging differentiation and integration outlined in Eq. \eqref{eqn:dI} fails.
Let

\\[
 f(x, \theta) := \begin{cases}
  1, & (x < \theta)\\\\[4pt]
  0. & (x \geq \theta)
\end{cases}
\\]

Then, for any $0 < \theta < 1$,

\\[
  I = \int_0^1 f(x, \theta) \\,\D x = \int_0^\theta \D x = [1]_0^{\theta} = \theta,
\\]

and

\\[
  \frac{\D I}{\D\theta} = \frac{\D}{\D\theta} \theta = \boxed{1}.
\\]

However, since the integrand $f$ is piecewise constant in this example, we have $\frac{\D f}{\D\theta} \equiv 0$.
Thus, Eq. \eqref{eqn:dI} in this example gives

\\[
  \int_0^1 \frac{\D}{\D\theta} f(x, \theta) \\,\D x = \int_0^1 0 \\,\D x = \boxed{0},
\\]

which does **not** match the manually calculated result.


## 2. The General Solution

Before presenting the general expression of the derivative $\D I/\D\theta$, we first examine the [success](#11-success-example) and [failure](#12-failure-example) examples shown above.
