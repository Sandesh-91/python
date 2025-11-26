import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# print(matplotlib.__version__)

#drawing a simple graph

# x=np.array([10,20,30,55])
# y=np.array([2.6,3,6,8.9])
# z=np.array([30,40,70,2])
# line_style=dict(
#     marker="*",
#     ms=20, #ms
#     mfc="aqua", #mfc
#     mec="blue", #mec
#     linestyle="solid",
#     linewidth=3,
#     color="red"
# )
# plt.plot(x,y,**line_style)  #plot the graph
# plt.plot(x,z,**line_style)
# plt.title("Pressure",fontsize=20,family="Poppins",color="Brown",fontweight="bold")
# plt.xlabel("Force")
# plt.ylabel("Area")
# plt.tick_params(axis="both",colors="tomato")
# plt.xticks(x)
# plt.yticks(y)


#---------------------------------------------------------------------------grid----------------------------------------------------------- 


# # plt.grid(axis="both",color="lightgray",linewidth=1,linestyle="dashed")
# categories=np.array(["Lumbini","Bagmati","Karnali","Biratnagar","Madhesh","Sudurpaschim","Chitwan"])
# values=np.array([30,33,28,22,25,31,30])
# plt.bar(categories,values,color="blue")
# plt.title("Literacy in province",color="Red",fontsize=30,fontweight="bold")
# plt.xlabel("categories")
# plt.ylabel("values")
# plt.xticks(categories,fontsize=8)
# plt.yticks(values,fontsize=8)
# plt.grid(axis="y",linewidth=2,color="blue")

# plt.yticks(values)

# plt.show() #show the graph



#-----------------------------------------------------------------pie chart-----------------------------------------------------------------



# categories=["Seniors","Juniors","Sophomores"]
# values=np.array([200,100,250])
# colors=["Red","Blue","Green"]
# plt.pie(values,labels=categories,colors=colors,autopct="%1.1f",explode=[0.1,0,0],shadow=True,startangle=180)  # autopct sets percentage explode makes slices like in  a pizza ,shadow brings a shadow,and startangle rotates the pie chart   
# plt.show()


#------------------------------------------------------------------scatter graphs-------------------------------------------------------------
#they show the correlation between two variables +,- or none

# x=np.array([0,2,4,5,3,6,7])
# y=np.array([5,3,3,9,10,6,7])

# z=np.array([0,2,1,5,4,8,7])
# l=np.array([5,3,1,5,4,8,7])


# plt.scatter(x,y,color="blue",alpha=0.5,s=200,label="Class A")
# plt.scatter(z,l,color="red",alpha=0.5,s=200,label="Class B")
# plt.title("Examine")
# plt.legend()
# plt.xlabel("Test score")
# plt.ylabel("Hours")


# plt.show()



#-----------------------------------------------------------------histograms----------------------------------------------------------------

#a visual representation of distribution of quantative data,they group values into bins(intervals) and count how many fall in the range

# scores=np.random.normal(loc=80,scale=10,size=100)  #loc is the mean ,scale is S.D and size is 100 values
# scores=np.clip(scores,0,100) #ensure no values go beyond 0 and 100
# plt.hist(scores,bins=10,color="lightgreen",edgecolor="black") #generate histogram
# plt.show()


# #-----------------------------------------------------------------------------------subplots------------------------------------------------
# x=np.array([1,2,3,4,5,6])

# figures,axes=plt.subplots(2,2)

# axes[0,0].plot(x,x*2,color="red")
# axes[0,0].set_title("x**2",fontsize=10)
# axes[0,1].plot(x,x**2,color="blue")
# axes[0,1].set_title("x**2",fontsize=10)
# axes[1,0].plot(x,x*3,color="green")
# axes[1,0].set_title("x**2",fontsize=10)
# axes[1,1].plot(x,x**3,color="navy")
# axes[1,1].set_title("x**2",fontsize=10)
# plt.show()
# plt.tight_layout()



#---------------------------------------------pandas+matplotlib-----------------------------------------------------------------------------

df=pd.read_csv("pokemon.csv")
# print(df)
type_count=df["Type1"].value_counts(ascending=True)
print(type_count)
plt.barh(type_count.index,type_count.values,color="lightgreen",edgecolor="black")
plt.tight_layout()
plt.title("# pokemon by primary type")
plt.show()