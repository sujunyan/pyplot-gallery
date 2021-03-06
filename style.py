"""
This file store some functions for style adjustment
to make the figures fit into publication templates.
See https://matplotlib.org/stable/tutorials/introductory/customizing.html
for a full list of matplotlib rc param
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

# some good-looking colors defined by Junyan Su.
g_colors = ["#3c5488","#ad002a","#e18727","#dc0000","#FEA772","#4dbbd5","#00a087"]

google_colors = ["#ea4335","#4285f4","#fbbc04","#34a853","#b8dae9","#f4cccc", "#9048B9"]
def change_hatch_color(c):
	mpl.rcParams['hatch.color'] = c 

def use_google_style_colors():
	mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=google_colors) 

"""
require Latex installed
"""
def use_bold_tex_style():
	print(f"using bold latex style")
	mpl.rc('font', family='serif', serif='cm10')
	mpl.rc('text', usetex=True)
	mpl.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{bm} \boldmath')
	## The following command is decreciated, I guess...
	#matplotlib.rcParams['text.latex.preamble'] = [r'usepackage{bm}', r'\boldmath']

	#mpl.rc('font', family='serif', serif='cm10')
	#mpl.rc('text', usetex=True)
	## need to use $$ symbol to bold the label
	#mpl.rcParams['text.latex.preamble'] = r'''
	#	\boldmath
	#'''

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
