
# coding: utf-8

# In[1]:


# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt


# In[2]:


# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")


# In[3]:


# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))


# In[4]:


# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.


# In[5]:


# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])


# In[6]:


input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
print(data_list[:20])


# In[7]:


# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

n = 0

print("\nTASK 2: Printing the genders of the first 20 samples")
for row in data_list[:20]:
    print("Linha", n, row[6])
    n = n+1


# In[9]:


# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order

def column_to_list(data, index):
    """
      function to add the columns(features) of a list in another list in the same order.
      Args:
          param1: list with some colums.
          param2: index of collums that will be added in the another list
      Returns:
          List with the features in the same order
    """
    column_list = []
    for n in data:
        column_list.append(n[index])        
       
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    #print(len(column_list))
    return column_list



# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------


# In[10]:


#input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.

male = 0
female = 0

for gender in column_to_list(data_list, -2):
    
    if gender == "Female":
        female = female + 1
    elif gender == "Male":
        male = male + 1
    else:
        pass


# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------


# In[13]:


input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)

def count_gender(data_list):
    """
      function to count the genders 
      Args:
          param1: list with some columns
      Returns:
          List with two index: 'male' and 'female'
    """
    male = 0
    female = 0
    
    for n in column_to_list(data_list, -2):
        if n == "Female":
            female = female + 1
        elif n == "Male":
            male = male + 1
        else:
            pass
    return [male, female]

print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------


# In[15]:


input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.


def most_popular_gender(data_list):
    
    """
      function to count the genders 
      Args:
          param1: list with some columns
      Returns:
          string with the most popular gender
    """

    answer = ""    
    male, female = count_gender(data_list)
    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    else:
        answer = "Same"
    
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------


# In[17]:


# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.

def count_user_type(data_list):
    
    """
      function to count the user_types 
      Args:
          param1: list with some columns
      Returns:
          List with two index: 'subscriber' and 'customer'
    """

    subscriber = 0
    customer = 0
    for user_type in column_to_list(data_list, -3):
        if user_type == "Subscriber":
            subscriber = subscriber + 1
        elif user_type == "Customer":
            customer = customer + 1
        else:
            pass
    return [customer, subscriber]


user_type_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)


print("\nTASK 7: Check the chart!")


# In[18]:


input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because in some lines of the archive there's not information about the gender"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------


# In[25]:


input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().


def calculate_median(items):

    """
    return the median number of list.
    Args:
        param1: list with some columns
    Returns:
        median of list.
    """

    size = len(items)
    n = size // 2
    if size % 2:
        return items[n]
    median = (items[n] + items[n - 1]) / 2
    return median


trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = sorted([int(x) for x in trip_duration_list])
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = round(sum(trip_duration_list) / len(trip_duration_list))
median_trip = calculate_median(trip_duration_list)


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------


# In[26]:


input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()

start_station = column_to_list(data_list, 3)
user_types = set(start_station)

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------


# In[29]:


input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:

"""
      Example function with annotations.
      Args:
          param1: The first parameter.
          param2: The second parameter.
      Returns:
          List of X values

"""


# In[30]:


input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "no"

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
