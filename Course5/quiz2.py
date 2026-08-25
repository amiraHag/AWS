def resource_allocator(resources, tasks):
    """Allocates resources to tasks and handles division by zero errors."""
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
        resources_per_task = resources // tasks
        leftovers = resources % tasks
        return resources_per_task, leftovers
    except ZeroDivisionError as e:
        print("Error: {}".format(e))
        print("Error: Number of tasks cannot be zero. Please enter a positive number of tasks.")
        return None, None

    
# The main code block is below
def main():
    lets_optimize = 'y'
    while lets_optimize == 'y':
        try:
            resources = int(input("How many computational resources (computers) are available? "))
            if resources < 0:
                print("Number of resources cannot be negative. Please enter a positive number.")
                continue

            tasks = int(input("How many tasks (people) need resources? "))
            if tasks < 0:
                print("Number of tasks cannot be negative. Please enter a positive number.")
                continue

            resources_each, leftovers = resource_allocator(resources, tasks)

            if resources_each is not None:
                message = "\nResource Allocation: We'll have {} tasks, each will get {} resources, and we'll have {} resources left over."
                print(message.format(tasks, resources_each, leftovers))

            lets_optimize = input("\nWould you like to optimize more? (y or n) ").lower()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
