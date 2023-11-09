"""Sphinx configuration."""
project = "Flask Moreshell"
author = "tgoddessana"
copyright = "2023, tgoddessana"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
