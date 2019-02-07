def recommendations(name, cosine_sim = None):
    #empty list of restaurant
    recommended_restaurants = []
    if name in df['rest_name'].values:

        #find index of restaurant that matches the name
        rest_index = df[df['rest_name'] == name].index[0]

        #Find the index in the cosine matrix
        matching_index = pd.Series(cosine_sim[rest_index]).sort_values(ascending = False)

        #find top 5
        similar_indices = list(matching_index[1:6].index)

        #Print top 5 recs
        for i in similar_indices:
            recommended_restaurants.append(df.rest_name[i])
            print(f'{df.rest_name[i]} , rating = {df.rest_rating[i]}, cost = {df.rest_cost[i]}')

    else:
        print(f'Sorry, we can\'t find what you\'re looking for. Please try a different restaurant')


def create_sim_matrix(df, cols_to_drop):
    from sklearn.metrics.pairwise import cosine_similarity
    cos_sim = cosine_similarity(df.drop(cols_to_drop, axis = 1), df.drop(cols_to_drop, axis = 1))
    return cos_sim
