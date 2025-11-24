# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as p

list=[20,21,23,25,30]
varr=p.Series(list) #creating series
print(varr)
print(varr[varr>=25]) #print the data in series >=25
change=varr.loc[2]=22
print("after change")
print(" ")
print(varr)
chng=varr.iloc[1]=19
print(varr)


#dictionary
exercise={
    "Day 1":"chest+tricep",
    "Day 2":"back+bicep",
    "Day 3":"leg"
}


ex=p.Series(exercise)
print(ex)
print(ex[ex=="chest+tricep"])
ex.loc["Day 2"]="shoulder"
print("after change")
print(ex)


# DataFrame

dict = {
    "name": ["sandesh", "gaurav","puskar"],
    "address": ["janakinagar", "motipur","kalikanagar"],
    "phone": [9863580388, 9845298345,9812345678],
}
# hold = p.DataFrame(dict)
hold=p.DataFrame(dict,index=["Name","Address","Phone"])
print(hold)
print(hold.loc["Name"])
print(hold.loc["Address","name"])
hold["gender"]=["male","male","female"] #creating a new column
print(hold)
#adding a new row 
#this is done by creating a new DataFrame and concat them\

new_row=p.DataFrame([{"name":"anshul","address":"belbas","phone":9812345678,"gender":"N/A"}],index=["Hello"])
#concating
hold=p.concat([hold,new_row])
print("after adding row and colummn")
print(hold)


# print(p.loc["Address","Phone"])
hold.to_csv('data.csv')#export to csv
#in output 0 and 1 are index and name,address ,phone are columns

print(hold.head(2)) #display first 2 rows
print(hold.tail(2)) #display last two rows
print(hold.describe()) # describe numeric data like mean,std


#read a csv

# var=p.read_csv('data.csv')
# a=p.DataFrame(dict,index=["Name","Address","Phone","Hello"])
# a.loc["Name","name"]="hello"
# print(a.to_csv('data.csv'))
# print(a)




