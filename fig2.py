import matplotlib.pyplot as plt
import numpy as np
import style

if __name__ == '__main__':
    # plot for energy
    #style.use_bold_tex_style()
    # style.use_google_style_colors()
    style.use_ieee_style()
    
    fig, (ax1,ax2) = plt.subplots(1,2)

    # suitable for two-column paper
    fig.set_size_inches(w=7.25, h=2.5)
    n = 1000
    bins = 30
    y = np.random.normal(size=n)
    ax1.hist(y, bins=bins, density=True, facecolor='none', edgecolor=style.g_brown_color)
    color2 = style.g_blue_color
    color2a = [color2[0], color2[1], color2[2], 0.3] ## the last element is alpha, which denotes the transparency.

    ax2.hist(y, bins=bins, cumulative=True, facecolor=color2a, edgecolor=color2, density=True)

    for ax_ in [ax1, ax2]:
        # ax_.grid(ls='--')
        ax_.spines['right'].set_visible(False)
        ax_.spines['top'].set_visible(False)
        ax_.set_xlabel("xlabel")
        ax_.set_ylabel("ylabel")
    #fig.legend(loc='upper center', ncol=2, 
    #		   bbox_to_anchor=(0, -0.1, 1, 0.2), mode=None,
    #		   handlelength=2, columnspacing=2,
    #		   labelspacing=0.2, frameon=False)
    fig.suptitle("pdf and cdf of normal distribution")

    fig.subplots_adjust(bottom=0.15, left=0.08, right=0.92, wspace=0.25)
    fig.savefig("figs/fig2.png", dpi=400)

# %%