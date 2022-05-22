list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
word_list = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

def binary_search(ordered_list, first_element_index, last_element_index, term): 

    if (last_element_index < first_element_index): 
        return False 
    else: 
        mid_point = first_element_index + ((last_element_index - first_element_index) // 2) 
        if ordered_list[mid_point] > term: 
            return binary_search(ordered_list, first_element_index, mid_point-1,term) 
        elif ordered_list[mid_point] < term: 
            return binary_search(ordered_list, mid_point+1, last_element_index, term) 
        else: 
            return (True)

print(binary_search(list, 0, 9, 31))
print(binary_search(list, 0, 9, 77))
print(binary_search(word_list, 0, 6, 'Delta'))