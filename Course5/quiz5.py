import math
# calculate e to the power of 3 using the math module
result = math.exp(3)

### Notebook grading
import math
correct = math.exp(3)

if round(result,12) == round(correct,12):
    print("Nice job!")
else:
    print("Your code produced the wrong result. Expected answer is `20.085536923187668`.")



# TODO: First import the `random` module
import random

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# TODO: Add your function generate_password below
def generate_password():
    return ''.join(random.sample(word_list, 3))
# It should return a string consisting of three random words 
# concatenated together without spaces

# Now we test the function
password = generate_password()

### Notebook grading
pswd1 = generate_password()
pswd2 = generate_password()
pswd3 = generate_password()
    
def feedback(pswd1, pswd2, pswd3):
    fb = ""
    correct = 0
    if (not isinstance(pswd1, str)) or (not isinstance(pswd2, str)) or (not isinstance(pswd3, str)):
        fb = "Try again. Your function does not return a string."
    elif (not 11<len(pswd1)<22) or (not 11<len(pswd2)<22) or (not 11<len(pswd3)<22):
        fb = "Try again. The password that your function returns is either too short or too long."
    elif (pswd1==pswd2) or (pswd2==pswd3) or (pswd1 == pswd3):
        fb = "Try again. Your function returns the same passwords when called multiple times."
    else:
        fb = "Your code passes all of our tests, nice work!"
        correct = 1
    return fb, correct
fb, correct = feedback(pswd1, pswd2, pswd3)

if correct:
    print(fb)
else:
    print(fb)