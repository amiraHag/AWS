# Actual and predicted accuracies
actual_accuracy = 0.85  # replace with actual accuracy
predicted_accuracy = 0.80  # replace with predicted accuracy

# Compare predicted accuracy to actual accuracy
# TODO
if actual_accuracy > predicted_accuracy:
    result = "Oops! Your prediction was too low."
elif actual_accuracy < predicted_accuracy:
    result = "Oops! Your prediction was too high."
else:
    result = "Nice! Your prediction matched the actual accuracy!"

print(result)
### Notebook grading
def get_solution(actual_accuracy, predicted_accuracy):
    if predicted_accuracy < actual_accuracy:
        return "Oops! Your prediction was too low."
    elif predicted_accuracy > actual_accuracy:
        return "Oops! Your prediction was too high."
    else:
        return "Nice! Your prediction matched the actual accuracy!"

if result == get_solution(actual_accuracy, predicted_accuracy):
    print("Good job!")
else:
    print("Try again. That doesn't look like the expected answer.")



# Provider and computation cost
provider = "AWS"  # Either "AWS", "Azure", or "GCP"
computation_cost = 1000  # amount of computation cost

# Determine the cost rate based on the provider and calculate the total cost
# TODO
if provider == "AWS":
    cost_rate = .075
    total_cost = computation_cost * (1 + cost_rate)
    result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
elif provider == "Azure":
    cost_rate = .095
    total_cost = computation_cost * (1 + cost_rate)
    result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
elif provider == 'GCP':
    cost_rate = .089
    total_cost = computation_cost * (1 + cost_rate)
    result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
else:
    result = "Provider not recognized."
    
    
    
    
### Notebook grading
def get_solution(provider, computation_cost):
    if provider == 'AWS':
        cost_rate = .075
        total_cost = computation_cost * (1 + cost_rate)
        result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
    elif provider == 'Azure':
        cost_rate = .095
        total_cost = computation_cost * (1 + cost_rate)
        result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
    elif provider == 'GCP':
        cost_rate = .089
        total_cost = computation_cost * (1 + cost_rate)
        result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
    else:
        result = "Provider not recognized."
    return result

if result == get_solution(provider, computation_cost):
    print("Good job!")
else:
    print("Oops! That doesn't look like the expected answer.")