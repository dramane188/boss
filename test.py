import os
import csv
file_num = 2
#creates file path as file
#csvpath = os.path.join(''..','resources','employee_data.csv')
csv_file = os.path.join('employee_data.csv')
#employee_data.csv = os.path.join('..', 'Resources', 'employee_data.csv')
#open the csv 
#with open(employee_data.csv) as csv_file:
#csv_reader = csv.reader(csv_file, delimiter=',')
#with open(csv.reader, newline='') as csv_file:
#csv_file = os.path.join("raw_data" , input('please input the entire file name:'))
#state dictionary

#empty lists for parsed data
Emp_ID = [ ]
First_name = [ ]
Last_name = [ ]
DOB = [ ]
SSN = [ ] 
State = [ ]
#open csv_fille and reads in as dictionary
Emp_IDmain = input('what is your ID number' + 'r')
csv_reader = csv.reader(csv_file, delimiter=',')
with open(csv_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
        Emp_ID.append (row['Emp ID'])
        First_name.append(row['Name'].split(' ')[0])
        Last_name.append(row['Name'].split(' ')[1])
        DOB.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] +'/' + row['DOB'].split('-')[0])
        SSN.append('***-**-' + row['SSN'].split('-')[2])
        State.append(row['State'])
    #zips lists together
    new_data = zip(Emp_ID, First_name, Last_name, DOB, SSN, State)
    #names outputfile as emp_data_clean
    output_file = os.path.join('emp_data_clean' + str(file_num) + '.csv')
    #writes the results to a new csv file
    with open(output_file, 'w') as csvwrite:
        clean_file = csv.writer(csvwrite, delimiter = ',')
        clean_file.writerow(['Emp ID, First_name', 'Last_name', 'DOB', 'SSN', 'State'])
        clean_file.writerows(new_data)




