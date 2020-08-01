# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']

# Concatenate both the strings
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Append the list
new_class = class_1+class_2
print(new_class)

# Print updated list
new_class.append('Peter Warden')
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

# Create the Dictionary
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}

total=sum(courses.values())
print(total)

percentage=(total/500)*100
print(percentage)

mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,
'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

# Slice the dict and stores  the all subjects marks in variable

topper=max(mathematics,key=mathematics.get)
print(topper)

first_name=(topper.split()[0])
last_name=(topper.split()[1])

full_name=last_name.upper()+' '+first_name.upper()
certificate_name=full_name
print(certificate_name)


