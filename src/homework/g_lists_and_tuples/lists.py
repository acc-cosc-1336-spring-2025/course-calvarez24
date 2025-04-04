def get_lowest_list_value(value_list):
    lowest_value = float('inf')

    for value in value_list:
          if value < lowest_value:
                lowest_value = value

    return lowest_value


def get_highest_list_value(value_list):
    highest_value = float('-inf')

    for value in value_list:
        if value > highest_value:
                highest_value = value 

    return highest_value

