resolve-includes (LaTeX)
======

This action quickly resolves \include{} statements in your LaTeX files, recursively

Warning: this isn't very rigorous. It doesn't parse LaTeX syntax, it just looks for `^\include{[a-zA-Z0-9]+}$` in your .tex files. Use with caution.
