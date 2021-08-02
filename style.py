"""
This file store some functions for style adjustment
to make the figures fit into publication templates.
See https://matplotlib.org/stable/tutorials/introductory/customizing.html
for a full list of matplotlib rc param
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

def use_google_style_colors():
	mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["#ea4335","#4285f4","#fbbc04","#34a853","#b8dae9","#f4cccc"]) 

def use_bold_tex_style():
	mpl.rc('font', family='serif', serif='cm10')
	mpl.rc('text', usetex=True)
	# need to use $$ symbol to bold the label
	mpl.rcParams['text.latex.preamble'] = r'''
		\boldmath
	'''

def use_acm_style():
    rc_fonts = {
    "font.family": "serif",
    "font.size": 9,
    #'figure.figsize': (5, 3),
    "text.usetex": True,
    #'text.latex.preview': True,
    'text.latex.preamble': 
        r"""
        \usepackage[libertine]{newtxmath}
        \usepackage{libertine}
        """,
    }
    plt.rcParams.update(rc_fonts)
    
def use_ieee_style():
    rc_fonts = {
    "font.family": "serif",
	"font.serif" : "Times",
    "font.size": 8,
    'figure.figsize': (3.3, 2.5),
    "text.usetex": True,
    #'text.latex.preview': True,
    'text.latex.preamble': 
        r"""
        \usepackage[libertine]{newtxmath}
        \usepackage{libertine}
        """,
    }
    plt.rcParams.update(rc_fonts)
