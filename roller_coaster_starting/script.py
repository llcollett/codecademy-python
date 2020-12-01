import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
#print(wood.head())
#print(steel.head())

# write function to plot rankings over time for 1 roller coaster here:
def plot_rankings(rc_name, park):
	df = wood[(wood['Name'] == rc_name) & (wood['Park'] == park)]
	plt.plot(range(len(df['Year of Rank'])), df['Points'])
	plt.show()

plot_rankings("Wild Mouse", "Blackpool Pleasure Beach")
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def plot_two_rankings(rc_name1, park1, rc_name2, park2):
	df1 = wood[(wood['Name'] == rc_name1) & (wood['Park'] == park1)]
	df2 = wood[(wood['Name'] == rc_name2) & (wood['Park'] == park2)]
	plt.plot(range(len(df1['Year of Rank'])), df1['Points'], 
		color = "red", label = rc_name1 + ", " + park1)
	plt.plot(range(len(df2['Year of Rank'])), df2['Points'], 
		color = "blue", label = rc_name2 + ", " + park2)
	plt.show()

plot_two_rankings("Blue Streak", "Cedar Point", 
	"T Express", "Everland")
plt.clf()
