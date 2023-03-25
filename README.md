# Physics-Based Differentiable and Inverse Rendering

This website provides a comprehensive introduction---with detailed examples and codes---on recent advances in physics-based differentiable and inverse rendering.

## Accessing the website

The deployed version of this website is hosted at [diff-render.org](https://diff-render.org).

## Developing/building the website

To clone this repository, use `git clone --recursive` to also pull the [hugo-book](https://github.com/alex-shpak/hugo-book) submodule.

This website is developed using [Hugo](https://gohugo.io/). To build it, you will need to [install Hugo](https://gohugo.io/installation/) by running, for example, `brew install hugo` under MacOS and `sudo snap install hugo` under Ubuntu.

With Hugo installed, running `hugo sever` under the `./hugo` directory will start a local web server listening on `127.0.0.1:1313`. For the server to also include draft pages, use `hugo server -D` instead.

To build a persistent version of the website (without including any draft pages), run `hugo --minify` under `./hugo`. The resulting static pages will be stored at `./hugo/public`.
