ratings = [['U', 0], ['PG', 0], ['12A', 0], ['12', 12], ['15', 15], ['18', 18], ['R18', 18]]

age = int(input('Enter your age as a number: '))

for rating in ratings:
    if rating[1] <= age:
        print(rating[0])