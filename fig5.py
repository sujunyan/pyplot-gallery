"""
barplot
"""

import matplotlib.pyplot as plt
import style
import matplotlib as mpl

if __name__ == '__main__':
    # plot for energy
    style.use_ieee_style()
    # mpl.rc('text', usetex=true)
    # style.use_google_style_colors()
    
    fig, ax1 = plt.subplots()