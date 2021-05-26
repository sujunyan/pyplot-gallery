# %%
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # plot for energy
    fig, ax1 = plt.subplots()

    # suitable for two-column paper
    fig.set_size_inches(w=3.5, h=2.5)
    ax1.set_xlabel("xlabel")
    ax1.set_ylabel("ylabel1")
    # The second axes for saved energy (percentage)
    ax2 = ax1.twinx()
    ax2.set_ylabel("ylabel2")
    n = 10
    for i in range(2):
        marker = ['+', 'x'][i]
        ax1.plot([(i+1)*x for x in range(n)],f'-b{marker}',label=f'1{i}')
        ax2.plot([(i+1)/(x+1) for x in range(n)],f'-r{marker}',label=f'2{i}')
    ax1.grid(ls='--')
    fig.legend(loc='upper center', ncol=2, 
               bbox_to_anchor=(0, -0.15, 1, 0.2), mode=None,
               handlelength=2, columnspacing=2,
               labelspacing=0.2, frameon=False)

    fig.subplots_adjust(bottom=0.2, left=0.2, right=0.8)
    fig.savefig("fig1.png", bbox_inches='tight')
# %%
