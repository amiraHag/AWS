# This is the type play ground

x = 5
print(type(x))

y = float(x)
print(type(y))

z= str(x)
print(type(z))

mon_loss = "0.15"
tues_loss = "0.12"
wed_loss = "0.13"
thurs_loss = "0.10"
fri_loss = "0.11"
sat_loss = "0.09"
sun_loss = "0.08"

# TODO: assign the total loss to a string with this format: This week's total loss: xxx
# You will probably need to write some lines of code before the assigning statement.

# Convert string loss values to float and calculate the total loss
total_loss = float(mon_loss) + float(tues_loss) + float(wed_loss) + float(thurs_loss) + float(fri_loss) + float(sat_loss) + float(sun_loss)  

# Format the result string
result_string = "This week's total loss: {:.2f}".format(total_loss)
print(result_string)

### Notebook grading
if result_string == "This week's total loss: 0.78":
    print("You calculated the correct sum and formatted the string correctly. Nice work!")
else:
    print("That doesn't match the solution. The total loss should be 0.78. If that's what you got, check that your string is formatted correctly.")
