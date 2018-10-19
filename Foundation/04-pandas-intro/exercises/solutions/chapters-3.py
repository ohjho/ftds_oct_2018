fig,axs = plt.subplots(2,1)
df[people].plot.line(ax=axs[0])
df[places].plot.line(ax=axs[1])