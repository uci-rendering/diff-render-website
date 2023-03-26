---
title: "Differentiating Integrals"
weight: 1
mathjax: true
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

{{< latex_macros_basic >}}

# Differentiating Integrals

_by Shuang Zhao_

Since **forward rendering** largely amounts to computing (high-dimensional) integrals, physics-based **differentiable rendering** requires estimating derivatives of forward-rendering integrals (with respect to arbitrary parameters of a virtual scene).

In what follows, we discuss the differentiation of a general Lebesgue integral `$I(\theta)$` over some domain `$\Omega$` associated with measure `$\mu$`:

<div>
\begin{equation}
  \label{eqn:I}
  I(\theta) = \int_{\Omega} f(\bx, \theta) \,\D\mu(\bx).
\end{equation}
</div>

When applied to rendering, the domain `$\Omega$` in Eq. \eqref{eqn:I} can be:

- The surface of the unit sphere `$\sph := \{ \bx \in \real^3 : \| \bx \| = 1 \}$`;
- The surface `$\calM$` of objects in the scene;
- The path space under Veach's path-integral formulation.

In practice, the integral in Eq. \eqref{eqn:I} can be estimated numerically using *Monte Carlo integration* via

<div>
\begin{equation}
  \label{eqn:I_MC}
  \langle I(\theta) \rangle = \frac{1}{N} \sum_{i = 1}^N \frac{f(\bx_i, \theta)}{p(\bx_i)},
\end{equation}
</div>

where `$\bx_1, \bx_2, \ldots, \bx_N \in \Omega$` are `$N$` random samples drawn from some probability density distribution `$p$`.

In Eq. \eqref{eqn:I_MC}, `$\langle I(\theta) \rangle$` is an *unbiased* and *consistent* estimator of $I(\theta)$.


## The Incomplete Solution

The derivative of the integral in Eq. \eqref{eqn:I} with respect to `$\theta$` can *sometimes* be obtained by exchanging the ordering of differentiation and integration:

<div>
\begin{equation}
  \label{eqn:dI_0}
  \frac{\D}{\D\theta} I = \frac{\D}{\D\theta} \left( \int_{\Omega} f(\bx, \theta) \,\D\mu(\bx) \right)
  \stackrel{\Large ?}{=} \int_{\Omega} \left( \frac{\D}{\D\theta} f(\bx, \theta) \right) \D\mu(\bx).
\end{equation}
</div>

Precisely, the second equality in Eq. \eqref{eqn:dI_0} requires the integrand $f$ to be **continuous** throughout the domain `$\Omega$`.
When this is the case, the derivative `$\D I/\D\theta$` in Eq. \eqref{eqn:dI_0} can be estimated using *Monte Carlo integration* using a similar process as Eq. \eqref{eqn:I_MC} via

<div>
\begin{equation}
  \label{eqn:dI_MC}
  \left\langle \frac{\D I}{\D\theta} \right\rangle = \frac{1}{N} \sum_{i = 1}^N \frac{\D f(\bx_i, \theta)/\D\theta}{p(\bx_i)}.
\end{equation}
</div>


### Success Example

We now provide a toy example where Eq. \eqref{eqn:dI_0} holds.
Let `$f(x, \theta) := x^2 \,\theta$`. Consider the following simple Riemann integral:

<div>
$$
  I = \int_0^1 (x^2 \,\theta) \,\D x.
$$
</div>

Since `$I = \left[ (x^3 \,\theta)/3 \right]_0^1 = \theta/3$`, we know that

<div>
$$
  \frac{\D I}{\D\theta} = \frac{\D}{\D\theta} \left( \frac{\theta}{3} \right)
  = {\color{blue}\frac{1}{3}}.
$$
</div>

We now try calculating the same derivative `$\D I/\D\theta$` using Eq. \eqref{eqn:dI_0}:

<div>
$$
  \frac{\D I}{\D\theta} = \int_0^1 \frac{\D}{\D\theta} (x^2 \,\theta) \,\D x
  = \int_0^1 x^2 \,\D x
  = \left[ \frac{x^3}{3} \right]_0^1
  = {\color{blue}\frac{1}{3}},
$$
</div>

which matches the manually calculated result above.


### Failure Example

We now show another toy example for which simply exchanging differentiation and integration outlined in Eq. \eqref{eqn:dI_0} fails.
Let

<div>
\begin{equation}
  \label{eqn:f_step}
  f(x, \theta) := \begin{cases}
    1, & (x < \theta)\\
    1/2. & (x \geq \theta)
  \end{cases}
\end{equation}
</div>

Then, for any `$0 < \theta < 1$`, it holds that

<div>
$$
  \begin{split}
  I &= \int_0^1 f(x, \theta) \,\D x 
  = \left( \int_0^\theta \D x \right) + \left( \int_{\theta}^1 \frac{1}{2} \,\D x \right)\\
  &= \left[ x \right]_0^{\theta} + \left[ \frac{x}{2} \right]_{\theta}^1
  = \theta + \left( \frac{1}{2} - \frac{\theta}{2} \right)
  = \frac{1}{2} + \frac{\theta}{2},
  \end{split}
$$
</div>

and

<div>
$$
  \frac{\D I}{\D\theta} = \frac{\D}{\D\theta} \left( \frac{1}{2} + \frac{\theta}{2} \right) = {\color{red}\frac{1}{2}}.
