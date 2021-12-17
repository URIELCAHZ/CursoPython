

# with open('C:\\Users\\URIELXD\\Documents\\CursoPythonPaco\\CursoPython\\fifteenth_clas\\pi_digits.txt') as file_object:
#     content = file_object.read()
#     for line in file_object:
#         print(line.rstrip())

# file_object = open('C:\\Users\\URIELXD\\Documents\\CursoPythonPaco\\CursoPython\\fifteenth_clas\\pi_digits.txt')

# file_object.read()

# file_object.close()

with open('C:\\Users\\URIELXD\\Documents\\CursoPythonPaco\\CursoPython\\fifteenth_clas\\pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:

    pi_string += line.strip()

print(pi_string)
    
    
