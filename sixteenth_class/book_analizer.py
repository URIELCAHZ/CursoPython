import sys

if (len(sys.argv)) <= 1:
    print("You should pass a file path")
    exit()

file_name = sys.argv[1]
#filename = "C:\\Users\\URIELXD\\Documents\\CursoPythonPaco\\CursoPython\\sixteenth_class\\Alice.txt"

try:
    with open(filename) as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("Sorry, file no found")
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")