import matplotlib.pyplot as plt
import numpy as np
import style

if __name__ == '__main__':
	# plot for energy
	#style.use_bold_tex_style()
	style.use_google_style_colors()
	
	fig, (ax1,ax2) = plt.subplots(1,2)

	# suitable for two-column paper
	fig.set_size_inches(w=6, h=2.5)
	n = 1000
	bins = 50
	y = np.random.normal(size=n)
	ax1.hist(y, bins=bins, color="#ea4335",density=True)
	ax2.hist(y, bins=bins, cumulative=True, color="#4285f4", density=True)
	for ax_ in [ax1, ax2]:
		ax_.grid(ls='--')
		ax_.spines['right'].set_visible(False)
		ax_.spines['top'].set_visible(False)
	#fig.legend(loc='upper center', ncol=2, 
	#		   bbox_to_anchor=(0, -0.1, 1, 0.2), mode=None,
	#		   handlelength=2, columnspacing=2,
	#		   labelspacing=0.2, frameon=False)
	fig.suptitle("pdf and cdf of normal distribution")

	fig.subplots_adjust(bottom=0.1, left=0.08, right=0.92, wspace=0.25)
	fig.savefig("figs/fig2.png")

# %%