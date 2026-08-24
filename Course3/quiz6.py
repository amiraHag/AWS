model_names = ["Logistic Regression", "Decision Tree", "Random Forest", "Support Vector Machine"]
model_identifiers = []

# Write your for loop here
# TODO
for model_name in model_names:
    model_identifier = model_name.lower().replace(" ","_")
    model_identifiers.append(model_identifier)
### Notebook grading
if model_identifiers == ["logistic_regression", "decision_tree", "random_forest", "support_vector_machine"]:
    print("Nice work!")
else:
    print("Not quite! Did you append each new identifier to the list `model_identifiers`?")

# Write your for loop here
# TODO
for i in range(len(model_identifiers)):
    model_identifiers[i] = model_identifiers[i].lower().replace(" ","_")

### Notebook grading
if model_identifiers == ["logistic_regression", "decision_tree", "random_forest", "support_vector_machine"]:
    print("Nice work!")
else:
    print("Not quite! Did you modify each element in the list `model_identifiers`?")



predictions = ['Predicted: 0.95', 'Actual: 0.90', 'Predicted: 0.85']
count = 0

# Write your for loop here
# TODO
for prediction in predictions:
    if prediction.startswith("Predicted:"):
        count +=1

### Notebook grading
if count == 2:
    print("Nice work!")
else:
    print("Not quite! Did you track the number of predictions with `count`?")




metrics = ['Accuracy: 0.95', 'Precision: 0.92', 'Recall: 0.88']
html_str = "<ul>\n"

# Write your code here
# TODO
for metric in metrics:
    element = "<li>" + metric + "</li>"
    html_str += element + "\n"

html_str +="</ul>"

# Print the resulting HTML string
print(html_str)

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)
word_counter2 = {}
for word in book_title:
    word_counter2[word] = word_counter2.get(word, 0) + 1   
print(word_counter2) 


