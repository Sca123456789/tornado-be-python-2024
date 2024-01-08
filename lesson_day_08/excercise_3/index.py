from collections import defaultdict
def count_messagas(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sender_counts = defaultdict(int)
        for line in lines:
            sender = line.split('From ')[1].split('<')[0].strip()
            sender_counts[sender] +=1 
            return sender_counts
        
        file_path = "/Users/tornado-02/Desktop/tornado-be-python-2024/lesson_day_08/excercise_3/mail.txt"
        print(count_messagas(file_path))