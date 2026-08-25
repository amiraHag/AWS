names =  list(map(str,input("Enter the names of the students separated by commas: ").title().split(",")))
assignments =  list(map(int, input("Enter the number of assignments left for each student separated by commas: ").split(",")))
grades =  list(map(int, input("Enter the grades for each student separated by commas: ").split(",")))

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(names)):
    name = names[i].strip()
    assignment = assignments[i]
    grade = grades[i]
    potential_grade = grade + (assignment * 10)  # Assuming each assignment is worth 10 points
    print(message.format(name, assignment, grade, potential_grade)) 