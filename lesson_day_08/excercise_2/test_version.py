
import re

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            for c in content:
                if c.startswith('From'):
                    # print(c) 
                    d = c.split(" ")[1]
                    print(d)
        return content
    except Exception as e:
        # print(f"Error: {str(e)}")
        return None

def process_lines(content):
    lines = content.split('\n')
    dates = [re.search(r'(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat)\s\w{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2}\s\d{4}', line) for line in lines if line.strip()]
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
    # print(content)
    
    # if content is not None:
    #     dates = process_lines(content)
    #     day_dict = get_latest_day(dates)
        # print_results(day_dict)

if __name__ == "__main__":
    main()
