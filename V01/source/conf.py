# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Welding Kit SDK API Manual'
copyright = '2025, JAKA Robotics'
author = 'JAKA Robotics'
release = 'V01'

import os
import sys

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon', 
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
]

source_suffix = {
 '.rst': 'restructuredtext',
 '.txt': 'restructuredtext',
 '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

master_doc = 'index'

# 启用图形、表格、代码块等的自动编号
numfig = True

# 设置编号格式
# 默认格式为：图 %s，表 %s，代码块 %s
# 可以根据需要自定义
numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码块 %s',
    'section': '节 %s'
}

numfig_secnum_depth = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 语法高亮样式
pygments_style = 'sphinx'

# 使用sphinx主题时，也可以尝试其他样式，如'colorful'
pygments_style = 'colorful'

# 使用jieba进行中文分词
html_search_language = 'zh'
html_search_options = {
    'type': 'jieba',
    'lang': 'zh_CN'
}
