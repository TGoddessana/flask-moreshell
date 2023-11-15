"""Sphinx configuration."""
project = "Flask Moreshell"
author = "JAEGYUN JUNG"
copyright = "2023, JAEGYUN JUNG"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