$$
</div>

However, since the integrand $f$ is piecewise-constant in this example, we have `$\D f/\D\theta \equiv 0$`.
Thus, Eq. \eqref{eqn:dI_0} in this example gives

<div>
$$
  \int_0^1 \frac{\D}{\D\theta} f(x, \theta) \,\D x = \int_0^1 0 \,\D x = {\color{red}0},
$$
</div>

which does **not** match the manually calculated result.


## The General Solution

Before presenting the general expression of the derivative `$\D I/\D\theta$`, we first examine the examples shown above.

### Examining The Previous Examples

#### The Success Example

We first examine the [success example](#success-example) with the integrand `$f(x, \theta) = x^2 \,\theta$`.
In the following, we show the graph of `$f(x, \theta)$` for some fixed `$\theta = \theta_0$` in the following:
![SuccessExample_0](/images/diff-render/basics/diff-int/SuccessExample_0_ManimCE_v0.17.2.png)
By definition, the integral `$I(\theta_0) := \int_0^1 f(x, \theta) \,\D x$` equals the signed area (marked in light blue) of the region below the graph.
Further, by adding some small `$\Delta\theta > 0$` to `$\theta_0$`, we obtain the graph of `$f(x, \theta_0 + \Delta\theta)$` and the corresponding signed area `$I(\theta_0 + \Delta\theta)$`, both illustrated in red:
![SuccessExample_1](/images/diff-render/basics/diff-int/SuccessExample_1_ManimCE_v0.17.2.png)

We recall that the derivative of $I$ with respect to `$\theta$` is given by the rate at which $I$ changes with `$\theta$`.
To calculate this rate, we examine the difference between `$I(\theta_0 + \Delta\theta)$` and `$I(\theta_0)$`:

<div>
\begin{equation}
  \label{eqn:diffI0_0}
  I(\theta_0 + \Delta\theta) - I(\theta_0) = \int_0^1 \left(f(x, \theta_0 + \Delta\theta) - f(x, \theta_0)\right) \,\D x.
\end{equation}
</div>

Geometrically, this difference equals the (signed) area of the orange region illustrated below:
![SuccessExample_2](/images/diff-render/basics/diff-int/SuccessExample_2_ManimCE_v0.17.2.png)

At each fixed `$0 < x < 1$`, the integrand of Eq. \eqref{eqn:diffI0_0} satisfies that

<div>
$$
  f(x, \theta_0 + \Delta\theta) - f(x, \theta_0) \approx \left[ \frac{\D}{\D\theta} f(x, \theta) \right]_{\theta = \theta_0} \Delta\theta.
$$
</div>

Base on this relation, we can rewrite the area difference \eqref{eqn:diffI0_0} as:

<div>
$$
  I(\theta_0 + \Delta\theta) - I(\theta_0)
  \approx \int_0^1 \left( \left[ \frac{\D}{\D\theta} f(x, \theta) \right]_{\theta = \theta_0} \Delta\theta \right) \D x
  = \Delta\theta \int_0^1 \left[ \frac{\D}{\D\theta} f(x, \theta) \right]_{\theta = \theta_0} \D x.
$$
</div>

In both equations above, the equalities become exact at the limit of `$\Delta\theta \to 0$`.
Therefore, for any `$0 < \theta_0 < 1$`, we have

<div>
$$
  \left[ \frac{\D}{\D\theta} I(\theta) \right]_{\theta = \theta_0}
  := \lim_{\Delta\theta \to 0} \frac{I(\theta_0 + \Delta\theta) - I(\theta_0)}{\Delta\theta} = \int_0^1 \left[ \frac{\D}{\D\theta} f(x, \theta) \right]_{\theta = \theta_0} \D x,
$$
</div>

which agrees with the incomplete solution expressed in Eq. \eqref{eqn:dI_0}.


#### The Failure Example

So what has been the cause for the [failure example](#failure-example)?
To be specific, what has been missing from the incomplete solution \eqref{eqn:dI_0}?

To understand what has been going on, we again examine the integrand `$f(x, \,\theta)$` which, for this example, is the piecewise-constant function defined in Eq. \eqref{eqn:f_step}.

The following are the graphs of `$f(x, \,\theta)$` for some fixed `$\theta = \theta_0$` and `$\theta = \theta_0 + \Delta\theta$` (for some small `$\Delta\theta > 0$`), respectively:
![FailureExample_0](/images/diff-render/basics/diff-int/FailureExample_0_ManimCE_v0.17.2.png)
![FailureExample_1](/images/diff-render/basics/diff-int/FailureExample_1_ManimCE_v0.17.2.png)

Further, the difference `$I(\theta_0 + \Delta\theta) - I(\theta_0)$` between the signed areas below the two graphs is caused by the rectangle illustrated in orange:
![FailureExample_2](/images/diff-render/basics/diff-int/FailureExample_2_ManimCE_v0.17.2.png)

Intuitively, in the [success example](#success-example), the change of signed area is caused by **vertical** shifts of the graph---which is captured by the incomplete solution \eqref{eqn:dI_0}.
On the other hand, in this [failure example](#failure-example), the change of signed area is caused by **horizontal** shifts of the graph *at jump discontinuities*---which is *missing* from the incomplete solution!
