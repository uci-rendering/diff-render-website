# Physics-Based Differentiable and Inverse Rendering

This website provides a comprehensive introduction---with detailed examples and codes---on recent advances in physics-based differentiable and inverse rendering.

## Accessing the website

The deployed version of this website is hosted at [diff-render.org](https://diff-render.org).

## Developing/building the website

To clone this repository, use `git clone --recursive` to also pull the [hugo-book](https://github.com/alex-shpak/hugo-book) submodule.

This website is developed using [Hugo](https://gohugo.io/). To build it, you will need to [install Hugo](https://gohugo.io/installation/) by running, for example, `brew install hugo` under MacOS and `sudo snap install hugo` under Ubuntu.

With Hugo installed, running `hugo sever` under the `./hugo` directory will start a local web server listening on `127.0.0.1:1313`. For the server to also include draft pages, use `hugo server -D` instead.

To build a persistent version of the website (without including any draft pages), run `hugo --minify` under `./hugo`. The resulting static pages will be stored at `./hugo/public`.

## Writing math

This website uses [MathJax](https://www.mathjax.org/) to support both inline and display math (using TeX/LaTeX).
To enable MathJax on a page, set the page-level parameter `mathjax: true`.

### Mitigating Processor Conflicts

There is a known issue between Hugo's Markdown processor and MathJax: TeX symbols like `_` (for subscripts) may be conflicted with Hugo's Markdown processor [Goldmark](https://github.com/yuin/goldmark/) (for italic fonts), causing math equations to break.
To mitigate this issue, we use [this trick](https://geoffruddock.com/math-typesetting-in-hugo/) that requires inline math to use `` `$ ... $` `` and display math to use

```
<div>
$$
...
$$
</div>
```

or

```
<div>
\begin{equation}
...
\end{equation}
</div>
```

### Defining TeX/LaTeX Macros

TeX/LaTeX macros can be defined in Javascript like

```
<script>
  window.MathJax.tex.macros = {
    real: "\\mathbb{R}"
  };
</script>
```

Although one can directly include `<script>` blocks in individual pages, doing so is highly **discouraged**. Instead, it is recommended to utilize Hugo's *shortcodes* functionality by storing macro-containing `<script>` blocks in HTML files under [`hugo/layouts/shortcodes/`](hugo/layouts/shortcodes/). To include, for example, the file [`latex_macros_basic.html`](hugo/layouts/shortcodes/latex_macros_basic.html) in a page, use `{{< latex_macros_basic >}}` (perferably *after* the title).
