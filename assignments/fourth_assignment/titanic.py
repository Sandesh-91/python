

#titanic dataset

import pandas as pd

titanic=pd.read_csv("titanic.csv")

#data cleaning
titanic=titanic.drop_duplicates()
titanic=titanic.fillna("none")
#print(titanic.to_string())
print(titanic)

# group=titanic.groupby("Survived")
# # print(group)
# # print(group.groups) # shows the groups 
# survived=group.get_group(1) #df of survived
# survived=len(survived)
# print(survived)

surr=titanic[titanic["Survived"]==1] #df of survived
total=titanic["PassengerId"] #total no
print(f"survival rate is {(len(surr)*100)/len(total):.2f}")


