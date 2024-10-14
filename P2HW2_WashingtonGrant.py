# Grant Washington
# 10/14/24
# P2HW2
# Brief description of program

yearly_grades = set()
module1 = yearly_grades.add(float(input("Enter grade for Module 1: ")))
module2 = yearly_grades.add(float(input("Enter grade for Module 2: ")))
module3 = yearly_grades.add(float(input("Enter grade for Module 3: ")))
module4 = yearly_grades.add(float(input("Enter grade for Module 4: ")))
module5 = yearly_grades.add(float(input("Enter grade for Module 5: ")))
module6 = yearly_grades.add(float(input("Enter grade for Module 6: ")))

highest_grade = max(yearly_grades)
lowest_grade = min(yearly_grades)
sum_of_grades = sum(yearly_grades)
average_of_grades = sum_of_grades/len(yearly_grades)

print("---------Results----------------------------")
print(f'Lowest Grade:     {lowest_grade:.1f} ')
print(f'Highest Grade:    {highest_grade:.1f} ')
print(f'Sum of Grades:    {sum_of_grades:.1f}')
print(f'Average:          {average_of_grades:.2f}')
print('---------------------------------------------')
