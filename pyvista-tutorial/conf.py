# -- Path setup --------------------------------------------------------------
import os
from urllib.parse import urljoin

from sphinx_revealjs.themes import get_theme_path

# -- Project information -----------------------------------------------------
project = "pyvista-tutorial-presentation"
copyright = "2023, Tetsuo Koyama"
author = "Tetsuo Koyama"
version = "0.1.dev"
release = "2023.10"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx_design",
    "sphinx_revealjs",
    "sphinxcontrib.gtagjs",
    "sphinxcontrib.sass",
    "sphinxext.opengraph",
    "sphinxemoji.sphinxemoji",
    "oembedpy.ext.sphinx",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "ja"
exclude_patterns = [".venv", "_build", "Thumbs.db", ".DS_Store", "_sections"]
pygments_style = None

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for Reveal.js output ---------------------------------------------
revealjs_style_theme = "white"

revealjs_script_conf = {
    "width": 1244,
    "height": 700,
    "controls": True,
    "progress": True,
    "history": True,
    "center": True,
    "transition": "none",
    "previewLinks": True,
}
revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealMath",
        "src": "revealjs/plugin/math/math.js",
    },
]

revealjs_static_path = html_static_path

revealjs_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
    # "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css",
    "slides.css",
    "footnotes.css",
]

# -- Options for HTMLHelp output ---------------------------------------------
htmlhelp_basename = "sphinx-revealjsdoc"

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}
latex_documents = [
    (
        master_doc,
        "sphinx-revealjs.tex",
        "sphinx-revealjs Documentation",
        "Kazuya Takei",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, "sphinx-revealjs", "sphinx-revealjs Documentation", [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (
        master_doc,
        "sphinx-revealjs",
        "sphinx-revealjs Documentation",
        author,
        "sphinx-revealjs",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_exclude_files = ["search.html"]

# -- Options for extensions --------------------------------------------------
todo_include_todos = True

if "GTAGJS_IDS" in os.environ:
    gtagjs_ids = os.environ["GTAGJS_IDS"].split(",")

budoux_targets = ["h1", "h2", "h3"]

sass_src_dir = "_sass"
sass_out_dir = "_static"
sass_targets = {"custom.scss": "custom.css"}
sass_include_paths = [
    get_theme_path("sphinx_revealjs") / "static" / "revealjs4" / "css" / "theme",
]

# sphinxext-opengraph
ogp_site_url = os.environ.get("DEMO_URL_BASE", "http://localhost:8000/")
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
    '<meta name="twitter:site" content="@attakei" />',
]


def update_ogp(app, config):
    print(config.ogp_site_url, config.language)
    config.ogp_site_url = urljoin(config.ogp_site_url, f"{config.language}/")


def setup(app):
    app.connect("config-inited", update_ogp)
