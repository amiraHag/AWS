f = open("some_file.txt", "r")
content = f.read()
f.close()
print(content)



f2 = open("text1.txt","w")
f2.write("This is a test file.\n")
f2.write("This file is used to test file handling in Python.\n")
f2.close()

with open("some_file.txt", "r") as f:
    content3 = f.read()

print(content3)