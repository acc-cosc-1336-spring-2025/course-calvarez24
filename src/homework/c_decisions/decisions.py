def get_options_ratio(x, y):
    return  x / y

def get_faculty_rating(x):
    rating = x
    if rating >= .9 and rating <= 1:
        return "Excellent"
    elif rating >= .8:
        return "Very Good"
    elif rating >= .7:
        return "Good"
    elif rating >=.6:
        return "Needs Improvement"
    elif rating >= 0 and rating <= .59:
        return "Unacceptable"
    else:
        rating = "Invalid Ratio"

def sum_odd_numbers(num):
    sum = 0
    i = 1
    while 1 <= num:
        if i % 2 != 0:
            sum += i
        i += 1
    return sum
