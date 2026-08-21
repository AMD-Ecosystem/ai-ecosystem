# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).parent.resolve()

latex_engine = "xelatex"
latex_elements = {
    "fontpkg": r"""
\usepackage{tgtermes}
\usepackage{tgheros}
\renewcommand\ttdefault{txtt}
"""
}

# configurations for PDF output by Read the Docs
project = "ROCm AI Ecosystem"
project_path = str(DOCS_DIR).replace("\\", "/")
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) %Y Advanced Micro Devices, Inc. All rights reserved."
version = "0.0.0"
release = version
#
# setting_all_article_info = False
# all_article_info_os = ["linux", "windows"]
# all_article_info_author = ""
# # pages with specific settings
# article_pages = [
# ]

external_toc_path = "./sphinx/_toc.yml"

# Register Sphinx extensions and static assets
sys.path.append(str(DOCS_DIR / "extension"))
extensions = [
    "rocm_docs",
    "rocm_docs.selector",
    "rocm_docs_custom.matrix",
    "rocm_docs_custom.icon",
    "sphinxcontrib.datatemplates",
    "sphinxcontrib.mermaid",
    "sphinx_substitution_extensions",
]
html_static_path = ["sphinx/static"]
html_js_files = ["legacy/vllm-model-select.js"]
html_css_files = ["legacy/vllm-model-select.css"]

external_projects_current_project = "rocm"
html_theme = "rocm_docs_theme"
templates_path = [
    "templates",
    str(DOCS_DIR / "extension/rocm_docs_custom/selector/templates"),
]
html_theme_options = {
    "flavor": "ai-ecosystem",
    "link_main_doc": False,
    "repository_url": "https://github.com/AMD-Ecosystem/ai-ecosystem",
    "use_repository_button": True,
    "use_issues_button": True,
}
html_title = f"AMD ROCm AI Ecosystem"
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

myst_fence_as_directive = ["mermaid"]
numfig = False

exclude_patterns = [
    "exclude/**",
    "**/include/**",
    "**/extension/**",
    "**/images/**",
]

# external_projects_remote_repository = ""
