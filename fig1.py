# %%
import matplotlib.pyplot as plt
import style
import matplotlib as mpl

if __name__ == '__main__':
    # plot for energy
    style.use_ieee_style()
    # mpl.rc('text', usetex=true)
    # style.use_google_style_colors()
    
    fig, ax1 = plt.subplots()

    # suitable for two-column paper
    fig.set_size_inches(3.5, 2.2)
    ax1.set_xlabel("xlabel")
    ax1.set_ylabel("ylabel1")
    # The second axes for saved energy (percentage)
    ax2 = ax1.twinx()
    ax2.set_ylabel("ylabel2")
    n = 10
    lw = 2.0
    color1 = style.g_brown_color
    color2 = style.g_blue_color
    y_dict = {}
    for i in range(2):
        marker = ['+', 'x'][i]

        y_dict[(i,1)] = [(i+1)*x for x in range(n)]
        ax1.plot(y_dict[(i,1)],f'-{marker}',label=f'leg.1.{i}', lw=lw, color=color1)

        y_dict[(i,2)] = [(i+1)/(x+1) for x in range(n)]
        ax2.plot(y_dict[(i,2)],f'--{marker}',label=f'leg.2.{i}', lw=lw, color=color2)

    ax1.fill_between(range(n), y_dict[(0,1)], y_dict[(1,1)], color=color1, alpha=0.1)
    ax2.fill_between(range(n), y_dict[(0,2)], y_dict[(1,2)], color=color2, alpha=0.1)

    ax1.yaxis.label.set_color(color1)
    ax1.tick_params(colors=color1, axis="y")

    ax2.yaxis.label.set_color(color2)
    ax2.tick_params(colors=color2, axis="y")

    fig.legend(loc='upper center', ncol=4, 
               bbox_to_anchor=(0.5, 0.12), ## the location of the legend
               handlelength=2, columnspacing=1,
               labelspacing=0.2, frameon=False)

    fig.subplots_adjust(bottom=0.25, left=0.15, right=0.85, top=0.99)
    fig.savefig("figs/fig1.png", dpi=400)
# %%
