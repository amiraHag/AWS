# This function prints the dataset size after adding the increment, but does not return anything
def display_new_size(dataset_size, increment):
    new_size = dataset_size + increment
    print(f"New dataset size after adding {increment} GB: {new_size} GB")

# This function returns the dataset size after adding the increment
def get_new_size(dataset_size, increment):
    return dataset_size + increment

# Example usage:
dataset_size = 50  # in GB
increment = 10  # in GB

print('Calling display_new_size...')
return_value_1 = display_new_size(dataset_size, increment)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling get_new_size...')
return_value_2 = get_new_size(dataset_size, increment)
print('Done calling')
print('This function returned: {} GB'.format(return_value_2))


# Write your function here
def data_storage_density(data_amount, land_area):
    return data_amount/land_area
### Notebook grading
import types
explanation_str = '''Your function produced the wrong result when called like this: {}\t
The expected output is: {}'''
if 'data_storage_density' not in locals():
    print("Your code doesn't define `data_storage_density`. Check your spelling.")
elif not isinstance(data_storage_density, types.FunctionType):
    print("`data_storage_density` should be a function.")
elif data_storage_density(10, 1) != 10 / 1:
    print(explanation_str.format('data_storage_density(10, 1)', 10. / 1))
elif data_storage_density(864816, 121.4) != 864816 / 121.4:
    print(explanation_str.format('data_storage_density(864816, 121.4)', 864816. / 121.4))
elif data_storage_density(1234321, 42) != 1234321 / 42:
    print(explanation_str.format('data_storage_density(1234321, 42)', 1234321. / 42))
else:
    print("Nicely done! You can view my solution on the next page.")



# Write your function here
def readable_processing_time(days):
    weeks = days // 7
    remain_days = days % 7
    return f"{weeks} week(s) and {remain_days} day(s)."

### Notebook grading
import random
def readable_processing_time_soltn(days):
    """Print the number of weeks and days in a number of days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

explanation_str = '''Your function produced the wrong result when called like this: readable_processing_time({}). The expected output is: {}'''

test_cases = [1, 6, 7, 9, random.randint(100, 10000)]
test_failed = False

if 'readable_processing_time' not in locals():
    test_failed = True
    print("Your code doesn't define `readable_processing_time`. Check your spelling.")
elif not isinstance(readable_processing_time, types.FunctionType):
    test_failed = True
    print("`readable_processing_time` should be a function.")
else:
    for case in test_cases:
        if readable_processing_time(case) != readable_processing_time_soltn(case):
            test_failed = True
            print(explanation_str.format(case, readable_processing_time_soltn(case)))
            break

    if not test_failed:
        print("Nicely done! You can view my solution on the next page.")