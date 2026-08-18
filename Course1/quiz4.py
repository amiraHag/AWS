# Model 1 metrics
model1_tp = 50
model1_fp = 10
model1_fn = 5

# Model 2 metrics
model2_tp = 45
model2_fp = 5
model2_fn = 10

# Calculate precision and recall for Model 1
model1_precision = model1_tp / (model1_tp + model1_fp)
model1_recall = model1_tp / (model1_tp + model1_fn)

# Calculate precision and recall for Model 2
model2_precision = model2_tp / (model2_tp + model2_fp)
model2_recall = model2_tp / (model2_tp + model2_fn)

# Compare precision
precision_comparison_result = model1_precision > model2_precision

# Compare recall
recall_comparison_result = model1_recall > model2_recall

# Output the results
print(f"Model 1 Precision: {model1_precision:.2f}")
print(f"Model 1 Recall: {model1_recall:.2f}")
print(f"Model 2 Precision: {model2_precision:.2f}")
print(f"Model 2 Recall: {model2_recall:.2f}")
print(f"Is Model 1 precision higher than Model 2? {precision_comparison_result}")
print(f"Is Model 1 recall higher than Model 2? {recall_comparison_result}")