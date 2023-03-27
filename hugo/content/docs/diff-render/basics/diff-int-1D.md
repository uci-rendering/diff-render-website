---
title: "Differentiating 1D Integrals"
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

# Differentiating 1D Integrals

_by [Shuang Zhao](https://shuangz.com)_

In what follows, we discuss the differentiation of a simple Riemann integral `$I(\theta)$` over some 1D interval `$(a, b) \subseteq \real$`:

<div>
\begin{equation}
  \label{eqn:I}
  I(\theta) = \int_a^b f(x, \theta) \,\D x.
\end{equation}
</div>

## The Incomplete Solution

The derivative of the integral in Eq. \eqref{eqn:I} with respect to `$\theta$` can _sometimes_ be obtained by exchanging the ordering of differentiation and integration:

<div>
\begin{equation}
  \label{eqn:dI_0}
  \frac{\D}{\D\theta} I = \frac{\D}{\D\theta} \left( \int_a^b f(x, \theta) \,\D x \right)
  \stackrel{\Large ?}{=} \int_a^b \left( \frac{\D}{\D\theta} f(x, \theta) \right) \D x.
\end{equation}
</div>

Precisely, the second equality in Eq. \eqref{eqn:dI_0} requires the integrand $f$ to be **continuous**[^1] throughout the interval `$(a, b)$`.

[^1]: Unless otherwise stated, we use "continuous" to indicate the `$C^0$` class.

### Success Example

We now provide a toy example where Eq. \eqref{eqn:dI_0} holds.
Let `$f(x, \theta) := x^2 \,\theta$`. Consider the following integral:

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
    1, & (x < \theta/2)\\
    1/2. & (x \geq \theta/2)
  \end{cases}
\end{equation}
</div>

Then, for any `$0 < \theta < 2$`, it holds that

<div>
$$
  \begin{split}
  I &= \int_0^1 f(x, \theta) \,\D x 
  = \left( \int_0^{\theta/2} \D x \right) + \left( \int_{\theta/2}^1 \frac{1}{2} \,\D x \right)\\
  &= \left[ x \right]_0^{\theta/2} + \left[ \frac{x}{2} \right]_{\theta/2}^1
  = \frac{\theta}{2} + \left( \frac{1}{2} - \frac{\theta}{4} \right)
  = \frac{1}{2} + \frac{\theta}{4},
  \end{split}
$$
</div>

and

<div>
\begin{equation}
  \label{eqn:f_step_dI_manual}
  \frac{\D I}{\D\theta} = \frac{\D}{\D\theta} \left( \frac{1}{2} + \frac{\theta}{4} \right) = {\color{red}\frac{1}{4}}.
\end{equation}
</div>

However, since the integrand $f$ is piecewise-constant in this example, we have `$\D f/\D\theta \equiv 0$`.
Thus, Eq. \eqref{eqn:dI_0} in this example gives

<div>
$$
  \int_0^1 \frac{\D}{\D\theta} f(x, \theta) \,\D x = \int_0^1 0 \,\D x = {\color{red}0},
$$
</div>

which does **not** match the manually calculated result in Eq. \eqref{eqn:f_step_dI_manual}.

## The General Solution

### Examining The Previous Examples

Before presenting the general expression of the derivative `$\D I/\D\theta$`, we first examine the examples shown above.

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
By dividing both sides by `$\Delta\theta$` and taking the limit of `$\Delta\theta \to 0$`, we have

<div>
$$
  \left[ \frac{\D}{\D\theta} I(\theta) \right]_{\theta = \theta_0}
  := \lim_{\Delta\theta \to 0} \frac{I(\theta_0 + \Delta\theta) - I(\theta_0)}{\Delta\theta} = \int_0^1 \left[ \frac{\D}{\D\theta} f(x, \theta) \right]_{\theta = \theta_0} \D x,
$$
</div>

for any `$0 < \theta_0 < 1$`.
This agrees with the incomplete solution expressed in Eq. \eqref{eqn:dI_0}.

#### The Failure Example

So what has been the cause for the [failure example](#failure-example)?
To be specific, what has been missing from the incomplete solution \eqref{eqn:dI_0}?

To understand what has been going on, we again examine the integrand `$f(x, \theta)$` which, for this example, is the piecewise-constant function defined in Eq. \eqref{eqn:f_step}.

The following are the graphs of `$f(x, \theta)$` for some fixed `$\theta = \theta_0$` and `$\theta = \theta_0 + \Delta\theta$` (for some small `$\Delta\theta > 0$`), respectively:
![FailureExample_0](/images/diff-render/basics/diff-int/FailureExample_0_ManimCE_v0.17.2.png)
![FailureExample_1](/images/diff-render/basics/diff-int/FailureExample_1_ManimCE_v0.17.2.png)

Further, the difference `$I(\theta_0 + \Delta\theta) - I(\theta_0)$` between the signed areas below the two graphs is caused by the rectangle illustrated in orange:
![FailureExample_2](/images/diff-render/basics/diff-int/FailureExample_2_ManimCE_v0.17.2.png)

Intuitively, in the [success example](#success-example), the change of signed area is caused by **vertical** shifts of the graph---which is captured by the incomplete solution \eqref{eqn:dI*0}.
On the other hand, in this [failure example](#failure-example), the change of signed area is caused by **horizontal** shifts of the graph \_at jump discontinuities*---which is _missing_ from the incomplete solution!

We now calculate the signed area of the orange rectangle shown above.
We first observe that the length of the rectangle's vertical edge equals the difference `$\Delta f \equiv 1 - 1/2 = 1/2$` of the integrand `$f(x, \theta)$` across the discontinuity point.

To calculate the length of the rectangle's horizontal edge, we let `$x(\theta) = \theta/2$` denote the jump discontinuity point of `$f(x, \theta)$` defined in Eq. \eqref{eqn:f_step}.
Then, the (signed) length of the horizontal edge is simply `$x(\theta_0 + \Delta\theta) - x(\theta_0)$`.

Based on the observations above, we know that

<div>
$$
I(\theta_0 + \Delta\theta) - I(\theta_0) = \Delta f \,(x(\theta_0 + \Delta\theta) - x(\theta_0)).
$$
</div>

Dividing both sides of this equation by `$\Delta t$` and taking the limit `$\Delta\theta \to 0$` produce:

<div>
$$
  \begin{split}
    \left[ \frac{\D}{\D\theta} I(\theta) \right]_{\theta = \theta_0}
    &= \lim_{\Delta\theta \to 0} \frac{I(\theta_0 + \Delta\theta) - I(\theta_0)}{\Delta\theta}\\
    &= \Delta f \,\lim_{\Delta\theta \to 0}\frac{x(\theta_0 + \Delta\theta) - x(\theta_0)}{\Delta\theta}
    = \Delta f \left[ \frac{\D}{\D\theta} x(\theta) \right]_{\theta = \theta_0}.
  \end{split}
$$
</div>

Therefore, we know that

<div>
$$
  \frac{\D}{\D\theta} I(\theta) = \underbrace{\Delta f}_{=\, 1/2} \; \underbrace{\frac{\D}{\D\theta} x(\theta)}_{=\, 1/2}
  = {\color{red}\frac{1}{4}},
$$
</div>

matching the hand-derived result in Eq. \eqref{eqn:f_step_dI_manual}.

### The Full Derivative

Based on the observations [above](#examining-the-previous-examples), we now present the general derivative of the 1D integral expressed in Eq. \eqref{eqn:I}:

<div>
\begin{equation}
  \label{eqn:dI}
  \boxed{
    \frac{\D}{\D\theta} \left( \int_a^b f(x, \theta) \,\D x \right)
    = \underbrace{\int_a^b \left( \frac{\D}{\D\theta} f(x, \theta) \right) \D x}_{\text{interior}} \,+\,
    \underbrace{\sum_i \Delta f(x_i(\theta), \theta) \,\frac{\D}{\D\theta} x_i(\theta)}_{\text{boundary}}\,,
  }
\end{equation}
</div>

which comprises:

- A **interior** component obtained by exchanging differentiation and integration operations---identical to Eq. \eqref{eqn:dI_0}.

- A **boundary** component involving a sum over all jump discontinuity points `$\{ x_i(\theta) : i = 1, 2, \ldots \}$`.

#### Remarks

Precisely, `$\Delta f(x, \theta)$` in the _boundary_ component is defined as

<div>
$$
  \Delta f(x, \theta) := \lim_{u \uparrow x} f(u, \theta) - \lim_{u \downarrow x} f(u, \theta),
$$
</div>

where `$\lim_{u \uparrow x}$` and `$\lim_{u \downarrow x}$` denote **one-sided limits** with `$u$` approaching `$x$` from _below_ (i.e., `$u < x$`) and _above_ (i.e., `$u > x$`), respectively.
For any fixed $\theta$, $\Delta f(x, \theta)$ is nonzero (and well-defined) if and only if `$x$` is a jump discontinuity point of `$f(\cdot, \theta)$`.

Lastly, when the endpoints `$a$` and `$b$` of the integral depend on `$\theta$`, they should be considered as jump discontinuities with `$\Delta f(a, \theta) = -f(a, \theta)$` and `$\Delta f(b, \theta) = f(b, \theta)$`.

In the [next section]({{<relref "diff-int-hd.md" >}}), we will present a generalization of Eq. \eqref{eqn:dI} that describes derivatives of Lebesgue integrals.
