import pandas as pd

#creating the dataframes for each csv file
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

#getting rid of the rows that are not pink morsles
df1 = df1[df1["product"] == "pink morsel"]
df2 = df2[df2["product"] == "pink morsel"]
df3 = df3[df3["product"] == "pink morsel"]

#getting rid of $ in the remaining price columns
#.str is so it does not just look for cells that contain only $
#regex is to stop the $ from acting as a regex command
df1["price"] = df1["price"].str.replace("$", "", regex=False).astype(float)
df2["price"] = df2["price"].str.replace("$", "", regex=False).astype(float)
df3["price"] = df3["price"].str.replace("$", "", regex=False).astype(float)

#finding the total price for each row price*quantity in a new column sales
df1["sales"] = df1["quantity"] * df1["price"]
df2["sales"] = df2["quantity"] * df2["price"]
df3["sales"] = df3["quantity"] * df3["price"]

#getting rid of sales and quantity columns
df1 = df1[["sales", "date", "region"]]
df2 = df2[["sales", "date", "region"]]
df3 = df3[["sales", "date", "region"]]

#merging the 3 dataframes and recalculating the index
exportDf = pd.concat([df1, df2, df3], ignore_index=True)

#writing to a new .csv, prevents an extra index column from being added
exportDf.to_csv("merged_sales_data_0.csv", index=False)