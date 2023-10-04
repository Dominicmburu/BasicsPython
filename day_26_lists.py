import random

numbers = [1,2,3,4,5]
new_list = [n+1 for n in numbers]
# print(new_list)

name = "Angela"
new_list = [letter for letter in name]
# print(new_list)

new_list = [num * 2 for num in range(1,5)]
# print(new_list)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
longer_names = [name.upper() for name in names if len(name) > 5]
# print(longer_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
# print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
# print(result)

with open("day_26_file1.txt") as file1:
    file_1_data = file1.readlines()

with open("day_26_file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
# print(result)

## new_dict = {new_key:new_value for item in list}
## new_dict = {new_key:new_value for (key,value) in dict.items()}
## new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {students:score for (students, score) in students_scores.items() if score >= 60}
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
result = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
# print(result)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas as pd

# student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

# for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row["score"])

df = pd.read_csv("day_26_NATO.csv")
word = input("Enter a word: ").upper()
phonetic_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}
result = [phonetic_dict[letter] for letter in word]
print(result)









