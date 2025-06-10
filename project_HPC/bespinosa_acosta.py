# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.

# Weekly report
def report_week(habits_dict, task_dict, name):
    """
    Function to print a summary of tasks and habits for the week.
    Parameters:
    - task_dict (dict): The dictionary containing tasks for each day.
    - habits_dict (dict): The dictionary containing habits for the week.
    Returns:
    - None: Prints the summary directly.
    """
    if not habits_dict:
        print("\nNo habits tracked for the week.")
        return
    if not task_dict:
        print("\nNo tasks tracked for the week.")
        return
    print("\n******************************************************")
    print(f"{name} Weekly Report:")
    print("--------------------")
    print("Habits Summary:\n")
    count_completed_habits = 0
    for habit in habits_dict.keys():
        for day, status in habits_dict[habit].items():
            if status:
                count_completed_habits += 1
                status_str = "Completed"
            else:
                status_str = "Not Completed"
        print(f"{habit} completed {count_completed_habits} times this week.")
    print("--------------------")
    print("Tasks Summary:\n")
    completed_tasks = []               # Remade this to comply with the indications but the print_tasks function already does this
    uncompleted_tasks = []
    for day, tasks in task_dict.items():
        for task, status in tasks.items():
            if status:
                completed_tasks.append((task, day))
            else:
                uncompleted_tasks.append((task, day))
    print("Completed Tasks:")
    for task in completed_tasks:
        print(f"\t{task[0]} on {task[1]}")
    print("Uncompleted Tasks:")
    for task in uncompleted_tasks:
        print(f"\t{task[0]} on {task[1]}")
    print("\n******************************************************")
    return


# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = ['dictionaries_1.txt', 'dictionaries_10.txt', 'dictionaries_2.txt', 'dictionaries_3.txt', 'dictionaries_4.txt', 
             'dictionaries_5.txt', 'dictionaries_6.txt', 'dictionaries_7.txt', 'dictionaries_8.txt', 'dictionaries_9.txt'] 

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        report_week(data[0], data[1], file_name)