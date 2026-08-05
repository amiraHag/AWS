# Accuracy scores for the last three months
accuracy_scores = [85.5, 90.2, 87.3]

# Calculate the average accuracy
average_accuracy = sum(accuracy_scores)/len(accuracy_scores)

print(f"The average prediction accuracy over the last three months is {average_accuracy:.2f}%")


# Sizes of datasets (in images)
dataset1_size = 4000
dataset2_size = 3000

# Size of each image in KB
image_size_kb = 256

# Calculate total storage needed (in KB)
total_storage_kb = image_size_kb * (dataset1_size + dataset2_size)

# Convert total storage needed to MB
total_storage_mb = total_storage_kb / 1024
print(f"Total storage needed: {total_storage_mb:.2f} MB")

# Storage device capacity (in MB)
device_capacity_mb = 2048

# Calculate leftover storage in MB
leftover_storage_mb = device_capacity_mb - total_storage_mb
print(f"Storage left after storing all images: {leftover_storage_mb:.2f} MB")
