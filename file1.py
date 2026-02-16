import pandas as pd 

df = pd.read_excel('data/USvideos.xlsx')
print(df.head())

total_views_sum = df['views'].sum()
print("Total views is:",total_views_sum)


min_views = df['views'].min()
print("Minimum views is:",min_views)

max_views = df['views'].max()
print("Maximum views is:",print(max_views))


mean_views = df['views'].mean()
print("The average of views is :",mean_views)

median_views = df['views'].median()
print("The median of views is:",median_views)


#taking 10000 random data in pandas
sample_views = df.sample(n=10000,random_state = 42)
#.sample() method is the tool pandas uses for random selection.
mean_sample_views = sample_views['views'].mean()
print("The sample average of views is :",mean_sample_views)


median_sample_views = sample_views['views'].median()
print("The sample median of views is:",median_sample_views)

# print(mean_sample_views)
# print(median_sample_views)