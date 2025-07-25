# two ways to handle file
# 1.
file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

# 2.
with open('youtube.txt', 'w') as file:
    file.write("Video downloading...")