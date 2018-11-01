def sort_occupation(dictionary):
    applicant_data_list = []
    for key in dictionary:
        applicant_data_list.append([key,dictionary[key][0],dictionary[key][1]])
    print(applicant_data_list)
    sorted_occupations = sorted(applicant_data_list, key=lambda x: (-x[1], x[0]))

    return sorted_occupations