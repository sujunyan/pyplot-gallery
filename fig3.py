#%%
import matplotlib.pyplot as plt
import numpy as np
import random

if __name__ == "__main__":
	fig, ax = plt.subplots()
	fig.set_size_inches(w=3.5, h=2.5)
	np.random.seed(0)
	data_mat = np.random.rand(1000,5)
	args = {
		'notch':True,
		'whis':1.5,
		'showbox':True,
		'showcaps':True,
		'showfliers':True,
		'sym':'r+',
		'showmeans':False,
		'boxprops':{'color':'b'},
		'whiskerprops':{'color':'black','ls':'--'},
		'medianprops':{'c':'r'}
	}
	#ax.boxplot(data_mat, notch=True, whis=1.5, showbox=True, showcaps=True, showfliers=True, sym='r+', showmeans=False, boxprops={'color':'b'}, whiskerprops={'color':'black', 'ls':'--'}, medianprops={'c':'r'})
	ax.boxplot(data_mat, **args)
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.grid(ls='--', axis='y')
	plt.subplots_adjust(bottom=0.18, left=0.15, right=0.85)
	fig.savefig("fig3.png", bbox_inches='tight')

# %%
