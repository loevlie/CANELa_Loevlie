# Configuration file for the Sphinx documentation builder.
# import sphinx_theme
# -- Project information
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0,os.path.abspath('../..'))
# sys.path.insert(1, os.path.dirname(os.path.abspath("../..")) + os.sep + "feature_engine")

project = 'CANELa_Loevlie'
copyright = '2022, Dennis Loevlie'
author = 'Dennis Loevlie'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_design',
    "furo.sphinxext",
    "sphinx.ext.autosectionlabel",
    'sphinx.ext.napoleon',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std'] 

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = "furo"

html_theme_options = {
    'navigation_depth': 4,
}
# -- Options for EPUB output
epub_show_urls = 'footnote'
