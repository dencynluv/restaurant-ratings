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
    restaurant_ratings[line[0]] = line[1]
# print restaurant_ratings

# alpha_ratings = sorted(restaurant_ratings.items())

for restaurant in sorted(restaurant_ratings):
    print "{} is rated at {}.".format(restaurant_ratings[restaurant], restaurant)