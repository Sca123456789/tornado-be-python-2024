
# file_path = open("word.txt", "r") 
# d = dict()

# try: 
#     # with open(file_path, "r") as file:
#         file_content = file_path.read()
#         # print(file_content)
#         for line in file_content:
#             line = line.strip()
#             line = line.lower()
#             words = line.split(" ")
            
#             for word in words:
#                 if word in d:
#                     d[word] = d[word] + 1
#                 else:
#                     d[word] = 1
#         for key in list(d.keys()):
#                         print(key, ":", d[key])
            
        
# except FileNotFoundError:
#     print("sorry we could not find the file youre looking for")


# the new version of this code :

# file_path = "word.txt"
# d = dict()

# try:
#     with open(file_path, "r") as file:
#         file_content = file.read()
#         for line in file_content.splitlines():
#             line = line.strip().lower()
#             words = line.split(" ")

#             for word in words:
#                 if word in d:
#                     d[word] += 1
#                 else:
#                     d[word] = 1

#         # Move this part outside the first for loop
#         for key in d.keys():
#             print(key, ":", d[key])

# except FileNotFoundError:
#     print("Sorry, we could not find the file you're looking for.")
# except Exception as e:
#     print(f"An error occurred: {e}")




