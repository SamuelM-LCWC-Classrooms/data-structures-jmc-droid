def task_1():  # Lists
    original_list = ["Geoff", "Jeff", "Jeffrey"]
    original_list.append("Adam")
    original_list.remove("Jeff")  # Using remove instead of pop to remove by value
    new_list = original_list.copy()  # Correcting the assignment
    print(original_list)
    return new_list

def task_2():  # Dictionaries
    keys = ("name", "age", "profession")
    values = ("Geoff", 35, "technician")
    person = dict(zip(keys, values))  # Use zip to combine keys and values into a dictionary

    car = {
        "make": "Ford",
        "model": "Focus",
        "engine": 1.6,
        "colour": "blue"
    }
    person["car"] = car  # Adding car details to person dictionary

    return person

def task_3():  # Tuples
    student_1 = ("Geoff", "Maths", 80)
    
    # Input values should be provided, but for this example, I'll set them as strings
    name = "John"
    subject = "Science"
    score = 85  # Assuming input is cast to an integer
    student_2 = (name, subject, score)
    
    print(student_2)

    students = student_1 + student_2  # Combining the two tuples

    return students

def task_4():  # Sets
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya", "sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}
    
    fruits_1.remove("sprite")
    fruits_2.remove("steak")
    
    print(fruits_1)
    print(fruits_2)
    
    duplicate_fruits = tuple(fruits_1.intersection(fruits_2))  # Duplicate fruits
    symmetric_difference = tuple(fruits_1.symmetric_difference(fruits_2))  # Individual fruits
    
    print(duplicate_fruits)  # Printing the duplicates
    print(symmetric_difference)  # Printing the unique fruits
    
    return [duplicate_fruits, symmetric_difference]  # Returning both tuples inside a list

# Testing the tasks
print(task_1())
print(task_2())
print(task_3())
print(task_4())
