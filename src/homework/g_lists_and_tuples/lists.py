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


def get_p_distance(list1, list2):
    differences = 0
    for a, b in zip(list1, list2):
         if a != b:
            differences += 1
    return differences / len(list1)


def get_p_distance_matrix(dna_lists):
    matrix = []
    for i in range(len(dna_lists)):
        row = []
        for j in range(len(dna_lists)):
            row.append(get_p_distance(dna_lists[i], dna_lists[j]))
        matrix.append(row)
    return matrix 

          
     

