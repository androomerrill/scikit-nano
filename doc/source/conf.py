# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
#
# scikit-nano documentation build configuration file, created by
# sphinx-quickstart on Wed Oct 30 00:26:16 2013.
#
# This file is execfile()d with the current directory set to its containing dir

#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import re
import sys

# Check Sphinx version
import sphinx
if sphinx.__version__ < "1.1":
    raise RuntimeError("Sphinx 1.1 or newer required")

needs_sphinx = '1.1'

# -- General configuration ----------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../sphinxext'))
sys.path.insert(0, os.path.abspath('../sphinxext/numpydoc'))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.mathjax', 'numpydoc',
              'sphinx.ext.intersphinx', 'sphinx.ext.coverage',
              'sphinx.ext.autosummary', 'sphinx.ext.inheritance_diagram',
              'sphinx.ext.todo', 'sphinx.ext.viewcode',
              'ipython_console_highlighting', 'sphinxarg.ext']

# Show todo items
todo_include_todos = True

# Determine if the matplotlib has a recent enough version of the
# plot_directive.
try:
    from matplotlib.sphinxext import plot_directive
except ImportError:
    use_matplotlib_plot_directive = False
else:
    try:
        use_matplotlib_plot_directive = (plot_directive.__version__ >= 2)
    except AttributeError:
        use_matplotlib_plot_directive = False

if use_matplotlib_plot_directive:
    extensions.append('matplotlib.sphinxext.plot_directive')
else:
    raise RuntimeError("You need a recent enough version of matplotlib")

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = u'scikit-nano'
copyright = u'2014, Andrew Merrill'

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
import sknano
version = re.sub(r'\.dev-.*$', r'.dev', sknano.__version__)
release = sknano.__version__

print("scikit-nano (VERSION {})".format(version))

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# List of documents that shouldn't be included in the build.
#unused_docs = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "autolink"

# List of directories, relative to source directories, that shouldn't be
# searched for source files.
exclude_dirs = []

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

#themedir = '_theme'
html_theme = 'sknano'
html_theme_path = ['.']

html_theme_options = {
    "edit_link": False,
    "sidebar": "left",
    "sknano_logo": False,
    "rootlinks":
    [("http://github.com/androomerrill/scikit-nano", "scikit-nano"),
     ("http://projects.geekcode.io/scikit-nano/doc", "Docs")]}
html_logo = '_static/sknano_logo.png'
html_favicon = '_static/favicon.ico'
html_sidebars = {'index': 'indexsidebar.html'}

html_title = "%s v%s Reference Guide" % (project, version)
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

html_use_modindex = True
html_copy_source = False

#pngmath_use_preview = True
#pngmath_dvipng_args = ['-gamma', '1.5', '-D', '96', '-bg', 'Transparent']

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = '.html'

# Output file base name for HTML help builder.
htmlhelp_basename = 'scikit-nano-doc'

# -- Options for LaTeX output -------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class
# [howto/manual]).
latex_documents = [('index', 'scikit-nano-ref.tex',
                    'scikit-nano Reference Guide',
                    'Andrew Merrill', 'manual')]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_preamble = r'''
\usepackage{amsmath}

\DeclareUnicodeCharacter{00A0}{\nobreakspace}

% In the parameters etc. sections, align uniformly, and adjust label emphasis
\usepackage{expdlist}
\let\latexdescription=\description
\let\endlatexdescription=\enddescription
\renewenvironment{description}%
{\begin{latexdescription}%
[\setleftmargin{60pt}\breaklabel\setlabelstyle{\bfseries\itshape}]}%
{\end{latexdescription}}

% Make Examples/etc section headers smaller and more compact
\makeatletter
\titleformat{\paragraph}{\normalsize\normalfont\bfseries\itshape}%
            {\py@NormalColor}{0em}{\py@NormalColor}{\py@NormalColor}
\titlespacing*{\paragraph}{0pt}{1ex}{0pt}
\makeatother

% Save vertical space in parameter lists and elsewhere
\makeatletter
\renewenvironment{quote}%
               {\list{}{\topsep=0pt%
                        \parsep \z@ \@plus\p@}%
                \item\relax}%
               {\endlist}
\makeatother

% Fix footer/header
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{\thechapter.\ #1}}{}}
\renewcommand{\sectionmark}[1]{\markright{\MakeUppercase{\thesection.\ #1}}}
'''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_use_modindex = False


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'scikit-nano', u'scikit-nano Documentation',
     [u'Andrew Merrill'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -----------------------------------------------


# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [('index', 'scikit-nano',
                      u'scikit-nano Documentation',
                      u'Andrew Merrill', 'scikit-nano',
                      'python toolkit',
                      'Miscellaneous')]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -----------------------------------------------------------------------------
