# your code goes here
# Your job is to write a program named 
# restaurant-ratings.py that reads the file, 
# then spits out the ratings in alphabetical 
# order by restaurant.

restaurant_ratings = {}

# restaurant1 = "Arinell's:4"
# restaurant1 = restaurant1.split(":")
# restaurant_ratings["Arinell's"] = 4
# print restaurant_ratings


scores = open("scores.txt")

for line in scores:
    line = line.rstrip()
    line = line.split(":")
    # print line
    # restaurant_ratings[line[0]] = line[1] same as below
    restaurant_name = line[0]
    restaurant_rating = line[1]
    # restaurant_name, restaurant_rating = line     *same as above by unpacking
    restaurant_ratings[restaurant_name] = restaurant_rating
# print restaurant_ratings

# alpha_ratings = sorted(restaurant_ratings.items()) same as below

for restaurant in sorted(restaurant_ratings):
    print "{} is rated at {}.".format(restaurant, restaurant_ratings[restaurant])