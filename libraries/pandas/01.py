# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as p

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


# print(p.loc["Address","Phone"])
hold.to_csv('data.csv')#export to csv
#in output 0 and 1 are index and name,address ,phone are columns

print(hold.head(2)) #display first 2 rows
print(hold.tail(2)) #display last two rows
print(hold.describe()) # describe numeric data like mean,std


#read a csv

var=p.read_csv('data.csv')
a=p.DataFrame(dict,index=["Name","Address","Phone"])
a.loc["Name","name"]="hello"
print(a.to_csv('data.csv'))
print(a)




