import matplotlib.pyplot as plt
import numpy as np

import style

def set_broken_plot(ax1, ax2):
    """
    set the broken plot, refer to:
    https://stackoverflow.com/questions/32185411/break-in-x-axis-of-matplotlib

    ax1: the left axes
    ax2: the right axes
    """
    ax1.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax1.yaxis.tick_left()
    # ax1.tick_params(labelright='off')
    ax2.yaxis.tick_right()

    d = .015 # how big to make the diagonal lines in axes coordinates
    # arguments to pass plot, just so we don't keep repeating them
    kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
    ax1.plot((1-d,1+d), (-d,+d), **kwargs)
    ax2.plot((1-d,1+d),(1-d,1+d), **kwargs)

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d,+d), (1-d,1+d), **kwargs)
    ax2.plot((-d,+d), (-d,+d), **kwargs)

def plot_broken_step():
    M = 3
    T = 100
    fig, axs = plt.subplots(M,2, sharey=True)
    fig.set_size_inches(3.5, 3.5)
    rng = np.random.default_rng(1)
    Y_mat = rng.random((T,M))
    x = np.arange(1, T+1)
    break_line = 10
    for m in range(M):
        rate_limit_vec = Y_mat[:,m]
        ax = axs[m]
        for ax in axs[m,:]:
            ax.step(x, rate_limit_vec, lw=2.0, color=style.g_blue_color)
            # ax.grid(ls="--")
        axs[m,0].set_xlim(1,break_line-0.5)
        axs[m,1].set_xlim(T-break_line+0.5,T)
        axs[m,0].set_ylabel(f"y{m+1}")
        set_broken_plot(axs[m,0], axs[m,1])
        
    for m in range(0,M-1):
        for ax in axs[m,:]:
            # ax.xaxis.set_visible(False)
            pass

    axs[M-1,0].set_xlabel("t")
    axs[M-1,1].set_xlabel("t")
    # fig.subplots_adjust(bottom=0.15, left=0.1, right=0.99, top=0.97, wspace=0.25, hspace=0)
    fig.subplots_adjust(hspace=0.25, wspace=0.04, top=0.98, left=0.15, right=0.85, bottom=0.1)

    fig.savefig("figs/fig4.png", dpi=400)


if __name__ == '__main__':
    # plot for energy
    style.use_ieee_style()
    #style.use_bold_tex_style()
    # style.use_google_style_colors()
    plot_broken_step()