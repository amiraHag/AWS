# Part 1: Define the dictionary
# TODO: replace None with appropriate code
# Define a dictionary, `model_accuracies`, that provides information
# on the accuracies of different image classification models. 
# The key is the name of a model (a string), and the associated value 
# is its accuracy (a float).
#   Key      |   Value
# ResNet     |   0.91
# AlexNet    |   0.85
# VGG        |   0.88
# Inception  |   0.92
model_accuracies = {"ResNet": 0.91, "AlexNet": 0.85, "VGG": 0.88, "Inception": 0.92}

# Part 2: Calculate the average accuracy
# TODO: replace None with appropriate code
average_accuracy = sum(model_accuracies.values()) / len(model_accuracies)

# Part 3: Find the best model
# TODO: replace None with appropriate code
best_model = max(model_accuracies, key=model_accuracies.get)
print(best_model)

# Part 4: Add a new model
# TODO: replace None with appropriate code
# Add the model MobileNet with an accuracy of 0.89
new_model = 'MobileNet'
new_accuracy = 0.89

# Add the new model to the dictionary
model_accuracies[new_model] = new_accuracy
print(model_accuracies)

### Notebook grading
model_accuracies_solution = {
    "ResNet": 0.91, 
    "AlexNet": 0.85,
    "VGG": 0.88,
    "Inception": 0.92,
    "MobileNet": 0.89
}

if model_accuracies == model_accuracies_solution:
    print("Nice work defining the dictionary!\n")

average_accuracy_solution = 0.89
if average_accuracy == average_accuracy_solution:
    print("Nice work calculating the average accuracy!\n")
else:
    print(f"Double check your average accuracy calculation. It should be {average_accuracy_solution}.")

best_model_solution = 'Inception'
if best_model == best_model_solution:
    print("Nice work finding the best model!\n")
else:
    print(f"Double check your best model calculation. It should be {best_model_solution}.")


# invalid dictionary - this should break but we convert list to tuples by change [] to ()
room_numbers = {
    ('Freddie', 'Jen'): 403,
    ('Ned', 'Keith'): 391,
    ('Kristin', 'Jazzmyne'): 411,
    ('Eugene', 'Zach'): 395
}
print(room_numbers)