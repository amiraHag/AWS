total_images = 100
batch_size = 20

processed_images = 0
# TODO
while processed_images < total_images:
    print(f"processing images from {processed_images} to {processed_images + batch_size}")
    processed_images += batch_size
    

### Notebook grading
def get_solution(total_images, batch_size):
    processed_images = 0
    while processed_images < total_images:
        processed_images += batch_size
    return processed_images

correct = get_solution(total_images, batch_size)

if processed_images == correct:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")


total_images = 100
batch_size = 20

if total_images < batch_size:
    processed_images = total_images
else:
    processed_images = 0
    while processed_images < total_images:
        processed_images += batch_size

result = processed_images

### Notebook grading
def get_solution(total_images, batch_size):
    if total_images < batch_size:
        return total_images
    else:
        processed_images = 0
        while processed_images < total_images:
            processed_images += batch_size
        return processed_images

correct_ans = get_solution(total_images, batch_size)

if result == correct_ans:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

limit = 50
nearest_batch = 0
current_value = 0

# TODO
while (current_value + 1) **2 <= limit:
    current_value += 1
    nearest_batch = current_value **2
    

### Notebook grading
def get_solution(limit):
    current_value = 0
    while (current_value + 1)**2 < limit:
        current_value += 1
        nearest_batch = current_value**2
    return nearest_batch

correct_ans = get_solution(limit)

if nearest_batch == correct_ans:
    print("Good job!")
else:
    print("Not quite. Did you assign your result to `nearest_batch`?")


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_list = list()
index = 0
while len(odd_list) < 5:
   if num_list[index]%2 == 1:
       odd_list.append(num_list[index])
   index += 1

print(odd_list)
print(sum(odd_list))


manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# Breaks the loop if weight is greater than or equal to the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))