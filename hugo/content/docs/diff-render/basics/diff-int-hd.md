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

{{< latex_macros_basic >}}

# Differentiating General Integrals

_by [Shuang Zhao](https://shuangz.com)_

In the [previous section]({{<relref "diff-int-1D.md" >}}), we have discussed the differentiation of 1D Riemann integrals.

In what follows, we discuss the differentiation of a general Lebesgue integral `$I(\theta)$` over some domain `$\Omega$` associated with measure `$\mu$`:

<div>
\begin{equation}
  \label{eqn:I}
  I(\theta) = \int_{\Omega} f(\bx, \,\theta) \,\D\mu(\bx).
\end{equation}
</div>

When applied to rendering, the domain `$\Omega$` in Eq. \eqref{eqn:I} can be:

- The surface of the unit sphere `$\sph := \{ \bx \in \real^3 : \| \bx \| = 1 \}$`;
- The surface `$\calM$` of objects in the scene;
- The path space under Veach's path-integral formulation.

Assuming that `$f(\bx, \theta)$` is piecewise continuous with a zero-measure boundary `$\overline{\partial\Omega}$` comprised of the domain boundary `$\partial\Omega$` and all jump discontinuity points (as illustrated below).
Although this assumption may seem strong, it is the case for most, if not all, problems in rendering.
