import os
from helper_functions import sort_occupation
import re

def top_occupations(file):
    #this first part gathers the index values for each column to use on the following lines
    data = open(file, 'r')
    heading = data.readline()
    heading_list = heading.split(";")
    occupation_index = heading_list.index("SOC_NAME")
    certified_index = heading_list.index("CASE_STATUS")

    print(heading)
    print(heading_list)
    print(occupation_index)
    print(certified_index)
    applicant_data = {}
    #key:value pair = (Occupation, (# certified, total applications)
    read_data = data.readlines(10000)
    #Takes each line of data, processes into a list, and retrieves the occupation and the certification status of the visa, and puts it into applicant_data
    while read_data:
        for line in read_data:
            applicant = line.split(";")
            applicant[occupation_index] = re.sub('\"', '', applicant[occupation_index])
            print(applicant[occupation_index])
            if applicant[occupation_index] not in applicant_data:
                applicant_data[applicant[occupation_index]] = [0,1]
                if applicant[certified_index] == "CERTIFIED":
                    applicant_data[applicant[occupation_index]][0] += 1
            else:
                applicant_data[applicant[occupation_index]][1] += 1
                if applicant[certified_index] == "CERTIFIED":
                    applicant_data[applicant[occupation_index]][0] += 1



        read_data = data.readlines(10000)
    print(applicant_data)

    occ_sorted = sort_occupation(applicant_data)

    print(occ_sorted)


    output_heading = "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"

if __name__ == "__main__":
    top_occupations('../insight_testsuite/tests/test_1/input/h1b_input.csv')