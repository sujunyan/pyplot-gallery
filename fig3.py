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
	#fig.set_size_inches(w=3.5, h=2.5)
	np.random.seed(0)
	n = 5
	data_mat = np.random.rand(1000,n)
	#style.change_hatch_color('#707070')
	args = {
		'notch':True,
		'whis':1.5,
		'showbox':True,
		'showcaps':True,
		'showfliers':True,
		'sym':'r+',
		'showmeans':False,
		"notch": True, # the curve besides the median
		'patch_artist':True, # enable facecolor
		'boxprops':{
			#'facecolor':style.google_colors[1],
			#'facecolor':"None",
			'facecolor':style.google_colors[1],
			'edgecolor':"#707070",
			#'color': "None",
			#'hatch':'/',
			},
		'whiskerprops':{
			'color':style.google_colors[1],
			'ls':'-',
			},
		'capprops':{
			'color':style.google_colors[1],
		},
		'medianprops':{
			'c': '#707070',
			'lw':2,
			},
		"widths":0.2,
		
	}
	#ax.boxplot(data_mat, notch=True, whis=1.5, showbox=True, showcaps=True, showfliers=True, sym='r+', showmeans=False, boxprops={'color':'b'}, whiskerprops={'color':'black', 'ls':'--'}, medianprops={'c':'r'})
	range_ = np.arange(n)
	offset = 0.14
	ax.boxplot(data_mat, **args, positions=range_+offset)
	for prop in ['whiskerprops', 'capprops']:
		args[prop]['color'] = style.google_colors[0]
	args['boxprops']['facecolor'] = style.google_colors[0]

	ax.boxplot(data_mat, **args, positions=range_-offset)
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	ax.set_xticks(range_)
	ax.set_xticklabels(range_)

	plt.grid(ls='--', axis='y')
	plt.subplots_adjust(bottom=0.18, left=0.15, right=0.85)
	fig.savefig("figs/fig3.png", bbox_inches='tight')

# %%
