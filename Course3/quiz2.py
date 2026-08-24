accuracy = 0.85  # use this input to make your submission

# write your if statement here
state = ""

if accuracy <= 1 and accuracy >= 0.91:
    state  = "Excellent"
elif  accuracy <= 0.9 and accuracy >= 0.76:
    state  = "Good"
elif  accuracy <= 0.75 and accuracy >= 0.51:
    state  = "Average"
else:
    state  = "Poor"

result = "Model performance: " + state + "."
# Check the result
print(result)

# Notebook grading
if result == "Model performance: Good.":
    print("Nice work!")
else:
    print("Not quite! Are your result strings formatted correctly?")