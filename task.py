def task_1(): # Lists

    origional_list = ["Geoff", "Jeff", "Jeffrey"]
    origional_list.append("Adam")
    origional_list.pop("Jeff")
    origional_list.copy = new_list
    print(origional_list)


    return new_list


def task_2(): # Dictionaries

    keys = ("name", "age", "profession")
    values = ("Geoff", 35, "technician")
    person = {keys + values}

    car = {
    "make": "Ford",
    "model": "Focus",
    "engine": 1.6,
    "colour": "blue"
}
    person.append{"car"}

    return person


def task_3(): # Tuples
    student_1 = ("Geoff", "Maths", 80)
    student_2 = (name, subject, score)
    name = "Enter name"
    subject = "Enter subject"
    score = "Enter score"(int)
    print(student_2)

    students = student_1 + student_2

    return students


def task_4(): # Sets
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya","sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}
    fruits_1.remove("sprite")
    fruits_2.remove("steak")
    print(fruits_1)
    print(fruits_2)
    print(fruits_1.intersection(fruits_2)) #duplicate fruits
    symmetric_difference = fruits_1.symmetric_difference(fruits_2)
    print(symmetric_difference)

    duplicate_fruits = None # This should be a tuple containing all the fruits in both tuples
    individual_fruits = None # This should be a tuple containing only the individual fruits


    return [duplicate_fruits, individual_fruits] # Note - functions can only return one data item - so both tuples
                                                 # are contained inside a single list
print(task_1())
print(task_2())
print(task_3())
print(task_4())
