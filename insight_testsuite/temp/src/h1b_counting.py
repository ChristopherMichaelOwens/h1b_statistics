
import re

#counts the certified H1B visas by field and state, and outputs the top 10
def h1b_count(file):
    #this first part opens the file, splits the heading into a list, and gathers the index values for each desired column
    data = open(file, 'r', encoding="utf8")
    heading = data.readline()
    heading_list = heading.split(";")
    occupation_index = heading_list.index("SOC_NAME")
    certified_index = heading_list.index("CASE_STATUS")
    state_index = heading_list.index("WORKSITE_STATE")
    #key:value pair = (Occupation: #Certified) or (State : #Certified)
    applicant_occupation_data = {}
    applicant_state_data ={}

    #iterates through the file in small chunks, to handle large amounts of data
    read_data = data.readlines(10000)
    certified_total = 0

    #takes each line of data, processes into a list, and retrieves the occupation, word state, and the certification status of the visa, and puts it into requisite dictionary
    while read_data:
        for line in read_data:
            applicant = line.split(";")
            #removes extra quotes in the entry, as some were found in the test in occupation
            applicant[occupation_index] = re.sub('\"', '', applicant[occupation_index])

            #adds the keys to the dictionaries and increments the values, along with total certified
            if applicant[occupation_index] not in applicant_occupation_data:
                applicant_occupation_data[applicant[occupation_index]] = 0
            if applicant[state_index] not in applicant_state_data:
                applicant_state_data[applicant[state_index]] = 0
            if applicant[certified_index] == "CERTIFIED":
                applicant_occupation_data[applicant[occupation_index]] += 1
                applicant_state_data[applicant[state_index]] += 1
                certified_total += 1

        #feeds more data into the while loop until there's none left
        read_data = data.readlines(10000)

    #converts dictionary to list and sorts it based on certified applicants, and alphabetical occupation in the case of a tie
    #cuts off size to 10 entries
    occ_sorted = sort_dic(applicant_occupation_data)[0:10]
    state_sorted = sort_dic(applicant_state_data)[0:10]

    #creates a new file for each of the counts and writes the heading and data in format
    #occupation: SOFTWARE DEVELOPERS, APPLICATIONS;6;60.0%
    #state: FL;2;20.0%
    occ_file = open("output/top_10_occupations.txt", "x")
    occ_file.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")

    for line in occ_sorted:
        percent = line[1] / certified_total * 100
        occ_file.write(line[0] + ";" + str(line[1]) + ";" + '%.1f' %percent + "%\n" )

    print("Occupation sort complete")

    state_file = open("output/top_10_states.txt", "x")
    state_file.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")

    for line in state_sorted:
        percent = line[1] / certified_total * 100
        state_file.write(line[0] + ";" + str(line[1]) + ";" + '%.1f' %percent + "%\n" )
    print("State sort complete")

#converts dictionary to a list, and orders it by decending count, then alphabetically if any ties.
def sort_dic(dictionary):
    applicant_data_list = []
    for key in dictionary:
        applicant_data_list.append([key,dictionary[key]])

    sorted_occupations = sorted(applicant_data_list, key=lambda x: (-x[1], x[0]))

    return sorted_occupations

if __name__ == "__main__":
    h1b_count('input/h1b_input.csv')
