import pandas as pd


df=pd.read_csv('pokemon.csv')
# print(df)
# print(df.head(6))
# print(df.to_string())#should be careful when using files with large data

#access by column 

# print(df["Name"])
# print(df["Name"][149])
# print(df.loc[149,"Name"])
# print(df)


#selection by rows

# print(df.loc[24])
# print(df.loc["Pikachu"]) # for this to work we need to set index_col="col_name"
# print(df.loc["Moltres":"Mewtwo",["Height","Weight"]]) #for this als index_col="Name"
# print(df.iloc[145:150])
# print(df.iloc[145:150:2]) #step 2
# print(df.iloc[145:150:2,0:3]) #first three columns




#searching for a pokemon in csv file

# pokemon=input("Enter a pokemon name: ")

# try:
#     df.loc[pokemon]
#     print(f"{pokemon} is found in DataFrame:")
# except KeyError:
#     print(f"{pokemon} not found in DataFrame:")


#filtering in pandas
#keeping the rows that match the condition


# tall_pokemon=df[df["Weight"]>100]
# ff=df[(df["Type1"]=="Fire") | (df["Type2"]=="Flying")] # for and use &
# print(ff)

# print(tall_pokemon)



#-------------------------------------------------------------------------aggregation---------------------------------------------------------------------

#of whole DF
# print(df.mean(numeric_only=True)) #likewise sum,min,max,count

# #for a single column
# print(df["Height"].sum()) 

# #groupby function groups the columns of similar type like water types pokemons in one place and other types in other places

# group=df.groupby("Type1")
# print(group["Height"].count())


#------------------------------------------------------------------------------data cleaning--------------------------------------------------------------------


# df=df.drop(columns=["Legendary","No"]) #drops these columns from DF

# df=df.dropna(subset=["Type2"]) #drops the not  available df in type2
# df=df.fillna({"Type2":"none"})

#replace 

# df["Type1"]=df["Type1"].replace({"Grass":"GRASS","Fire":"FIRE"}) #replaces grass with GRASS and FIRE in Type1

#standardize

df["Name"]=df["Name"].str.lower() #converts into lowercase
# df["Legendary"]=df["Legendary"].astype(bool) # change the datatype of column legendary to boolean , previously it had numeric values
# df=df.drop_duplicates() #deletes the duplicate data
print(df)






