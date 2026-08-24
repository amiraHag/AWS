model_names = ["Model1", "Model2", "Model3", "Model4", "Model5"]
accuracy = [0.95, 0.89, 0.92, 0.87, 0.93]
precision = [0.94, 0.88, 0.91, 0.86, 0.92]
recall = [0.93, 0.87, 0.91, 0.85, 0.91]
model_metrics = []

# write your for loop here
# TODO
for model,acc,prec,reca in zip(model_names, accuracy, precision, recall):
    model_metrics.append(f"{model}: {acc}, {prec}, {reca}")

### Notebook grading
correct_answer = ["Model1: 0.95, 0.94, 0.93", "Model2: 0.89, 0.88, 0.87", "Model3: 0.92, 0.91, 0.91", "Model4: 0.87, 0.86, 0.85", "Model5: 0.93, 0.92, 0.91"]
if model_metrics == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")


model_names = ["Model1", "Model2", "Model3", "Model4", "Model5"]
accuracies = [0.95, 0.89, 0.92, 0.87, 0.93]

model_performance = {}
for model, acc in zip(model_names, accuracies):
    model_performance[model] = acc


### Notebook grading
correct_answer = {"Model1": 0.95, "Model2": 0.89, "Model3": 0.92, "Model4": 0.87, "Model5": 0.93}
if model_performance == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

model_performance = (("Model1", 0.95), ("Model2", 0.89), ("Model3", 0.92), ("Model4", 0.87), ("Model5", 0.93))

# define model_names and accuracies here
model_names, accuracies = zip(*model_performance)

### Notebook grading
correct_answer_names = ("Model1", "Model2", "Model3", "Model4", "Model5")
correct_answer_accuracies = (0.95, 0.89, 0.92, 0.87, 0.93)
if model_names == correct_answer_names and accuracies == correct_answer_accuracies:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

metrics_data = ((0.95, 0.94, 0.93), (0.89, 0.88, 0.87), (0.92, 0.91, 0.90), (0.87, 0.86, 0.85))

metric1, metric2, metric3 = zip(*metrics_data)
print(metric1)
# Transpose the matrix
metrics_data_transpose = [metric1, metric2, metric3]


### Notebook grading
correct_answer = [(0.95, 0.89, 0.92, 0.87), (0.94, 0.88, 0.91, 0.86), (0.93, 0.87, 0.90, 0.85)]
if metrics_data_transpose == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

model_descriptions = ["Model1 Description", "Model2 Description", "Model3 Description", "Model4 Description", "Model5 Description"]
accuracies = [0.95, 0.89, 0.92, 0.87, 0.93]

# write your for loop here
# TODO
for i, model in enumerate(model_descriptions):
    model_descriptions[i] = model + " " + str(accuracies[i])
    print(model_descriptions[i])

### Notebook grading
correct_answer = ["Model1 Description 0.95", "Model2 Description 0.89", "Model3 Description 0.92", "Model4 Description 0.87", "Model5 Description 0.93"]
if model_descriptions == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")