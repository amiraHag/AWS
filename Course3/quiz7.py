result = 0
model_counts = {'logistic_regression': 4, 'decision_tree': 19, 'random_forest': 3, 'datasets': 8}
model_types = ['logistic_regression', 'decision_tree', 'random_forest', 'support_vector_machine']

# Iterate through the dictionary
# TODO
for model, count in model_counts.items():
    # Check if the model is in the list of model types
    if model in model_types:
        # If it is, add the count to the result
        result += count


### Notebook grading
def get_solution(model_counts, model_types):
    result = 0
    for model, count in model_counts.items():
        if model in model_types:
            result += count
    return result

correct_answer = get_solution(model_counts, model_types)
if result == correct_answer:
    print("Nice work!")
else:
    print("Try again. That doesn't look like what expected.")





# Example 1
result = 0
dataset_items = {'support_vector_machine': 5, 'neural_network': 19, 'random_forest': 3, 'datasets': 8, 'linear_regression': 4}
model_types = ['logistic_regression', 'decision_tree', 'random_forest', 'support_vector_machine']

# Your previous solution here
# TODO
for item,value in dataset_items.items():
    if item in model_types:
        result += value

print(result)

# Example 2
result = 0
dataset_items = {'naive_bayes': 5, 'k_means': 2, 'random_forest': 3, 'datasets': 8, 'decision_tree': 4}
model_types = ['logistic_regression', 'decision_tree', 'random_forest', 'support_vector_machine']

# Your previous solution here
# TODO
for item,value in dataset_items.items():
    if item in model_types:
        result += value
print(result)

# Example 3
result = 0
dataset_items = {'k_means': 2, 'datasets': 3, 'support_vector_machine': 8, 'logistic_regression': 4, 'pandas': 10}
model_types = ['logistic_regression', 'decision_tree', 'random_forest', 'support_vector_machine']

# Your previous solution here
# TODO
for item,value in dataset_items.items():
    if item in model_types:
        result += value
print(result)

model_count, non_model_count = 0, 0
model_counts = {'logistic_regression': 4, 'decision_tree': 19, 'random_forest': 3, 'datasets': 8}
model_types = ['logistic_regression', 'decision_tree', 'random_forest', 'support_vector_machine']

# Iterate through the dictionary
# TODO
for model,count in model_counts.items():
    if model in model_types:
        model_count += count
    else:
        non_model_count +=count

print("Model count:", model_count)
print("Non-model count:", non_model_count)
### Notebook grading
def get_solution(model_counts, model_types):
    model_count, non_model_count = 0, 0
    for model, count in model_counts.items():
        if model in model_types:
            model_count += count
        else:
            non_model_count += count
    return model_count, non_model_count

correct_model, correct_non_model = get_solution(model_counts, model_types)
if model_count == correct_model and non_model_count == correct_non_model:
    print("Nice work!")
else:
    print("Try again. That doesn't look like what expected.")


model_parameters = {'logistic_regression': 100, 'decision_tree': 200, 'random_forest': 300, 'datasets': 50}
model_types = ['logistic_regression', 'decision_tree', 'random_forest', 'support_vector_machine']
total_parameters = 0

# Iterate through the dictionary
# TODO

for parameter,count in model_parameters.items():
    if parameter in model_types:
        total_parameters += count
print(total_parameters)

### Notebook grading
def get_solution(model_parameters, model_types):
    total_parameters = 0
    for model, params in model_parameters.items():
        if model in model_types:
            total_parameters += params
    return total_parameters

correct_total_parameters = get_solution(model_parameters, model_types)
if total_parameters == correct_total_parameters:
    print("Nice work!")
else:
    print("Try again. That doesn't look like what expected.")


model_info = {'model_a': 'regression', 'model_b': 'classification', 'model_c': 'clustering', 'model_d': 'regression'}
model_categories = {'regression': 0, 'classification': 0, 'clustering': 0}

# Iterate through the dictionary
# TODO
for model,category in model_info.items():
    if category in model_categories:
        model_categories[category] += 1



### Notebook grading
def get_solution(model_info, model_categories):
    model_categories = {'regression': 0, 'classification': 0, 'clustering': 0}
    for model, category in model_info.items():
        if category in model_categories:
            model_categories[category] += 1
    return model_categories

correct_model_categories = get_solution(model_info, model_categories)
if model_categories == correct_model_categories:
    print("Nice work!")
else:
    print("Try again. That doesn't look like what expected.")



model_accuracies = {'model_a': 0.95, 'model_b': 0.80, 'model_c': 0.85, 'model_d': 0.90}
accuracy_threshold = 0.85
filtered_models = {}
count = 0

# Iterate through the dictionary
# TODO
for model,accuracy in model_accuracies.items():
    if accuracy >= accuracy_threshold:
        count += 1
        filtered_models[model] = accuracy


### Notebook grading
def get_solution(model_accuracies, accuracy_threshold):
    filtered_models = {}
    count = 0
    for model, accuracy in model_accuracies.items():
        if accuracy >= accuracy_threshold:
            filtered_models[model] = accuracy
            count += 1
    return filtered_models, count

correct_filtered_models, correct_count = get_solution(model_accuracies, accuracy_threshold)
if filtered_models == correct_filtered_models and count == correct_count:
    print("Nice work!")
else:
    print("Try again. That doesn't look like what expected.")