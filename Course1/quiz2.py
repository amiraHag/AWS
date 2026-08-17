# The initial learning rate for the model
learning_rate = 0.01
# The initial training loss of the model
training_loss = 0.8

# Use the multiplication assignment operator to decrease 
# the learning_rate variable by 10% to account for better stability
learning_rate *= 0.9

### Notebook grading
if learning_rate == 0.01 * 0.9:
    print("Nice job! You can use the multiplication assignment operator like this: learning_rate *= 0.9")
elif learning_rate == 0.01 * 1.1:
    print("Sorry! learning_rate is too high. It looks like you increased the learning rate by 10% instead of decreasing it. Try again")        
else:
    print("Sorry! learning_rate is incorrect. Try again and make sure to use the *= assignment operator")


# Use the addition assignment operator to add 
# a small value (0.02) to the training_loss variable due to noisy data
training_loss += 0.02

### Notebook grading
if training_loss == 0.8 + 0.02:
    print("Nice job! You can use the addition assignment operator like this: training_loss += 0.02")
elif training_loss == 0.8:
    print("Sorry! training_loss is too low. Did you add the noise? Try again")        
else:
    print("Sorry! training_loss is incorrect. Try again and make sure to use the += assignment operator")

# Use the multiplication assignment operator to increase 
# training_loss by 5% to account for overfitting
training_loss *= 1.05

### Notebook grading
if training_loss == (0.8 + 0.02) * 1.05:
    print("Nice job! You can use the multiplication assignment operator like this: training_loss *= 1.05")
elif training_loss == 0.8 + 0.02:
    print("Sorry! training_loss is too low. Did you account for overfitting? Try again")        
else:
    print("Sorry! training_loss is incorrect. Try again and make sure to use the *= assignment operator")

# Use the multiplication assignment operator to decrease 
# training_loss by 5% to account for regularization
training_loss *= 0.95

### Notebook grading
if training_loss == (0.8 + 0.02) * 1.05 * 0.95:
    print("Nice job! You can use the multiplication assignment operator like this: training_loss *= 0.95")
elif training_loss == (0.8 + 0.02) * 1.05:
    print("Sorry! training_loss is too high. Did you account for regularization? Try again")        
else:
    print("Sorry! training_loss is incorrect. Try again and make sure to use the *= assignment operator")

# Use the subtraction assignment operator to subtract 
# a small value (0.05) from training_loss to account 
# for improved generalization due to more training data.
training_loss -= 0.05

### Notebook grading
if training_loss == (0.8 + 0.02) * 1.05 * 0.95 - 0.05:
    print("Nice job! You can use the subtraction assignment operator like this: training_loss -= 0.05")
elif training_loss == (0.8 + 0.02) * 1.05 * 0.95:
    print("Sorry! training_loss is too high. Did you account for the improved generalization? Try again")        
else:
    print("Sorry! training_loss is incorrect. Try again and make sure to use the -= assignment operator")

# Initial learning rate
learning_rate = 1e-3  # Equivalent to 0.001

# Update the learning rate by decreasing it by 10%
learning_rate *= 0.9

print(f"Updated learning rate: {learning_rate}")