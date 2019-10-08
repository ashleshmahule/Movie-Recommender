import pandas as pd

rating_col = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv(r'''H:\Python\Data Science\ml-100k\u.data''', sep='\t', names=rating_col, usecols=range(3), encoding="ISO-8859-1")

movie_col = ['movie_id', 'title']
movies = pd.read_csv(r'''H:\Python\Data Science\ml-100k\u.item''', sep='|', names=movie_col, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

print(ratings.head())

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(serRatings.head())

corrMatrix = userRatings.corr()
print(corrMatrix.head())

corrMatrix = userRatings.corr(method='pearson', min_periods=100)
print(corrMatrix.head())

myRatings = userRatings.loc[0].dropna()
print(myRatings)

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    
    sims = corrMatrix[myRatings.index[i]].dropna()

    sims = sims.map(lambda x: x * myRatings[i])

    simCandidates = simCandidates.append(sims)
    
print ("Sorting the list")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))


simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head(10))

filteredSims = simCandidates.drop(myRatings.index)
print(filteredSims.head(10))
