# Dimensions of each image in the format (width, height)
image_dimensions = [(640, 480), (800, 600), (1024, 768), (1280, 720), (1920, 1080)]

# The index of the image for which we want to find the height
image_index = 2

# TODO: replace None with appropriate code
# Use list indexing to determine the height for `image_index`
image_height = image_dimensions[image_index][1]

### Notebook grading
correct_answer = 768
if image_height != correct_answer:
    print("Not quite! Did you account for zero-based indexing?")
else:
    print("Nice work! I found image_height like this: `image_dimensions[image_index][1]`.")


# Filenames of images
image_filenames = ['img_001.jpg', 'img_002.jpg', 'img_003.jpg', 'img_004.jpg', 'img_005.jpg', 'img_006.jpg']

# TODO: Replace None with appropriate code
# Modify this code so it prints the filenames of the last three images
last_three_filenames = image_filenames[-3:]

### Notebook grading
correct_answer = ['img_004.jpg', 'img_005.jpg', 'img_006.jpg']
if last_three_filenames != correct_answer:
    print("Double check your slicing! Your code should print a list of the last three filenames from the original list, and nothing else.")
else:
    print('''My solution is this: `image_filenames[-3:]`
This slice uses a negative index to begin slicing three elements from the end of the list. The end index can be omitted because this slice continues until the end of the list.''')




# Predicted classes of a series of images
image_classifications = ['dog', 'cat', 'bird', 'cat', 'dog']

# TODO: replace None with appropriate code
# Use list slicing to reverse the list and check if it forms a palindrome
is_palindrome = image_classifications == image_classifications[::-1]

### Notebook grading
correct_answer = True
if is_palindrome != correct_answer:
    print("Not quite! Remember to use list slicing to reverse the list and check if it matches the original list.")
else:
    print("Nice work! I found is_palindrome like this: `image_classifications == image_classifications[::-1]`.")
