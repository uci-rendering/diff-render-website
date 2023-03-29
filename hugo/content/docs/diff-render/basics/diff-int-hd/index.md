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
    boundary: "\\overline{\\partial\\Omega}"
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
That is, for any point `$\bx$` on the extended boundary, we have the boundary normal `$\bn(\bx)$` specified.

We note that, although this assumption may seem restrictive, it is the case for most, if not all, problems of our interest.

## Reynolds Transport Theorem

The derivative of Eq. \eqref{eqn:I} with respect to `$\theta$` is given by Reynolds transport theorem.
This theorem---which is a generalization of the [result]({{<relref "diff-int-1d.md" >}}#the-full-derivative) from the [previous section]({{<relref "diff-int-1d.md" >}})---states that:

<div>
\begin{equation}
  \label{eqn:dI_reynolds}
  \boxed{
    \frac{\D}{\D\theta} I(\theta) = \underbrace{\int_{\domain} \frac{\D}{\D\theta} f(\bx, \,\theta) \,\D\mu(\bx)}_{\text{interior}} \;+\;
    \underbrace{\int_{\boundary} \Delta f(\bx, \theta) \,\vel(\bx) \,\D\dmu(\bx)}_{\text{boundary}} \,.
  }
\end{equation}
</div>

In this equation, the **interior** integral is obtained by exchanging differentiation and integration operations.

## The *Boundary* Integral

We now examine the **boundary** component of Eq. \eqref{eqn:dI_reynolds} more closely.

### Domain of Integration

The *boundary* integral is over the extended boundary `$\boundary$`.
In practice:

- When the domain `$\domain = (a, b) \subset \real$` of the ordinary integral \eqref{eqn:I} is a *1D interval* (with `$\mu$` being the [Borel measure](https://en.wikipedia.org/wiki/Borel_measure)), `$\boundary$` is a *discrete set* of jump discontinuity points, and the *boundary* integral reduces to the sum over all these discontinuity points---as presented in the [full derivative]({{<relref "diff-int-1d.md" >}}#the-full-derivative) from the [previous section]({{<relref "diff-int-1d.md" >}}).

- When `$\domain \subset \real^2$` is a *2D region* with `$\mu$` being the area measure, the extended boundary `$\boundary$` comprises a set of curves (as illustrated in [the figure above](#fig_domain)) with `$\dmu$` being the curve-length measure.

- When `$\domain \subseteq \sph$` is a *curved 2D region* within the surface `$\sph$` of the unit sphere and `$\mu$` the solid-angle measure, the extended boundary `$\boundary$` comprises a set of *spherical curves* with `$\dmu$` being the curve-length measure.

- When `$\domain \subset \real^3$` is a *3D volume* and `$\mu$` the volume measure, the extended boundary `$\boundary$` becomes *2D surfaces* with `$\dmu$` being the surface-area measure.

### Definition of `$\Delta f$`

In Eq. \eqref{eqn:dI_reynolds}, another important component of the *boundary* integral  is `$\Delta f(\bx, \theta)$` that captures the difference in `$f(\bx, \theta)$` across a discontinuity boundary at `$\bx$`.

Precisely, let `$\bx_{\bot}(\epsilon)$` be a regular curve parameterized by `$\epsilon$` (illustrated as the gray dashed line in the [figure above](#fig_domain)) that resides inside the domain `$\domain$` and satisfies $\bx_{\bot}(0) = \bx$.
When the domain `$\domain$` is "flat", for example, we have

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


### Change Rates

TBD.
