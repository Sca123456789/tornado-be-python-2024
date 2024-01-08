file_path = "sample.txt"
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")



try:
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("From"):
                line = line.strip()
                print(line)

                
                
    
except FileNotFoundError:
    print("We could not find the file you're looking for. :)")
