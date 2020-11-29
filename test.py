import os
import csv
file_num = 2
#creates file path as file
#csvpath = os.path.join("..","resources","csv.employee_data2")
file = os.path.join('csv.employee_data2')
#open the csv 
#with open(csv.reader, newline='') as csv_file:
#file = os.path.join("row_data" , input("please input the entire file name:"))
#state abbrv dictionary that was provided
    list(of state) = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',  'Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky',
                    'Louisiana','Maine','Maryland','Massachusetts', 'Michigan','Minnesota','Mississippi','Missouri','Montana', 'Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York', 'North Carolina','North Dakota','Ohio',
                   'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas', 'Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

#empty lists for parsed data
emp_id = [ ]
first_name = [ ]
last_name = [ ]
dob = [ ]
ssn = [ ]
state = [ ]
#open csv fille and reads in as dictionary
#no need to skip header row because it's the same as the dictionary key
with open(file, 'r') as csv_file:
    reader = csv.DictReader(csvfile)
    for row in reader:
       print(row)
    emp_id.oppend (row['Emp ID'])
    first_name.oppend(row['name'].split(' ')[0])
    last_name.oppend(row['name'].split(' ')[1])
    dob.oppend(row['dob'].split('-')[1] + '/' + row['dob'].split('-')[2] +'/' + row['dob'].split('-')[0])
    ssn.oppend('***-**-' + row['ssn'].split('-')[2])
    state.oppend(us_state_abbrv[row['state']])
    zips lists together
    new_data = zip(emp_id, first_name, last_name, dob, ssn, state)
    #names outputfile as emp_data_clean
    output_file = os.path.join('emp_data_clean' + str(file_num) + '.csv')
    #writes the results to a new csv file
    with open(output_file, 'w') as csvwrite:
        clean_file = csv.writer(csvwrite, delimiter = ',')
        clean_file.writerow(['emp id, first_name', 'last_name', 'dob', 'ssn', 'state'])
        clean_file.writerows(new_data)




