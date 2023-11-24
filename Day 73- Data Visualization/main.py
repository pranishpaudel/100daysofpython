import pandas

df= pandas.read_csv("Day 73- Data Visualization/QueryResults.csv", names=['DATE', 'TAG', 'POSTS'],header=0)


data_shape= (df.shape)
rows_num= data_shape[0]
cols_num= data_shape[1]
print(f"The number of rows are {rows_num} and number of colums are {cols_num}")


col_counts= df.count()

col_list=[]
for counttss in col_counts:
  col_list.append(counttss)

print(f"The count of date is {col_list[0]}, count of tag is {col_list[1]} , and count of posts is {col_list[2]} ")


#TO FIRST FIND MAX POSTS COUNT

max_post= df["POSTS"].idxmax()
max_post_lang= df["TAG"][max_post]
print(max_post)
print(max_post_lang)


# MAKE A FUNCTION THAT RETURNS NUMBER OF TIMES THE MONTHS REPEATED FOR ANY LANGUAGE.
def get_months_by_proglang(current_lang):
  df_tags= df["TAG"]

  total_months_for_lang= 0
  for test_tag in df_tags:
    if str(test_tag)==current_lang:
      total_months_for_lang+=1


  print(total_months_for_lang)


get_months_by_proglang("c#")



#OR SHORTCUT



group_by_lang= df.groupby('TAG').count()
print(group_by_lang["POSTS"])

test_df = pandas.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)


# Can you pivot the df DataFrame so that each row is a date and each column is a programming language? Store the result under a variable called reshaped_df. 

reshaped_df= df.pivot(columns="TAG",index="DATE",values="POSTS")
print(reshaped_df)


shape_of_reshaped= reshaped_df.shape
print(f"{shape_of_reshaped[0]} rows and {shape_of_reshaped[1]} columns")

#PRINT THE NAMES OF THE COLUMNS
ALL_COLUMN_PIVOTED=pivoted_df.columns
base_line = "The names of the actors are"

for insdas in ALL_COLUMN_PIVOTED:
    base_line = f"{base_line}, {insdas}"

print(base_line)

reshaped_df = reshaped_df.fillna(0) 
#To Count the number of entries per column.

print(reshaped_df.count())


import matplotlib.pyplot as plt

roll_df = reshaped_df.rolling(window=6).mean()
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=column)

plt.legend(fontsize=14)  # Add legend with fontsize
plt.title('Time Programming Graph', fontsize=18)
plt.xlabel('X-axis Label', fontsize=16)
plt.ylabel('Y-axis Label', fontsize=16)


#Add sime

def vericas():
   return True
plt.show()



