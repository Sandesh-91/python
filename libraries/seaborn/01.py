import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# var=sns.get_dataset_names()  #seaborn has a collection of data sets in this case they are stored in var
# print(var)
penguins=sns.load_dataset('penguins')
# print(penguins.head())
sns.set_style("ticks") #the style of the bg -  dark,white,darkgrid,whitegrid,ticks
sns.set_context("notebook")
# sns.scatterplot(data=penguins,x="flipper_length_mm",y="body_mass_g",hue="island",palette="Dark2")
# sns.despine(left=True)  #by default removes top and right axix lines 
# sns.scatterplot(data=penguins,x="species",y="body_mass_g",hue="island",style="sex")



# sns.stripplot(data=penguins,x="species",y="body_mass_g",hue="island",dodge=True,jitter=True)  #show somewhat clearer graph than scatterplot
# sns.set_context("talk")



# sns.swarmplot(data=penguins,x="species",y="body_mass_g",hue="island")
# sns.despine()

#histogram

# sns.histplot(data=penguins,x="body_mass_g",hue="sex",multiple="stack")



#regression  plot

# sns.regplot(data=penguins,x="body_mass_g",y="flipper_length_mm",color="green")##,scatter=False hides the drops


#lineplot
# sns.lineplot(data=penguins,x="body_mass_g",y="flipper_length_mm",hue="island",style="sex")
# sns.despine()


#barplot\
# sns.barplot(data=penguins,x="species",y="body_mass_g",hue="sex",estimator=np.var,palette=["blue","green"])#


#boxplot
sns.boxplot(data=penguins,x="species",y="body_mass_g",hue="sex")#

plt.show()




#set_style is used to change the style of whole graph but set_context is used to change small elements like size of the labels,lines etc

#set_context includes - 
#paper-ideal for printing in academic papers(smallest)
#notebook-it is the default setting in jupyter and collab(medium)
#talk-good for presentation slides where readability matters(large)
#poster-largest size



