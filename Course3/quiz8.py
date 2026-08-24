# Initial learning rate
initial_lr = 0.1
# Decay factor
decay_factor = 0.9
# Number of epochs
epochs = 5

# Initialize current learning rate
current_lr = initial_lr
# Initialize current epoch
current_epoch = 0

# While loop to apply learning rate decay
# TODO
while current_epoch < epochs:
    current_lr *= 0.9
    current_epoch += 1
    print(current_lr)

# Notebook grading
if abs(current_lr - 0.059049) < 1e-6:
    print("Nice work!")
else:
    print("Not quite. Check your learning rate calculations.")



# Model parameters
parameters = [0.5, 1.5, -0.5]
# Corresponding gradients
gradients = [0.1, -0.2, 0.05]
# Learning rate
learning_rate = 0.01

# For loop to update each parameter
# TODO
for i in range(len(parameters)):
    parameters[i] = parameters[i] - gradients[i]*learning_rate

# Notebook grading
if parameters == [0.499, 1.502, -0.5005]:
    print("Nice work!")
else:
    print("Not quite. Check your parameter updates.")