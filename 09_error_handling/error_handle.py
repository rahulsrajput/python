#Old way
file = open('youtube.txt', 'r')

try:
    file.write('chai aur code')
finally:
    file.close()




# Best Way 
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')