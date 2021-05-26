#%%
import matplotlib.pyplot as plt
import random

if __name__ == "__main__":
    fig, ax = plt.subplots()
    fig.set_size_inches(w=3.5, h = 2.5)
    # Move the left and bottom spines to x = 0 and y = 0, respectively.
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))

    # Hide the top and right spines.
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.
    #ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    #ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    xlabel_str = "xlabel"
    n = 2000
    random.seed(0)
    data_l = [abs(random.normalvariate(0,1)) for i in range(n)]
    plt.hist(data_l, bins=100, 
             alpha=0.5)
    plt.xlabel(xlabel_str)
    plt.ylabel("frequency")
    plt.grid(ls='--')

    plt.subplots_adjust(bottom=0.18, left=0.15, right=0.85)
    fig.savefig("fig2.png", bbox_inches='tight')
# %%
