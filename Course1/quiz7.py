## String method playground

# Example usage of some string methods
sample_text = "Hello, World! This is a sample text for NLP tasks."

# Convert the text to lowercase
lower_text = sample_text.lower()
print("Lowercase:", lower_text)

# Replace 'World' with 'Universe'
replaced_text = sample_text.replace('World','Universe')
print("Replaced text:", replaced_text)

# Split the text into words
words = sample_text.split()
print("Words:", words)

# Try out more string methods from the Python documentation link provided
print("Length of the text:", len(sample_text))
print("Count of 'is':", sample_text.count('is'))
print("Starts with 'Hello':", sample_text.startswith('Hello'))
print("Ends with 'tasks.':", sample_text.endswith('tasks.'))
print("Find index of 'sample':", sample_text.find('sample'))
print("Is the text alphanumeric?:", sample_text.isalnum())
print("Is the text alphabetic?:", sample_text.isalpha())
print("Is the text a digit?:", sample_text.isdigit())
print("Is the text whitespace?:", sample_text.isspace())


# Write two lines of code below, each assigning a value to a variable
model_name = "BERT"
accuracy = 92.5

# Now write a print statement using .format() to print out a sentence and the values of both of the variables
# TODO
print("The Model Name is {} and it is accuracy is {}".format(model_name, accuracy))
print(f"The Model Name is {model_name} and it is accuracy is {accuracy}")
