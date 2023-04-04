---
title: "Differentiating General Integrals"
weight: 2
mathjax: true
draft: false
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Differentiating General Integrals

_by [Shuang Zhao](https://shuangz.com)_

{{< latex_macros_basic >}}

<!-- Additional macros -->
<script>
  window.MathJax.tex.macros = Object.assign({}, window.MathJax.tex.macros, {
    domain: "\\Omega",
    boundary: "\\overline{\\partial\\Omega}",
    alphaBnd: "\\boldsymbol{\\alpha}_{\\bx}",
  });
</script>

In the [previous section]({{<relref "diff-int-1d.md" >}}), we have discussed the differentiation of 1D Riemann integrals.

In what follows, we discuss the differentiation of a general Lebesgue integral `$I(\theta)$` over some bounded and open domain `$\domain$` associated with measure `$\mu$`:

<div>
\begin{equation}
  \label{eqn:I}
  I(\theta) = \int_{\domain} f(\bx, \,\theta) \,\D\mu(\bx).
\end{equation}
</div>

For practical rendering problems, the domain `$\domain$` can be:

- The surface of the unit sphere `$\sph := \{ \bx \in \real^3 : \| \bx \| = 1 \}$`;

- The union `$\calM$` of all object surfaces;

- The path space (under Veach's path-integral formulation).

We assume that `$f(\bx, \theta)$` is piecewise continuous with a zero-measure **extended boundary** `$\boundary = \partial\domain \cup \Delta\domain$` comprising the *domain boundary* `$\partial\domain$` and all *jump discontinuity points* denoted as `$\Delta\domain$`---which are illustrated below as black and orange curves, respectively:

<span id="fig_domain"></span>

![domain](/images/diff-render/basics/diff-int-hd/domain.svg)

Further, we assume the *extended boundary* `$\boundary$` to be associated with a unit-normal field `$\bn$`.
That is, for any point `$\bx$` on the *extended boundary*, we have the boundary normal `$\bn(\bx)$` specified.
We note that, although this assumption may seem restrictive, it is the case for most, if not all, problems of our interest.


## Reynolds Transport Theorem

In general, when the domain `$\domain$` of integration depends on the parameter `$\theta$`, so does the extended boundary `$\boundary$`.
In this case, the derivative of Eq. \eqref{eqn:I} with respect to `$\theta$` is given by Reynolds transport theorem.
This theorem---which is a generalization of the [result]({{<relref "diff-int-1d.md" >}}#the-full-derivative) from the [previous section]({{<relref "diff-int-1d.md" >}})---states that:

<div>
\begin{equation}
  \label{eqn:dI_reynolds}
  \boxed{
    \frac{\D}{\D\theta} I(\theta) = \underbrace{\int_{\domain(\theta)} \frac{\D}{\D\theta} f(\bx, \,\theta) \,\D\mu(\bx)}_{\text{interior}} \;+\;
    \underbrace{\int_{\boundary(\theta)} \Delta f(\bx, \theta) \,\vel(\bx) \,\D\dmu(\bx)}_{\text{boundary}} \,.
  }
\end{equation}
</div>

In this equation, the **interior** integral is obtained by exchanging differentiation and integration operations.

## The *Boundary* Integral

We now examine the **boundary** component of Eq. \eqref{eqn:dI_reynolds} more closely.

### Domain of Integration

The *boundary* integral is over the extended boundary `$\boundary(\theta)$`.
In practice:

- When the domain `$\domain(\theta) = (a(\theta), b(\theta)) \subset \real$` of the ordinary integral \eqref{eqn:I} is a *1D interval* (with `$\mu$` being the [Borel measure](https://en.wikipedia.org/wiki/Borel_measure)), `$\boundary(\theta)$` is a *discrete set* of jump discontinuity points including the interval's endpoints `$a(\theta)$` and `$b(\theta)$`. Further, the *boundary* integral reduces to the sum over all these discontinuity points---as presented in the [full derivative]({{<relref "diff-int-1d.md" >}}#the-full-derivative) from the [previous section]({{<relref "diff-int-1d.md" >}}).

- When `$\domain(\theta) \subset \real^2$` is a *2D region* with `$\mu$` being the area measure, the extended boundary `$\boundary(\theta)$` comprises a set of curves (as illustrated in [the figure above](#fig_domain)) with `$\dmu$` being the curve-length measure.

- When `$\domain(\theta) \subseteq \sph$` is a *curved 2D region* within the surface `$\sph$` of the unit sphere and `$\mu$` the solid-angle measure, the extended boundary `$\boundary(\theta)$` comprises a set of *spherical curves* with `$\dmu$` being the curve-length measure.

- When `$\domain(\theta) \subset \real^3$` is a *3D volume* and `$\mu$` the volume measure, the extended boundary `$\boundary(\theta)$` becomes *2D surfaces* with `$\dmu$` being the surface-area measure.

### Definition of `$\Delta f$`

In Eq. \eqref{eqn:dI_reynolds}, another important component of the *boundary* integral  is `$\Delta f(\bx, \theta)$` that captures the difference in `$f(\bx, \theta)$` across a discontinuity boundary at `$\bx$`.

Precisely, let `$\bx_{\bot}(\epsilon)$` be a regular curve parameterized by `$\epsilon$` (illustrated as the gray dashed line in the [figure above](#fig_domain)) that resides inside the domain `$\domain(\theta)$` and satisfies $\bx_{\bot}(0) = \bx$.
When the domain `$\domain(\theta)$` is "flat", for example, we have

<div>
$$
  \bx_{\bot}(\epsilon) := \bx + \epsilon\,\bn(\bx),
$$
</div>

where `$\bn(\bx)$` is the unit normal of the extended boundary at `$\bx$`.
Then,

<div>
\begin{equation}
  \label{eqn:delta_f}
  \Delta f(\bx, \theta) = \lim_{\epsilon \uparrow 0} f(\bx_{\bot}(\epsilon), \,\theta)
  - \lim_{\epsilon \downarrow 0} f(\bx_{\bot}(\epsilon), \,\theta).
\end{equation}
</div>


### Normal Change Rate `$\vel$`

Another key component of the *boundary* integral in Eq. \eqref{eqn:dI_reynolds} is the **normal change rate** term `$\vel$` which, at a high level, captures how fast the extended boundary `$\boundary(\theta)$` evolves (with respect to `$\theta$`) along the normal `$\bn$`.
Precisely, for any `$\bx \in \boundary(\theta)$`, we have

<div>
\begin{equation}
  \label{eqn:vel}
  \vel(\bx) = \frac{\D\bx}{\D\theta} \cdot \bn(\bx),
\end{equation}
</div>

where "`$\cdot$`" denotes the dot (or scalar) product of two vectors.

#### Parameterizing Discontinuity Boundaries

Evaluating the derivative `$\D\bx/\D\theta$` on the right-hand side of Eq. \eqref{eqn:vel} requires the extended boundary `$\boundary(\theta)$` to be *locally parameterized*.
Specifically, for each `$\theta$` and `$\bx \in \boundary(\theta)$`, we assume without loss of generality that `$\alphaBnd(\boldsymbol{\xi}, \theta)$` is a differentiable and bijective function satisfying that:
 
- `$\alphaBnd(\cdot, \theta)$` maps an open ball centered at the origin `$\boldsymbol{0}$` to an open neighborhood around `$\bx$` within the extended boundary `$\boundary(\theta)$`;

- `$\alphaBnd(\boldsymbol{0}, \theta) = \bx$`.

Then,

<div>
\begin{equation}
  \label{eqn:vel_raw}
  \frac{\D\bx}{\D\theta} = \frac{\D}{\D\theta} \alphaBnd(\boldsymbol{0}, \theta).
\end{equation}
</div>


#### Parameterization Independency

The derivative `$\D\bx/\D\theta$` defined in Eq. \eqref{eqn:vel_raw} is *parameterization-dependent*.
That is, it depends on the choice of the local parameterization specified by the function $\alphaBnd$.

On the contrary, the normal change rate `$\vel(\bx)$` from Eq. \eqref{eqn:vel} is known to be *parameterization-independent*.
In other words, regardless to the choice of $\alphaBnd$, `$\vel(\bx)$` remains identical.

## Examples