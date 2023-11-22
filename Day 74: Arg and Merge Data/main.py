import pandas as pd


##FILE PATHS

COLOR_PATH= "/content/colors.csv"
SETS_PATH= "/content/sets.csv"
THEMES_PATH= "/content/themes.csv"


color_df= pd.read_csv(COLOR_PATH)
print(color_df)
count_of_colors= (color_df["name"].count())
print(count_of_colors)

#FIND THE NUMBER OF TRANSPARENT COLORS
transparent_color=color_df.groupby("is_trans").count()["id"][1]
non_transparent_color= color_df.groupby("is_trans").count()["id"][0]
print(f" The number of transparent colors are {transparent_color} and non-transparent are {non_transparent_color}")

import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have a DataFrame named sets_df
# SETS_PATH should be the path to your CSV file

sets_df = pd.read_csv(SETS_PATH)

# Group by "name" and count occurrences
sets_by_year = sets_df.groupby("year").count()["set_num"].reset_index()
print(sets_by_year)

plt.plot(sets_by_year.year[:-2],sets_by_year.set_num[:-2])

# Reset the index to make "name" a regular column


### TO FIND TOP 5 LEGO SETS WITH MOST NUMBER OF PARTS
parts_df = pd.read_csv(SETS_PATH).groupby("name")["num_parts"].sum().sort_values(ascending=False).head().reset_index()

OUTPUT_TEXT= "The top 5 logo sets with most numbers of parts are "

for LOGO_NAME in parts_df["name"]:
  OUTPUT_TEXT+=f",{LOGO_NAME}"

print(OUTPUT_TEXT)



set_df = pd.read_csv(SETS_PATH)

# Group by 'year' and apply the nunique function to get the count of unique theme IDs
themes_by_year = set_df.groupby('year')['theme_id'].agg(pd.Series.nunique).reset_index()
themes_by_year.rename(columns={'theme_id':'nr_themes'},inplace=True)

print(themes_by_year)

ax1 = plt.gca() # get current axes
ax1.set_ylabel('Number of Sets',color="green")

ax2 = ax1.twinx() 
ax2.set_ylabel('Number of Themes',color="blue")

ax1.plot(themes_by_year.year[:-2],themes_by_year.nr_themes[:-2],color="g")
ax2.plot(sets_by_year.year[:-2],sets_by_year.set_num[:-2],color="b")

parts_df= set_df.groupby('year').agg({'num_parts': pd.Series.mean}).reset_index()


plt.scatter(parts_df.year[:-2],parts_df.num_parts[:-2])


set_themes_count = set_df["theme_id"].value_counts().reset_index()
set_themes_count.columns = ['id', 'set_count']


theme_df= pd.read_csv('/content/themes.csv')


merged_db= pd.merge(set_themes_count,theme_df,on='id')
print(merged_db.head())


plt.bar(merged_db.name[:10],merged_db.set_count[:10])