# Intersphinx configuration
# -----------------------------------------------------------------------------
intersphinx_mapping = {
    'python': ('http://docs.python.org/2', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference', None),
    'pint': ('http://pint.readthedocs.org/en/latest', None),
}

# -----------------------------------------------------------------------------
# Numpy extensions
# -----------------------------------------------------------------------------

# If we want to do a phantom import from an XML file for all autodocs
phantom_import_file = 'dump.xml'

# Generate plots for example sections
numpydoc_use_plots = True

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

if sphinx.__version__ >= "0.7":
    import glob
    autosummary_generate = glob.glob("*.rst")

# -----------------------------------------------------------------------------
# Coverage checker
# -----------------------------------------------------------------------------
coverage_ignore_modules = r"""
    """.split()
coverage_ignore_functions = r"""
    test($|_) (some|all)true bitwise_not cumproduct pkgload
    generic\.
    """.split()
coverage_ignore_classes = r"""
    """.split()

coverage_c_path = []
coverage_c_regexes = {}
coverage_ignore_c_items = {}


#------------------------------------------------------------------------------
# Plot
#------------------------------------------------------------------------------
plot_pre_code = """
import numpy as np
import scipy as sp
np.random.seed(123)
"""
plot_include_source = True
plot_formats = [('png', 96), 'pdf']
plot_html_show_formats = False

import math
phi = (math.sqrt(5) + 1)/2

font_size = 13*72/96.0  # 13 px

plot_rcparams = {
    'font.size': font_size,
    'axes.titlesize': font_size,
    'axes.labelsize': font_size,
    'xtick.labelsize': font_size,
    'ytick.labelsize': font_size,
    'legend.fontsize': font_size,
    'figure.figsize': (3*phi, 3),
    'figure.subplot.bottom': 0.2,
    'figure.subplot.left': 0.2,
    'figure.subplot.right': 0.9,
    'figure.subplot.top': 0.85,
    'figure.subplot.wspace': 0.4,
    'text.usetex': False,
}

if not use_matplotlib_plot_directive:
    import matplotlib
    matplotlib.rcParams.update(plot_rcparams)

# -----------------------------------------------------------------------------
# Source code links
# -----------------------------------------------------------------------------

import inspect
from os.path import relpath, dirname

for name in ['sphinx.ext.linkcode', 'linkcode', 'numpydoc.linkcode']:
    try:
        __import__(name)
        extensions.append(name)
        break
    except ImportError:
        pass
else:
    print("NOTE: linkcode extension not found -- no links to source generated")


def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object
    """
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except:
            return None

    try:
        fn = inspect.getsourcefile(obj)
    except:
        fn = None
    if not fn:
        try:
            fn = inspect.getsourcefile(sys.modules[obj.__module__])
        except:
            fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.findsource(obj)
    except:
        lineno = None

    if lineno:
        linespec = "#L%d" % (lineno + 1)
    else:
        linespec = ""

    fn = relpath(fn, start=dirname(sknano.__file__))

    if 'dev' in sknano.__version__:
        return("https://github.com/androomerrill/scikit-nano/blob/" +
               "dev/sknano/{}{}".format(fn, linespec))
    else:
        return("https://github.com/androomerrill/scikit-nano/blob/" +
               "v{}/sknano/{}{}".format(sknano.__version__, fn, linespec))


class Mock(object):
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            mockType = type(name, (), {})
            mockType.__module__ = __name__
            return mockType
        else:
            return Mock()

MOCK_MODULES = []
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()
