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

In the [previous section]({{<relref "diff-int-1D.md" >}}), we have discussed the differentiation of 1D Riemann integrals.

In what follows, we discuss the differentiation of a general Lebesgue integral `$I(\theta)$` over some bounded and open domain `$\Omega$` associated with measure `$\mu$`:

<div>
\begin{equation}
  \label{eqn:I}
  I(\theta) = \int_{\Omega} f(\bx, \,\theta) \,\D\mu(\bx).
\end{equation}
</div>

For practical rendering problems, the domain `$\Omega$` can be:

- The surface of the unit sphere `$\sph := \{ \bx \in \real^3 : \| \bx \| = 1 \}$`;
- The union `$\calM$` of all object surfaces;
- The path space (under Veach's path-integral formulation).

Assuming that `$f(\bx, \theta)$` is piecewise continuous with a zero-measure extended boundary `$\overline{\partial\Omega}$` comprising the domain boundary `$\partial\Omega$` and all jump discontinuity points denoted as `$\Delta\Omega$`:

![domain](/images/diff-render/basics/diff-int-hd/domain.svg)

Although this assumption may seem restrictive, it is the case for most, if not all, problems in rendering.

## Reynolds Transport Theorem

TBD.


## Computing Boundary Change Rates

TBD.
