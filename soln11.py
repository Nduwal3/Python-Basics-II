# Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, find the extension. 
# For README.txt, the extension should be txt. Write code using slice operations that will give the name without the extension.
#  Does your code work on filenames of arbitrary length? 


# for 3 character file extension
file_name = 'README.txt'
extension = file_name[-3:]
print(extension)

# for arbitary length file extension
find_extension = lambda filename: filename.split('.')[1]

filename = "image.jpeg"
ext = find_extension(filename)
print(ext)
