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
    
    fig, ax = plt.subplots()

    fig.set_size_inches(3.5, 2.2)
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel1")

    n = 5

    x_vec = range(1,n+1)
    width = 0.2
    for i in range(3):
        y_vec = [(i+2)*x for x in x_vec]
        offset = width * (i-1) * 1.1
        x_vec1 = [x + offset for x in x_vec]
        color = [style.g_brown_color, style.g_blue_color, style.g_green_color][i]
        ax.bar(x_vec1, y_vec, label=f'leg.{i+1}', color=color, alpha=0.5, width=width)

    fig.legend(loc='upper center', ncol=4, 
               bbox_to_anchor=(0.5, 0.12), ## the location of the legend
               handlelength=2, columnspacing=2.5,
               labelspacing=0.2, frameon=False)

    fig.subplots_adjust(bottom=0.25, left=0.15, right=0.85, top=0.99)
    fig.savefig("figs/fig5.png", dpi=400)
