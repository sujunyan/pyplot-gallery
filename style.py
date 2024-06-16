"""
This file store some functions for style adjustment
to make the figures fit into publication templates.
See https://matplotlib.org/stable/tutorials/introductory/customizing.html
for a full list of matplotlib rc param
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

g_brown_color = np.array([160, 88, 44]) / 255.0
g_blue_color =  np.array([89, 132, 183]) / 255.0
g_green_color = np.array([84, 130, 53]) / 255.0
g_g1_color =    np.array([182, 213, 191]) / 255.0
g_yellow_color =np.array([244, 162, 89]) / 255.0
g_red_color   = np.array([215, 48, 39]) / 255.0

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
    'figure.figsize': (5, 3),
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
    'figure.figsize': (3.5, 2.5),
    "text.usetex": True,
    #'text.latex.preview': True,
    'text.latex.preamble': 
        r"""
        \usepackage[libertine]{newtxmath}
        \usepackage{libertine}
        """,
    }
    plt.rcParams.update(rc_fonts)
