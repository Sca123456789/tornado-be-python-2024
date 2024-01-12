# from collections import defaultdict


# def opening(file_path):

#     lines_by_day = defaultdict(list)
    
#     with open(file_path, "r") as f:
#         content = f.read()
#         lines = content.split('\n')
        
   
#         for line in lines:

#             if line.strip():

#                 if "from" in line:

#                     day = lines[lines.index(line) + 3].strip()
                    

#                     lines_by_day[day].append(line)
                    

#     latest_day = max(lines_by_day, key=lambda day: lines_by_day[day])
    

#     print("Lines for the latest day:")
#     for line in lines_by_day[latest_day]:
#         print(line)
    
#     print("Content of the latest dictionary:")
#     print(lines_by_day[latest_day])

# file_path = "/Users/tornado-02/Desktop/tornado-be-python-2024/lesson_day_08/excercise_2/mail-box.txt"
# opening(file_path)


# import os 
# print(os.getcwd())

# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as f:
#             content = f.read()
#         return content
#     except Exception as e:
#         print(f"An error occurred while reading the file: {e}")
#         return None

# def process_lines(content):
#     lines = content.split('\n')
#     dates = [re.search(r'(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat)\s\w{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2}\s\d{4}', line) for line in lines]
#     dates = [date.group() for date in dates if date is not None]
#     return dates

# def get_latest_day(dates):
#     day_dict = {}
#     for date in dates:
#         day = date.split(' ')[0]
#         if day in day_dict:
#             day_dict[day] += 1
#         else:
#             day_dict[day] = 1
#     latest_day = max(day_dict, key=day_dict.get)
#     return latest_day, day_dict[latest_day]

# def print_results(latest_day, count):
#     print(f"Latest day: {latest_day}")
#     print(f"Lines for the latest day: {count}")

# def main():
#     file_path = "/Users/tornado-02/Desktop/tornado-be-python-2024/lesson_day_08/excercise_2/mail-box.txt"
#     content = read_file(file_path)
#     if content is not None:
#         dates = process_lines(content)
#         latest_day, count = get_latest_day(dates)
#         print_results(latest_day, count)

# if __name__ == "__main__":
#     main()


# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.readlines()
#         return content
#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return None

# def process_lines(lines):
#     dates = []
#     for line in lines:
#         line = line.strip()
#         if line:
#             dates.append(line.split(' ')[0])
#     return dates

# def get_latest_day(dates):
#     day_dict = {}
#     for day in dates:
#         if day in day_dict:
#             day_dict[day] += 1
#         else:
#             day_dict[day] = 1
#     latest_day = max(day_dict, key=day_dict.get)
#     return latest_day, day_dict[latest_day]

# def print_results(latest_day, count):
#     print(f"Latest day: {latest_day}")
#     print(f"Lines for the latest day: {count}")

# def main():
#     file_path = "/Users/tornado-02/Desktop/tornado-be-python-2024/lesson_day_08/excercise_2/mail-box.txt"
#     content = read_file(file_path)
#     if content is not None:
#         dates = process_lines(content)
#         latest_day, count = get_latest_day(dates)
#         print_results(latest_day, count)

# if __name__ == "__main__":
#     main()

import os
import re

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def process_lines(content):
    lines = content.split('\n')
    dates = [re.search(r'(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat)\s\w{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2}\s\d{4}', line) for line in lines]
    dates = [date.group() for date in dates if date is not None]
    return dates

def get_latest_day(dates):
    day_dict = {}
    for date in dates:
        day = date.split(' ')[0]
        if day in day_dict:
            day_dict[day] += 1
        else:
            day_dict[day] = 1
    return day_dict

def print_results(day_dict):
    for day, count in day_dict.items():
        print(f"Day: {day} | Lines: {count}")

def main():
    file_path = "/Users/tornado-02/Desktop/tornado-be-python-2024/lesson_day_08/excercise_2/mail-box.txt"
    content = read_file(file_path)
    if content is not None:
        dates = process_lines(content)
        day_dict = get_latest_day(dates)
        print_results(day_dict)

if __name__ == "__main__":
    main()