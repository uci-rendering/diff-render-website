---
title: "Basics"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# Physics-Based Differentiable Rendering Basics

In this section, we cover important mathematical and algorithmic preliminaries that will be used repeatedly in the rest of the tutorials.

### Differentiating Integrals

The differentiation of integrals plays an essential role in physics-based **differentiable rendering** since **forward rendering**---the process that needs to be differentiated---largely amounts to computing (high-dimensional) integrals.

We begin this section by discussing the differentiation of [1D]({{<relref "diff-int-1d.md" >}}) and [general]({{<relref "diff-int-hd.md" >}}) (i.e., Lebesgue) integrals.
