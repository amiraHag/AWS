# Define the sentence
sentence = "the quick brown fox jumped over the lazy dog"

# Tokenize the sentence into words
words = sentence.split()

# Print each word on a new line
# TODO
for word in words:
    print(word)


# Define the dataset
data = list(range(1, 31))

# Define the batch size
batch_size = 5

# Process the data in batches
# TODO
for i in range(data[0], len(data), batch_size):
    batch_data = data[i: i+batch_size-1]
    print(batch_data)
    print(f"Batch no {i//batch_size +1} :{batch_data}")
