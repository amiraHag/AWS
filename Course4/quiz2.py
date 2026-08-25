def readable_processing_time(days):
    """ Make the value of time in human-readable format by return the weeks and days

    INPUT:
    days: int. The value of time in days

    OUTPUT:
    str: A String contain the time in weeks and days.

    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

### Notebook grading
import inspect
if 'readable_processing_time' not in locals():
    print("Your code doesn't define the `readable_processing_time` function.")
elif inspect.getdoc(readable_processing_time) is None:
    print("Your function doesn't have a docstring! Add one that explains the function's purpose.")
else:
    print("Nicely done! You can view my solution on the next page.")
