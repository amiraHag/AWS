features = [
    "Feature 1: High accuracy",
    "Feature 2: Low latency",
    "Feature 3: Scalability",
    "Feature 4: Robustness",
    "Feature 5: Interpretability"
]

feature_summary = ""
# Write your loop here
# TODO
for feature in features:
    if len(feature_summary) + len(feature) + 1 > 140:
        if feature_summary:
            feature_summary += "\n"
        feature_summary += feature[:140 - len(feature_summary)]
        break
    if feature_summary:
        feature_summary += "\n"
    feature_summary += feature

# Print the resulting summary
print(feature_summary)

### Notebook grading
def get_solution(features):
    feature_summary = ""
    for feature in features:
        if len(feature_summary) + len(feature) + 1 > 140:
            if feature_summary:
                feature_summary += "\n"
            feature_summary += feature[:140 - len(feature_summary)]
            break
        if feature_summary:
            feature_summary += "\n"
        feature_summary += feature

    return feature_summary

correct_ans = get_solution(features)

if feature_summary == correct_ans:
    print("Well done!")
else:
    print("Make sure you're inserting spaces between each feature, and that the summary is exactly 140 characters long.")