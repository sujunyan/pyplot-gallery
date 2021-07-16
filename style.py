"""
This file store some functions for style adjustment
to make the figures fit into publication templates.
"""

import matplotlib.pyplot as plt

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
