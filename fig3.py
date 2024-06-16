#%%
import matplotlib.pyplot as plt
import numpy as np
import random
import style
"""
some notes:
whisker: the vertical line below and above the box
cap: the horizontal line above the whisker
"""

if __name__ == "__main__":
    fig, ax = plt.subplots()
    style.use_ieee_style()
    fig.set_size_inches(w=4.5, h=2.5)
    np.random.seed(0)
    n = 5
    data_mat = np.random.rand(100, n)
    #style.change_hatch_color('#707070')
    color1 = style.g_blue_color
    color2 = style.g_brown_color
    color1a = [color1[0], color1[1], color1[2], 0.1]
    color2a = [color2[0], color2[1], color2[2], 0.1]
    
    lw = 1.5
    args = {
        'notch':True,
        'whis':1.5,
        'showbox':True,
        'showcaps':True,
        'showfliers':True,
        'sym':'r+',
        'showmeans':False,
        "notch": False, # the curve besides the median
        'patch_artist':True, # enable facecolor
        'boxprops':{
            #'facecolor':style.google_colors[1],
            #'facecolor':"None",
            'facecolor':color1a,
            'edgecolor':color1,
            'lw' : lw,
            #'color': "None",
            #'hatch':'/',
            },
        'whiskerprops':{
            'color':color1,
            'ls':'-', ## linestyle
            'lw':lw,
            },
        'capprops':{
            'color':color1,
        },
        'medianprops':{
            'c': color1,
            'lw':lw,
            },
        "widths":0.2,
        
    }
    #ax.boxplot(data_mat, notch=True, whis=1.5, showbox=True, showcaps=True, showfliers=True, sym='r+', showmeans=False, boxprops={'color':'b'}, whiskerprops={'color':'black', 'ls':'--'}, medianprops={'c':'r'})
    range_ = np.arange(n)
    offset = 0.14
    ax.boxplot(data_mat, **args, positions=range_+offset)

    for prop in ['whiskerprops', 'capprops']:
        args[prop]['color'] = color2
    args['medianprops']['c'] = color2
    args['boxprops']['facecolor'] = color2a
    args['boxprops']['edgecolor'] = color2

    ax.boxplot(data_mat, **args, positions=range_-offset)
    plt.xlabel("xlabel")
    plt.ylabel("ylabel")
    ax.set_xticks(range_)
    ax.set_xticklabels(range_)

    # plt.grid(ls='--', axis='y')
    plt.subplots_adjust(bottom=0.18, left=0.15, right=0.85)
    fig.savefig("figs/fig3.png", bbox_inches='tight', dpi=400)

# %%
