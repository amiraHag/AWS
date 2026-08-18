# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."

### Notebook grading
if ford_quote == "Whether you think you can, or you think you can't--you're right.":
    print("You fixed the string, nice work!")
else:
    print("Your code has no errors, but the `ford_quote` variable has the wrong value. Double check your work!")


username = "Kinari"
timestamp = "04:50"
predicted_label = "cat"

# TODO: write a log message using the variables above.
# The message should have the same format as this one:
# "User Kinari received a prediction of cat at 04:50."

message = "User " + username + " received a prediction of " + predicted_label +" at " + timestamp +"."

### Notebook grading
def space_error(message):
    feedback = ""
    error = False
    """see if students forget to include a space"""
    if message == '':
        error = True
        feedback = 'Looks like you are not printing anything!'
        return error, feedback
    if message[0]=='"' or message[-1]=='"':
        feedback = "The line does not need to start or end with quotes."
        error = True
    if "Kinarireceived" in message:
        feedback = 'You forgot to include a space between "Kinari" and "received".'
        error = True
    if "predictionof" in message:
        error = True
        feedback = 'You forgot to include a space between "prediction" and "of".'
    if "at04" in message:
        error = True
        feedback = 'You forgot to include a space between "at" and the timestamp.'
    if message == ' ':
        error = True
        feedback = 'Looks like you are printing a space!'
    if message == "User Kinari received a prediction of cat at 04:50":
        feedback = 'Your log message doesn\'t have a period "." at the end'
        error = True
    if 'User Yogesh' in message or 'dog' in message or '16:20' in message:
        feedback = 'Use the variables `username`, `timestamp`, and `predicted_label` in the log message.'
        error = True
    return error, feedback
    
error, feedback = space_error(message)
if message == "User Kinari received a prediction of cat at 04:50.":
    print("Nice work!")
elif error:
    print(feedback)
else:
    print('That\'s not quite right. Are you formatting your string correctly?')


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# TODO: calculate how long this name is
full_name = given_name + " " + middle_names + " " + family_name
name_length = len(full_name)

# Now we check to make sure that the name fits within the named entity character limit
# Uncomment the code below. You don't need to make changes to the code.

# named_entity_character_limit = 28
# print(name_length <= named_entity_character_limit)

### Notebook grading
if name_length == 20:
    print("Good job!")
elif name_length == 18:
    print("Your result doesn't match the solution. Did you remember to count for the spaces between each part of the name?")
else:
    print("Your result doesn't match the solution. Double check your code.")