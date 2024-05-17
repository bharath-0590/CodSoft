import numpy as np # type: ignore

# Sample dataset of user ratings
user_ratings = {
    'Alice': {'Inception': 5, 'Avatar': 3, 'Titanic': 4},
    'Bob': {'Inception': 4, 'Avatar': 5, 'Titanic': 3, 'The Dark Knight': 5},
    'Charlie': {'Inception': 2, 'Avatar': 1, 'Titanic': 5, 'The Dark Knight': 4},
    'David': {'Inception': 5, 'Avatar': 2, 'Titanic': 3, 'The Dark Knight': 4},
}

# Function to calculate the Pearson correlation coefficient between two users
def pearson_correlation(user1, user2):
    common_ratings = {}
    for item in user_ratings[user1]:
        if item in user_ratings[user2]:
            common_ratings[item] = 1
            
    num_ratings = len(common_ratings)
    
    if num_ratings == 0:
        return 0

    user1_sum = sum([user_ratings[user1][item] for item in common_ratings])
    user2_sum = sum([user_ratings[user2][item] for item in common_ratings])
    
    user1_squared_sum = sum([np.square(user_ratings[user1][item]) for item in common_ratings])
    user2_squared_sum = sum([np.square(user_ratings[user2][item]) for item in common_ratings])
    
    product_sum = sum([user_ratings[user1][item] * user_ratings[user2][item] for item in common_ratings])
    
    numerator = product_sum - (user1_sum * user2_sum / num_ratings)
    denominator = np.sqrt((user1_squared_sum - np.square(user1_sum) / num_ratings) *
                          (user2_squared_sum - np.square(user2_sum) / num_ratings))
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

# Function to get recommendations for a user
def get_recommendations(target_user):
    totals = {}
    similarity_sums = {}
    
    for other_user in user_ratings:
        if other_user == target_user:
            continue
        similarity = pearson_correlation(target_user, other_user)
        
        if similarity <= 0:
            continue
        
        for item in user_ratings[other_user]:
            if item not in user_ratings[target_user] or user_ratings[target_user][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += user_ratings[other_user][item] * similarity
                similarity_sums.setdefault(item, 0)
                similarity_sums[item] += similarity
    
    rankings = [(total / similarity_sums[item], item) for item, total in totals.items()]
    rankings.sort(reverse=True)
    
    return rankings

# Example usage
target_user = 'Alice'
recommendations = get_recommendations(target_user)

print(f"Recommendations for {target_user}:")
for score, movie in recommendations:
    print(f"{movie}: {score:.2f}")
