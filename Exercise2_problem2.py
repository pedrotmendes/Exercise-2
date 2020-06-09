# here is the variable which you use to set the selected month:
month = input('What is the month you want to know the average temperature? ')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

selected_month_index = months.index(month)

print(selected_month_index)

average_temp=[-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5]

selected_temp=average_temp[selected_month_index]

print(selected_temp)

print_statement = 'The average temperature in Helsinki in ' + str(month) + ' is ' + str(selected_temp)

print(print_statement)


from nose.tools import ok_, assert_equal

#Validate the length of two lists are 12
ok_(len(months)==12)
ok_(len(average_temp)==12)

#Validate that variable months and average_temp are lists
ok_(isinstance(months, list), 'Variable months is not a list')
ok_(isinstance(average_temp, list), 'Variable average_temp is not a list')

#Validate the print statement is correct;
# Set selected_month_index to correspond with July before running this cell.
# Note! Your code should work with any of the 12 months!
assert_equal(print_statement, 'The average temperature in Helsinki in July is 18.0')