
# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

# Approach

I initially set out to create two separate python programs to create the top ten lists for Occupations and States. However, as I completed it, I realized that the code was so similar, I was able to combine the code after making a few adjustments. Additionally, I can reduce the time by almost a factor of two by creating both data sets at once. A short sorting function was added so the code didn't have to be repeated.

When the python script is run, it pulls the heading from the Department of Labor data file, and finds out which columns contain the information required. During the test run, quotations were found around some of the names in the data, and were removed using regex.

The data in the document is then gone through, 10,000 bytes at a time (rounded to the nearest line) so it is able to handle large data inputs. The program goes line by line, counting the certified candidates by both "Occupation" and "State", creating two separate dictionaries with the data.

Those dictionaries are then turned into a list of lists, and sorted by the count (decending), and then by alphabetically ascending. The sorted list is then limited to ten entries, and the percentage is calculated using the counted number of occupation or state, and then divided by the counted number of total certified candidates. The data is formatted and then written to a document along with the header. 


#Limitations

The column names in the data file must match "SOC_NAME", "CASE_STATUS", and "WORKSITE_STATE". I ran into problems with the worksite state in the 2014 data, and the column names were so dissimilar, that I'm not sure how to ensure a correct match, as there are different instances of "state" columns. 

# Run Instructions

Navigate in the command line to the h1b_statistics folder, and type "./run.sh". Output should be in the output folder from the root directory.

