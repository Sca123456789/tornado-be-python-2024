# file_path = "word.txt"

# def opening():
#     with open(file_path, "r") as f:
#         content = f.read()
#         print(content)
    
#     opening()
file_path = "/Users/tornado-02/Desktop/tornado-be-python-2024/lesson_day_08/excercise_1/word.txt"

def opening(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        print(content)
        word_dictionary = {line.strip(): line.strip() for line in content.split('\n') if line.strip()}
        print(word_dictionary)
opening(file_path)