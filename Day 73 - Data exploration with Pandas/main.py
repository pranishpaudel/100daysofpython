import pandas



df= pandas.read_csv("salaries_by_college_major.csv")
clean_db= df.dropna()
wanted_column= clean_db["Starting Median Salary"]
post= (wanted_column.idxmax())
print(clean_db["Undergraduate Major"].loc[post])



#What college major has the highest mid-career salary? How much do graduates with this major earn?

mid_range_id_max= clean_db["Mid-Career Median Salary"].idxmax()
Mid_Career_Median_Salary= clean_db["Undergraduate Major"].loc[mid_range_id_max]
GRADUATES_EARNING= clean_db["Mid-Career Median Salary"].loc[mid_range_id_max]
print(Mid_Career_Median_Salary)
print(GRADUATES_EARNING)


#Which college major has the lowest starting salary and how much do graduates earn after university?
LOWEST_STARTING_SALARY_INDEX= clean_db["Starting Median Salary"].idxmin()
LOWEST_STARTING_SALARY_MAJOR= clean_db["Undergraduate Major"].loc[LOWEST_STARTING_SALARY_INDEX]
GRADUATES1_EARNING= clean_db["Starting Median Salary"].min()
print(LOWEST_STARTING_SALARY_MAJOR)
print(GRADUATES1_EARNING)



#How would we calculate the difference between the earnings of the 10th and 90th percentile?


diff_db= clean_db['Mid-Career 90th Percentile Salary'] - clean_db['Mid-Career 10th Percentile Salary']

clean_db.insert(1,"Spread",diff_db)
# print(clean_db.head())


#To see which degrees have the smallest spread, we can use the .sort_values() method. 
low_risk= clean_db.sort_values("Spread",ascending=False)

# print(low_risk[['Undergraduate Major','Spread']].head())



# find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile. 



ninthith_per= clean_db.sort_values("Mid-Career 90th Percentile Salary",ascending=False)
top_5_ninthith_per= ninthith_per["Undergraduate Major"].head()

print("\n")
#PRINTING OUT THE ACTUAL MAJORS WITH HIGHEST 90th PERCENTILE
for top_majors in top_5_ninthith_per:
  print(top_majors)

#find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation.

spread_per= clean_db.sort_values("Spread",ascending=False)
top_spread_per= spread_per["Undergraduate Major"].head()
print("\n")
#PRINTING OUT THE ACTUAL MAJORS WITH HIGHEST SPREAD
for top_majorss in top_spread_per:
  print(top_majorss)


print("\n")

count_major= clean_db.groupby("Group").count()["Mid-Career Median Salary"]
print(count_major)
print("\n")
count_major_salary= clean_db.groupby("Group")["Starting Median Salary"].mean().idxmax()
print(count_major_salary)








