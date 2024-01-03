def change():
    try:
        with open("romeo.txt", "r") as f:
            file_content = f.read()
            convertion = file_content.split()
            unique_words = list(set(convertion))
            unique_words.sort()
            print(unique_words)

    except FileNotFoundError:
        print("File not found.")
    except IOError as e:
        print(f"Error reading the file: {e}")

change()

