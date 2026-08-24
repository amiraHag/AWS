accuracy = 0.88  # use this as input for your submission

# Establish the default performance level to None
performance = None

# Use the accuracy value to assign performance levels to the correct performance names
# TODO

if  0 <= accuracy <= 0.5:
    performance = "Poor performance"
elif  0.51 <= accuracy <= 0.75:
    performance = "Average performance"
elif  0.76 <= accuracy <= 0.9:
    performance = "Good performance"
elif  0.91 <= accuracy <= 1:
    performance = "Excellent performance"
else:
    performance = "NO Accuracy Given"


# Use the truth value of performance to assign result to the correct phrase
if performance:
    result = "The model has achieved {}.".format(performance)
else:
    result = "Performance level not defined."

### Notebook grading
if result == "The model has achieved Good performance.":
    print("Good work!")
else:
    print("Not quite! Are your result string formatted correctly?")