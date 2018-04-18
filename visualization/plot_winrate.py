import numpy as np
import pylab as pl
import pandas as pd
import csv
import sys

ROOT_PATH = "/home/jake/github/dauntless"

ax = pl.axes()

for file in sys.argv[1:]:
	with open(ROOT_PATH + "/results/" + file + '_record.csv', 'rb') as f:
	    reader = csv.reader(f)
	    your_list = list(reader)
	    flat_list = [int(item) for sublist in your_list for item in sublist]
	    x = range(len(your_list))
	    #aggregate list
	    df = pd.DataFrame(data={"results" : flat_list})
	    df["aggregated"] = np.zeros(len(df["results"]))
	    for i in range(100, len(df["results"])):
	    	df.at[i, "aggregated_win"] = np.sum((df[(i-100):i]["results"]) == 1)
	    	df.at[i, "aggregated_loss"] = np.sum((df[(i-100):i]["results"]) == -1)
	    	df.at[i, "aggregated_draw"] = np.sum((df[(i-100):i]["results"]) == 0)
	    ax.plot(x, df["aggregated_win"] / 100.0, 'g', lw=1, label=file + "_win %")
	    ax.plot(x, df["aggregated_loss"] / 100.0 , 'r', lw=1, label=file + "_loss %")
	    ax.plot(x, df["aggregated_draw"] / 100.0, 'b', lw=1, label=file + "_draw %")

ax.set_title('Win Rate vs. Number of Games Played')
ax.set_xlabel('Game Number')
ax.set_ylabel('Win Rate')

# Shrink current axis's height by 10% on the bottom
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

pl.savefig(ROOT_PATH + '/results/' + "_".join(sys.argv[1:]) + '.png') 